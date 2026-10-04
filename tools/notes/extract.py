"""Extract structured topic blocks from theory notebooks.

The extractor walks notebook cells in order and groups them into topic blocks
anchored on Markdown headings. This produces a faithful intermediate
representation (IR) that the renderer turns into study notes.

IR shape
--------
{
  "notebook": "relative/path.ipynb",
  "title": "Notebook H1 or filename",
  "blocks": [
      {
          "level": 2,
          "title": "np.array - basic",
          "slug": "np-array-basic",
          "prose": "...markdown text...",
          "code": ["...source...", "..."],
          "tags": ["deep-dive", "common-mistakes", ...],
      }
  ],
}
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")

# Notebook metadata that describes the pedagogical intent of a block.
TAG_PATTERNS = {
    "deep-dive": re.compile(r"deep\s*dive|deep\s*understanding", re.I),
    "why": re.compile(r"\bwhy\b|what/why|importance", re.I),
    "how": re.compile(r"\bhow\b|how it works|mechanism|semantics|internals", re.I),
    "what": re.compile(r"\bwhat\b|introduction|overview|introduction?", re.I),
    "common-mistakes": re.compile(r"common mistakes?|mistakes?|pitfalls?|gotchas?", re.I),
    "edge-cases": re.compile(r"edge cases?|boundary", re.I),
    "when-to-use": re.compile(r"when to use|use cases?|applications?", re.I),
    "real-world": re.compile(r"real world|production|industry", re.I),
    "interview": re.compile(r"interview", re.I),
    "parameters": re.compile(r"parameters?", re.I),
    "comparison": re.compile(r"vs\b|versus|comparison|compare", re.I),
    "performance": re.compile(r"performance|optimi[sz]|speed|benchmark", re.I),
}

# Fenced code inside Markdown is already code; keep it but mark it.
FENCE_RE = re.compile(r"^```", re.MULTILINE)

EMOJI_HEADING_RE = re.compile(
    r"^[\W_]*"
    r"(?:[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u2190-\u21FF\u2B05\u2B1B\u2B50\u274F\u2764\uFE0F]+\s*)+",
)


def clean_title(raw: str) -> str:
    """Strip emoji/decoration noise from a heading string."""
    title = raw.strip()
    title = title.replace("\u00a0", " ")
    title = EMOJI_HEADING_RE.sub("", title).strip()
    title = re.sub(r"\s{2,}", " ", title)
    # Trailing punctuation used as visual separators in some notebooks.
    title = re.sub(r"[\u2022\u2014\u2013\-_=]{3,}$", "", title).strip()
    return title


def slugify(text: str, used: set[str]) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "section"
    if base in used:
        n = 2
        while f"{base}-{n}" in used:
            n += 1
        base = f"{base}-{n}"
    used.add(base)
    return base


def detect_tags(title: str, prose: str) -> list[str]:
    tags: list[str] = []
    haystack = f"{title}\n{prose[:600]}"
    for tag, pattern in TAG_PATTERNS.items():
        if pattern.search(title):
            tags.append(tag)
        elif tag in {"deep-dive", "common-mistakes", "edge-cases", "performance", "real-world"}:
            if pattern.search(haystack):
                tags.append(tag)
    seen: set[str] = set()
    ordered: list[str] = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            ordered.append(t)
    return ordered


def split_fenced(prose: str) -> tuple[str, list[str]]:
    """Split fenced code blocks out of Markdown prose."""
    if "```" not in prose:
        return prose, []

    out: list[str] = []
    inside = False
    buf: list[str] = []
    prose_parts: list[str] = []

    for line in prose.splitlines():
        if line.strip().startswith("```"):
            if inside:
                out.append("\n".join(buf).strip("\n"))
                buf = []
                inside = False
            else:
                inside = True
                # language token on the fence line is dropped
            continue
        if inside:
            buf.append(line)
        else:
            prose_parts.append(line)

    return "\n".join(prose_parts).strip(), [c for c in out if c.strip()]


def sanitize_prose(prose: str) -> str:
    """Light cleanup of notebook-authored Markdown."""
    if not prose.strip():
        return ""
    lines = prose.splitlines()
    cleaned: list[str] = []
    for line in lines:
        stripped = line.rstrip()
        # notebook separators such as "***" or "---" inside body text
        if re.fullmatch(r"[-*_=]{5,}", stripped.strip()):
            continue
        cleaned.append(stripped)

    text = "\n".join(cleaned)
    # collapse 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_notebook(path: Path, root: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        nb = json.load(fh)

    cells = nb.get("cells", [])
    used_slugs: set[str] = set()
    blocks: list[dict] = []
    nb_title = ""
    order = 0

    current: dict | None = None

    def flush() -> None:
        nonlocal current
        if current is None:
            return
        prose, fenced = split_fenced(current["prose"])
        prose = sanitize_prose(prose)
        code = list(current["code"]) + fenced
        if not prose and not code:
            current = None
            return
        current["prose"] = prose
        current["code"] = code
        current["tags"] = detect_tags(current["title"], prose)
        blocks.append(current)
        current = None

    for cell in cells:
        ctype = cell.get("cell_type")
        src = "".join(cell.get("source", []))

        if ctype == "markdown":
            # Find the first heading line to decide whether this cell opens a block.
            lines = src.splitlines()
            first_heading_idx = None
            for i, line in enumerate(lines):
                if HEADING_RE.match(line):
                    first_heading_idx = i
                    break

            if first_heading_idx is None:
                if current is not None:
                    current["prose"] += "\n\n" + src
                elif not blocks and src.strip():
                    # Leading untitled Markdown before any heading: treat as intro.
                    current = {
                        "level": 2,
                        "title": "Overview",
                        "slug": slugify("overview", used_slugs),
                        "prose": src,
                        "code": [],
                        "order": order,
                    }
                    order += 1
                continue

            heading_line = lines[first_heading_idx]
            level = len(HEADING_RE.match(heading_line).group(1))
            title = clean_title(HEADING_RE.match(heading_line).group(2))

            if level == 1 and not nb_title:
                nb_title = title
                # Document-level H1 does not create a section.
                remainder = "\n".join(lines[first_heading_idx + 1 :]).strip()
                if remainder:
                    if current is None:
                        current = {
                            "level": 2,
                            "title": f"Overview — {title}",
                            "slug": slugify(f"overview-{title}", used_slugs),
                            "prose": remainder,
                            "code": [],
                            "order": order,
                        }
                        order += 1
                    else:
                        current["prose"] += "\n\n" + remainder
                continue

            flush()
            remainder = "\n".join(lines[first_heading_idx + 1 :]).strip()
            current = {
                "level": min(level, 3),
                "title": title,
                "slug": slugify(title, used_slugs),
                "prose": remainder,
                "code": [],
                "order": order,
            }
            order += 1

        elif ctype == "code":
            if not src.strip():
                continue
            if current is None:
                current = {
                    "level": 2,
                    "title": "Code Walkthrough",
                    "slug": slugify("code-walkthrough", used_slugs),
                    "prose": "",
                    "code": [],
                    "order": order,
                }
                order += 1
            current["code"].append(src.rstrip())

    flush()

    rel = path.relative_to(root).as_posix()
    return {
        "notebook": rel,
        "title": nb_title or path.stem,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "md_cells": sum(1 for c in cells if c.get("cell_type") == "markdown"),
        "code_cells": sum(1 for c in cells if c.get("cell_type") == "code"),
        "blocks": blocks,
    }


def strip_heading_lines(prose: str) -> str:
    """Remove stray heading lines left inside prose so structure stays clean."""
    kept = [ln for ln in prose.splitlines() if not HEADING_RE.match(ln)]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()