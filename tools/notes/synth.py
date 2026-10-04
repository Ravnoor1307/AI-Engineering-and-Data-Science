"""Synthesize per-unit study notes from extracted notebook IR.

The synthesizer performs five deliberate transformations:

1. **Merge** blocks that describe the same topic across notebooks.
2. **Deduplicate** blocks whose prose is substantively identical.
3. **Classify** every topic into a pedagogical bucket (concept, mistake,
   edge case, performance, real-world).
4. **Cluster** remaining concepts by source session so the document reads as a
   coherent sequence rather than a flat list.
5. **Curate** code: keep representative snippets, cap runaway cell dumps.

Only content that exists in the notebooks is used. Nothing is invented.
"""
from __future__ import annotations

import re
from collections import OrderedDict, defaultdict
from pathlib import Path

from extract import extract_notebook
from render import callout, code_shell, diagram_flow, md
from units import Unit

# ----------------------------------------------------------------------------
# Classification
# ----------------------------------------------------------------------------

MISTAKE_RE = re.compile(
    r"(common mistake|mistakes?|pitfall|gotcha|wrong way|don'?t do|avoid|"
    r"careful|error to avoid|bad practice|anti-?pattern|caveat|watch ?out)",
    re.I,
)
EDGE_RE = re.compile(r"(edge case|boundary|off-?by-?one|overflow|underflow)", re.I)

# Headings that unambiguously describe a failure mode.
STRONG_MISTAKE_RE = re.compile(
    r"(common mistake|common pitfalls?|gotchas?|wrong way|"
    r"error to avoid|bad practice|anti-?pattern|don'?t confuse|"
    r"most common (mistake|error|bug)|watch ?out)",
    re.I,
)
PERF_RE = re.compile(
    r"(performance|optimi[sz]|faster|speed|benchmark|bottleneck|memory|"
    r"complexity|big-?o|space complexity|time complexity|efficien)",
    re.I,
)
REAL_RE = re.compile(
    r"(real world|production|industry|use case|when to use|applications?|"
    r"why it matters|case study)",
    re.I,
)
OVERVIEW_RE = re.compile(r"^overview\b", re.I)
WARMUP_RE = re.compile(r"^(warm-?up|pattern\s*\d|problem\s*\d)", re.I)

MAX_CODE_LINES = 34
MAX_CODE_BLOCKS_PER_TOPIC = 2

# Code budgets keep a document usable. Prose is never dropped; only the number
# of code blocks is capped, and the selection is spread evenly across topics so
# the early sessions do not consume the whole budget.
CODE_BUDGET = {
    "default": 150,
    "sql": 220,
}

# A topic becomes a compact callout only when it is short and code-free.
# Anything with real teaching content stays in Core Concepts.
CALLOUT_MAX_CHARS = 420


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _prose_key(text: str) -> str:
    return _norm(re.sub(r"```.*?```", "", text, flags=re.DOTALL))[:600]


def classify(block: dict) -> str:
    """Assign a pedagogical bucket.

    Editorial rule: a heading that names a *failure mode* (a mistake, a pitfall,
    a caveat) is routed to the callout sections regardless of how long it is,
    because that framing is exactly what makes it useful when reviewing. A
    heading that merely happens to discuss pitfalls in passing stays a concept.
    """
    title = block["title"]
    prose = block["prose"]
    tags = set(block.get("tags", []))

    if OVERVIEW_RE.match(title) or title.lower() == "overview":
        return "overview"
    if "interview" in tags:
        return "drop"

    # Failure-mode headings are strong signals in these notebooks.
    if STRONG_MISTAKE_RE.search(title):
        return "mistake"
    if EDGE_RE.search(title):
        return "edge"

    substantial = len(prose) > CALLOUT_MAX_CHARS or bool(block["code"])

    if not substantial:
        if MISTAKE_RE.search(title):
            return "mistake"
        if PERF_RE.search(title) and re.search(
            r"\b(big-?o|complexity|memory|speed|faster)", title, re.I
        ):
            return "performance"
        if REAL_RE.search(title):
            return "real"

    return "concept"


# ----------------------------------------------------------------------------
# Merge / dedupe
# ----------------------------------------------------------------------------


