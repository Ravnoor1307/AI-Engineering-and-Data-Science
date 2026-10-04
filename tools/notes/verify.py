"""Verify that no notebook was modified, and validate every generated artefact.

Checks performed
----------------
1. Every notebook referenced by the manifest still hashes to the value recorded
   at extraction time (proves the build is read-only).
2. Every generated HTML file parses, has exactly one <html>/<body>, no unresolved
   template placeholders, a matching TOC/section count, and valid internal anchors.
3. Every generated PDF starts with %PDF-, ends with %%EOF, and is not a renamed
   HTML file.
"""
from __future__ import annotations

import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "tools" / "notes" / "notes_manifest.json"

VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "param", "source", "track", "wbr"}


class Checker(HTMLParser):
    """Minimal structural validator: tag balance plus id collection."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.ids: set[str] = set()
        self.counts: dict[str, int] = {}
        self.html = 0
        self.body = 0

    def handle_starttag(self, tag, attrs):
        self.counts[tag] = self.counts.get(tag, 0) + 1
        if tag == "html":
            self.html += 1
        if tag == "body":
            self.body += 1
        d = dict(attrs)
        if "id" in d and d["id"]:
            self.ids.add(d["id"])
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if not self.stack:
            self.errors.append(f"stray </{tag}>")
            return
        if self.stack[-1] != tag:
            self.errors.append(f"mismatched </{tag}>, open: {self.stack[-1]}")
            if tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.stack.pop()
                self.stack.pop()
            return
        self.stack.pop()


def check_notebooks(manifest: dict) -> tuple[int, list[str]]:
    problems: list[str] = []
    checked = 0
    for unit in manifest["units"]:
        for src in unit.get("sources", []):
            path = ROOT / src["notebook"]
            if not path.exists():
                problems.append(f"missing notebook: {src['notebook']}")
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            checked += 1
            if digest != src["sha256"]:
                problems.append(
                    f"MODIFIED: {src['notebook']} "
                    f"(manifest {src['sha256'][:12]} vs now {digest[:12]})"
                )
    return checked, problems


def check_html(path: Path) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8")

    placeholders = re.findall(r"\{\{\s*\w+\s*\}\}", text)
    if placeholders:
        problems.append(f"unresolved placeholders: {sorted(set(placeholders))}")

    parser = Checker()
    parser.feed(text)
    parser.close()

    if parser.html != 1:
        problems.append(f"<html> count = {parser.html}")
    if parser.body != 1:
        problems.append(f"<body> count = {parser.body}")
    if parser.stack:
        problems.append(f"unclosed tags: {parser.stack[:5]}")
    for err in parser.errors[:5]:
        problems.append(err)

    sections = set(re.findall(r'<section class="section-card" id="([^"]+)"', text))
    anchors = set(re.findall(r'class="toc-link" href="#([^"]+)"', text))
    missing = anchors - {a for a in anchors if f'id="{a}"' in text}
    if missing:
        problems.append(f"TOC links without a target: {sorted(missing)}[:5]")
    orphan_sections = sections - anchors
    if orphan_sections:
        problems.append(f"sections missing from TOC: {sorted(orphan_sections)[:5]}")

    if text.count('class="code-shell"') == 0 and "code" in path.stem.lower():
        problems.append("no code blocks rendered")

    for needed in ('id="savePdfBtn"', "reading-progress", "@media print", "<style>", "<script>"):
        if needed not in text:
            problems.append(f"missing required feature: {needed}")

    if re.search(r"https?://[^/\s\"']+\.(?:png|jpe?g|gif|svg|webp)", text):
        problems.append("remote image reference (breaks standalone use)")

    return problems


def check_pdf(path: Path) -> list[str]:
    problems: list[str] = []
    if not path.exists():
        return ["PDF missing"]
    data = path.read_bytes()
    if not data.startswith(b"%PDF-"):
        problems.append("missing %PDF- header")
    if b"%%EOF" not in data[-4096:]:
        problems.append("missing %%EOF trailer")
    if len(data) < 5000:
        problems.append(f"suspiciously small: {len(data)} bytes")
    if b"<html" in data[:4000].lower():
        problems.append("looks like HTML renamed to .pdf")
    return problems


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    units = manifest["units"]

    nb_checked, nb_problems = check_notebooks(manifest)
    print(f"notebooks verified unmodified : {nb_checked}")
    for p in nb_problems:
        print(f"  !! {p}")

    html_bad = 0
    pdf_bad = 0
    total_pages = 0
    total_bytes = 0

    for unit in units:
        html_rel = unit["html"]
        html_path = ROOT / html_rel
        hproblems = check_html(html_path)
        pproblems = check_pdf(ROOT / unit["pdf"]) if unit.get("pdf") else ["no pdf entry"]

        total_bytes += html_path.stat().st_size
        total_pages += unit.get("pdf_pages") or 0

        status = "OK"
        if hproblems or pproblems:
            status = "FAIL"
            html_bad += bool(hproblems)
            pdf_bad += bool(pproblems)
            print(f"[{status}] {unit['unit']}")
            for p in hproblems:
                print(f"    html: {p}")
            for p in pproblems:
                print(f"    pdf : {p}")

    print()
    print(f"units            : {len(units)}")
    print(f"html failures    : {html_bad}")
    print(f"pdf failures     : {pdf_bad}")
    print(f"total html bytes : {total_bytes:,}")
    print(f"total pdf pages  : {total_pages}")
    print(f"notebook issues  : {len(nb_problems)}")

    return 1 if (html_bad or pdf_bad or nb_problems) else 0


if __name__ == "__main__":
    raise SystemExit(main())