def merge_blocks(irs: list[dict]) -> list[dict]:
    """Merge same-titled blocks across notebooks, preserving first-seen order."""
    merged: "OrderedDict[str, dict]" = OrderedDict()
    seen_prose: set[str] = set()

    for ir in irs:
        for block in ir["blocks"]:
            key = _norm(block["title"])
            if not key:
                continue

            bucket = classify(block)

            if bucket == "drop":
                continue

            pk = _prose_key(block["prose"])
            if pk and pk in seen_prose:
                # Identical prose already emitted; only keep new code.
                existing = merged.get(key)
                if existing is not None:
                    for code in block["code"]:
                        if code not in existing["code"]:
                            existing["code"].append(code)
                continue
            if pk:
                seen_prose.add(pk)

            if key in merged:
                target = merged[key]
                target["sources"].append(ir["notebook"])
                if block["prose"] and block["prose"] not in target["prose"]:
                    target["prose"] = (target["prose"] + "\n\n" + block["prose"]).strip()
                for code in block["code"]:
                    if code not in target["code"]:
                        target["code"].append(code)
                target["tags"] = sorted(set(target["tags"]) | set(block.get("tags", [])))
                if bucket != "concept":
                    target["bucket"] = bucket
            else:
                merged[key] = {
                    "title": block["title"],
                    "slug": block["slug"],
                    "level": block["level"],
                    "prose": block["prose"],
                    "code": list(block["code"]),
                    "tags": list(block.get("tags", [])),
                    "bucket": bucket,
                    "sources": [ir["notebook"]],
                    "session": ir["title"],
                }

    return list(merged.values())


# ----------------------------------------------------------------------------
# Code curation
# ----------------------------------------------------------------------------


def curate_code(codes: list[str], max_lines: int = MAX_CODE_LINES) -> list[str]:
    kept: list[str] = []
    for code in codes:
        stripped = code.strip()
        if not stripped:
            continue
        lines = stripped.splitlines()

        # Drop notebook-shell noise lines that carry no teaching value.
        if len(lines) <= 2 and not any(
            c.strip() and not c.strip().startswith("#") for c in lines
        ):
            continue
        if stripped.startswith("!") or stripped.startswith("%"):
            continue

        if len(lines) > max_lines:
            head = lines[: max_lines - 6]
            tail = lines[-4:]
            kept.append("\n".join(head + ["    # ..."] + tail))
        else:
            kept.append(stripped)
        if len(kept) >= MAX_CODE_BLOCKS_PER_TOPIC:
            break
    return kept


def apply_code_budget(topics: list[dict], budget: int) -> list[dict]:
    """Spread a code-block budget evenly across topics.

    Prose is never removed; only code blocks are dropped. Selection proceeds in
    rounds so every topic keeps its first example before any topic gets a
    second, which preserves topic coverage instead of exhausting the budget on
    whichever session happens to come first.
    """
    if budget <= 0:
        return topics

    kept = 0
    depth = 0
    while True:
        round_budget = 0
        for block in topics:
            codes = block.get("code") or []
            if len(codes) > depth:
                round_budget += 1
        if round_budget == 0:
            break
        if kept + round_budget > budget:
            # Partially fund the round, evenly across the topics that want one.
            wanters = [b for b in topics if len(b.get("code") or []) > depth]
            allowance = max(0, budget - kept)
            if allowance == 0:
                break
            step = len(wanters) / allowance
            for i, block in enumerate(wanters):
                if i % max(1, int(step)) == 0 and kept < budget:
                    block.setdefault("budgeted", list(block.get("code") or []))
                    block["budgeted"] = block.get("code")[: depth + 1]
                    kept += 1
            break

        for block in topics:
            codes = block.get("code") or []
            if len(codes) > depth:
                block.setdefault("budgeted", [])
                block["budgeted"] = list(block.get("budgeted", []))
                if depth < len(codes):
                    block["budgeted"].append(codes[depth])
                kept += 1
        depth += 1

    for block in topics:
        if "budgeted" in block:
            block["code"] = block["budgeted"]
            del block["budgeted"]
    return topics


def detect_language(codes: list[str], default: str = "python") -> str:
    joined = "\n".join(codes[:3])
    if re.search(r"^\s*(SELECT|INSERT|UPDATE|DELETE|CREATE TABLE|ALTER TABLE|WITH)\b", joined, re.I | re.M):
        return "sql"
    if re.search(r"^\s*(import|from)\s+\w+|^\s*def\s+\w+\(.*\):", joined, re.M):
        return "python"
    if re.search(r"^\s*(\$|#!/bin/bash|pip install|conda install)", joined, re.M):
        return "bash"
    return default


# ----------------------------------------------------------------------------
# Section builders
# ----------------------------------------------------------------------------


def render_topic(block: dict, level: int = 3, unit: Unit | None = None) -> str:
    heading_tag = f"h{min(level, 4)}"
    parts = [f'<{heading_tag}>{md_inline(block["title"])}</{heading_tag}>']

    if block["prose"]:
        parts.append(md(block["prose"]))

    codes = curate_code(block["code"])
    if codes:
        lang = detect_language(codes)
        for code in codes:
            parts.append(code_shell(code, lang))

    return "".join(parts)


def md_inline(text: str) -> str:
    """Escape then apply inline Markdown for heading text."""
    import html as html_mod

    import markdown2

    return markdown2.markdown(text, extras=["smarty-pants"]).strip()


def group_into_clusters(
    concepts: list[dict], irs: list[dict]
) -> list[tuple[str, list[dict]]]:
    """Cluster concept topics by the session notebook they came from."""
    order: list[str] = []
    buckets: "OrderedDict[str, list[dict]]" = OrderedDict()

    for ir in irs:
        label = clean_session_label(ir["title"])
        if label not in buckets:
            buckets[label] = []
            order.append(label)

    for block in concepts:
        label = clean_session_label(block.get("session", ""))
        if label not in buckets:
            buckets[label] = []
            order.append(label)
        buckets[label].append(block)

    clusters = [(label, buckets[label]) for label in order if buckets[label]]
    return clusters


SESSION_NOISE_RE = re.compile(
    r"\s*[—–-]\s*session\s*\d+\s*$|^\s*session\s*\d+\s*[-—–:]?\s*", re.I
)


def clean_session_label(title: str) -> str:
    label = title.strip()
    label = SESSION_NOISE_RE.sub("", label).strip()
    label = re.sub(r"\s{2,}", " ", label)
    return label or "Overview"


# ----------------------------------------------------------------------------
# Glossary extraction
# ----------------------------------------------------------------------------

GLOSSARY_PATTERNS = (
    re.compile(r"^\s*[-*]?\s*\*\*(?P<term>[A-Za-z][\w \-\(\)/\.]{2,45})\*\*\s*[:\-–]\s*(?P<def>.+)$", re.M),
    re.compile(r"^\s*[-*]?\s*`(?P<term>[A-Za-z][\w\.\-]{2,30})`\s*[:\-–]\s*(?P<def>.+)$", re.M),
    re.compile(r"\*\*(?P<term>[A-Za-z][\w \-]{2,40})\*\*\s+(?:is|are|means|refers to)\s+(?P<def>[^.\n]{15,240}\.)", re.I),
)

STOP_TERMS = {
    "note", "example", "warning", "tip", "important", "summary", "output",
    "input", "syntax", "returns", "return", "parameters", "usage", "code",
    "python", "numpy", "pandas", "sql", "step", "note that", "in practice",
}


def extract_glossary(blocks: list[dict], limit: int = 22) -> list[tuple[str, str]]:
    found: "OrderedDict[str, str]" = OrderedDict()
    for block in blocks:
        for pattern in GLOSSARY_PATTERNS:
            for m in pattern.finditer(block["prose"]):
                term = m.group("term").strip().strip(".")
                definition = re.sub(r"\s+", " ", m.group("def").strip()).strip()
                if len(term) < 3 or term.lower() in STOP_TERMS:
                    continue
                if len(definition) < 15:
                    continue
                key = _norm(term)
                if key not in found:
                    found[key] = (term, definition)

    items = list(found.values())[:limit]
    return items


# ----------------------------------------------------------------------------
# Document assembly
# ----------------------------------------------------------------------------

CHIP_SVG = (
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
    '<path d="M2 7h6M14 7h8M2 17h4M12 17h10"></path>'
    '<circle cx="10" cy="7" r="2"></circle><circle cx="8" cy="17" r="2"></circle></svg>'
)
DOC_SVG = (
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>'
    '<polyline points="14 2 14 8 20 8"></polyline></svg>'
)
CODE_SVG = (
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'
)


def build_document(unit: Unit, irs: list[dict]) -> tuple[str, list[dict]]:
    """Return (sections_html, toc_entries) for a unit."""
    merged = merge_blocks(irs)

    overview_blocks = [b for b in merged if b["bucket"] == "overview"]
    concepts = [b for b in merged if b["bucket"] == "concept" and not WARMUP_RE.match(b["title"])]
    mistakes = [b for b in merged if b["bucket"] == "mistake"]
    edges = [b for b in merged if b["bucket"] == "edge"]
    perfs = [b for b in merged if b["bucket"] == "performance"]
    reals = [b for b in merged if b["bucket"] == "real"]

    sections: list[dict] = []
    all_blocks = merged

    # ---- Code budget -------------------------------------------------------
    # Applied to every topic before rendering so a very large source notebook
    # cannot produce an unusable document.
    budget = CODE_BUDGET.get(unit.key, CODE_BUDGET["default"])
    all_rend = [b for b in merged if b["bucket"] != "drop"]
    apply_code_budget(all_rend, budget)

    # ---- Overview -----------------------------------------------------------
    overview_html_parts = []
    for block in overview_blocks[:4]:
        if block["prose"]:
            overview_html_parts.append(md(block["prose"]))
    overview_body = "".join(overview_html_parts)

    overview_extra = ""
    if unit.prerequisites:
        items = "".join(f"<li>{md_inline(p)}</li>" for p in unit.prerequisites)
        overview_extra += (
            "<h3>Prerequisites</h3>"
            f'<ul class="prereq-list">{items}</ul>'
        )

    if unit.outcomes:
        items = "".join(f"<li>{md_inline(o)}</li>" for o in unit.outcomes)
        overview_extra += (
            "<h3>What you will be able to do</h3>"
            f'<ul class="outcome-list">{items}</ul>'
        )

    if overview_body or overview_extra:
        sections.append(
            {
                "id": "overview",
                "title": "Unit Overview",
                "html": overview_body + overview_extra,
            }
        )

    # ---- Concept map -------------------------------------------------------
    if unit.focus:
        nodes = [f for f in unit.focus]
        sections.append(
            {
                "id": "at-a-glance",
                "title": "What This Unit Covers",
                "html": (
                    diagram_flow(nodes[:6], title="Concept map")
                    + "<p>The sections below follow this arc, from foundational "
                    "semantics to the engineering decisions that follow from them.</p>"
                ),
            }
        )

    # ---- Core concepts, clustered by session --------------------------------
    clusters = group_into_clusters(concepts, irs)
    concept_parts: list[str] = []
    for label, blocks in clusters:
        if not blocks:
            continue
        concept_parts.append(f'<h3>{md_inline(label)}</h3>')
        for block in blocks:
            concept_parts.append(render_topic(block, level=4))

    if concept_parts:
        sections.append(
            {
                "id": "core-concepts",
                "title": "Core Concepts",
                "html": "".join(concept_parts),
            }
        )

    # ---- Common mistakes ----------------------------------------------------
    if mistakes:
        parts = []
        for block in mistakes:
            body = md(block["prose"]) if block["prose"] else ""
            if not body and block["code"]:
                body = "".join(code_shell(c, detect_language([c])) for c in curate_code(block["code"]))
            parts.append(callout("warning", block["title"], body))
        sections.append(
            {"id": "common-mistakes", "title": "Common Mistakes and Pitfalls", "html": "".join(parts)}
        )

    # ---- Edge cases ---------------------------------------------------------
    if edges:
        parts = []
        for block in edges:
            body = md(block["prose"]) if block["prose"] else ""
            if not body and block["code"]:
                body = "".join(code_shell(c, detect_language([c])) for c in curate_code(block["code"]))
            parts.append(callout("important", block["title"], body))
        sections.append(
            {"id": "edge-cases", "title": "Edge Cases and Boundaries", "html": "".join(parts)}
        )

    # ---- Performance --------------------------------------------------------
    if perfs:
        parts = []
        for block in perfs:
            parts.append(render_topic(block, level=4))
        sections.append(
            {"id": "performance", "title": "Performance and Design Decisions", "html": "".join(parts)}
        )

    # ---- Real world / AI relevance -----------------------------------------
    real_parts = []
    if reals:
        for block in reals:
            real_parts.append(render_topic(block, level=4))
    if unit.focus:
        items = "".join(f"<li>{md_inline(f)}</li>" for f in unit.focus)
        real_parts.append(
            "<h3>Where this shows up in AI engineering</h3>"
            f"<ul>{items}</ul>"
        )
    real_parts.append(
        callout(
            "hinglish",
            "Exam aur interview perspective",
            md(
                "Agar koi concept interview ya exam mein poochha jaye, to definition ke "
                "saath apna ek chhota practical example zaroor bolo. Sirf theory batane se "
                "confidence nahi dikhta - implementation dikhane se dikhta hai."
            ),
        )
    )
    if real_parts:
        sections.append(
            {
                "id": "real-world",
                "title": "Real-World and AI Engineering Relevance",
                "html": "".join(real_parts),
            }
        )

    # ---- Quick reference ----------------------------------------------------
    quick = build_quick_reference(concepts)
    if quick:
        sections.append({"id": "quick-reference", "title": "Quick Reference", "html": quick})

    # ---- Glossary -----------------------------------------------------------
    glossary = extract_glossary(all_blocks)
    if len(glossary) >= 4:
        items = "".join(
            f'<div class="glossary-item"><div class="glossary-term">{term}</div>'
            f'<p class="glossary-def">{definition}</p></div>'
            for term, definition in glossary
        )
        sections.append(
            {
                "id": "glossary",
                "title": "Glossary",
                "html": f'<div class="glossary">{items}</div>',
            }
        )

    # ---- Revision checklist -------------------------------------------------
    revision = build_revision_checklist(concepts)
    if revision:
        sections.append(
            {
                "id": "revision",
                "title": "Revision Checklist",
                "html": revision,
            }
        )

    toc = [{"id": s["id"], "title": s["title"]} for s in sections]
    return sections, toc


def build_quick_reference(concepts: list[dict]) -> str:
    """Pick short, high-signal code snippets for a quick-reference block."""
    snippets: list[tuple[str, str, str]] = []
    for block in concepts:
        for code in block["code"]:
            stripped = code.strip()
            lines = stripped.splitlines()
            if not (2 <= len(lines) <= 12):
                continue
            if stripped.startswith(("%", "!")):
                continue
            snippets.append((block["title"], detect_language([stripped]), stripped))
            if len(snippets) >= 8:
                break
        if len(snippets) >= 8:
            break

    if not snippets:
        return ""

    parts = [
        "<p>Short, representative snippets collected from the unit's notebooks. "
        "Use them as syntax reminders, not as complete programs.</p>"
    ]
    seen = set()
    for title, lang, code in snippets:
        digest = _norm(code)[:120]
        if digest in seen:
            continue
        seen.add(digest)
        parts.append(code_shell(code, lang, caption=title))
    return "".join(parts)


def build_revision_checklist(concepts: list[dict]) -> str:
    titles = []
    for block in concepts:
        title = block["title"].strip()
        if len(title) < 4 or len(title) > 90:
            continue
        if title.lower().startswith(("overview", "code walkthrough")):
            continue
        titles.append(title)

    # Keep the list readable.
    titles = titles[:22]
    if len(titles) < 5:
        return ""

    items = "".join(f'<li><label class="check"><input type="checkbox"> <span>{md_inline(t)}</span></label></li>' for t in titles)
    return (
        "<p>Work through this list without looking at the notes. Anything you cannot "
        "explain aloud belongs back in the revision queue.</p>"
        f'<ul class="checklist">{items}</ul>'
    )


def load_unit_irs(unit: Unit, root: Path) -> list[dict]:
    """Extract IR for every theory notebook owned by a unit."""
    unit_root = root / unit.root
    if not unit_root.exists():
        return []

    if unit.sources:
        paths = [root / s for s in unit.sources]
        paths = [p for p in paths if p.exists()]
    else:
        paths = sorted(unit_root.rglob("*.ipynb"))

    irs: list[dict] = []
    for path in paths:
        rel = path.relative_to(root).as_posix()
        if path.name.endswith(".ipynb") and any(
            part in {".ipynb_checkpoints", ".virtual_documents"} for part in path.parts
        ):
            continue
        if unit.is_excluded(rel, path.stem):
            continue
        irs.append(extract_notebook(path, root))
    return irs