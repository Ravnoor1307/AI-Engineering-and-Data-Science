"""Build study-notes HTML for every registered curriculum unit.

Usage
-----
    python tools/notes/build_notes.py                # build all units
    python tools/notes/build_notes.py --unit numpy   # build one unit
    python tools/notes/build_notes.py --no-pdf       # HTML only
"""
from __future__ import annotations

import argparse
import html as html_mod
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from render import pygments_css  # noqa: E402
from synth import build_document, load_unit_irs  # noqa: E402
from units import UNITS, Unit  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools" / "notes"
TEMPLATE = TOOLS / "templates" / "notes_template.html"
CSS_FILE = TOOLS / "assets" / "notes.css"
JS_FILE = TOOLS / "assets" / "notes.js"
MANIFEST = TOOLS / "notes_manifest.json"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def read_asset(path: Path) -> str:
    """Read an asset, stripping a UTF-8 BOM.

    Python's ``utf-8`` codec keeps U+FEFF as a real character. When a BOM'd file
    is inlined into ``<style>`` or ``<script>`` that character is emitted
    verbatim, which invalidates the very first CSS rule.
    """
    return path.read_text(encoding="utf-8-sig")


def wrap_section(section_id: str, title: str, body: str) -> str:
    return (
        f'<section class="section-card" id="{section_id}" aria-labelledby="{section_id}-h">'
        f'<h2 id="{section_id}-h">{html_mod.escape(title)}</h2>'
        f"{body}"
        f"</section>"
    )


def build_toc(entries: list[dict]) -> str:
    return "\n".join(
        f'      <a class="toc-link" href="#{e["id"]}">{html_mod.escape(e["title"])}</a>'
        for e in entries
    )


def build_meta(unit: Unit, irs: list[dict], sections: list[dict]) -> str:
    nb_count = len(irs)
    topics = sum(1 for ir in irs for _ in ir["blocks"])
    chips = [
        (DOC_SVG_DOC, f"{nb_count} source notebook{'s' if nb_count != 1 else ''}"),
        (DOC_SVG_TOPIC, f"{topics} topic sections extracted"),
        (DOC_SVG_SECTIONS, f"{len(sections)} study sections"),
    ]
    parts = []
    for icon, label in chips:
        parts.append(
            f'<span class="chip">{icon}<span>{html_mod.escape(label)}</span></span>'
        )
    return "\n          ".join(parts)


DOC_SVG_DOC = (
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>'
    '<polyline points="14 2 14 8 20 8"></polyline></svg>'
)
DOC_SVG_TOPIC = (
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M4 4h16M4 10h16M4 16h10M4 22h6"></path></svg>'
)
DOC_SVG_SECTIONS = (
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<rect x="3" y="3" width="18" height="18" rx="2"></rect>'
    '<path d="M9 3v18M3 9h18"></path></svg>'
)


def render_unit(unit: Unit) -> dict:
    irs = load_unit_irs(unit, ROOT)
    sections, toc_entries = build_document(unit, irs)

    css = read_asset(CSS_FILE)
    # Inject Pygments token rules for screen, then a light print override.
    screen_tokens = pygments_css("default", ".code-shell pre.tok")
    print_tokens = pygments_css("friendly", ".code-shell pre.tok")
    css = (
        css.replace("/* ---------- Accessibility ---------- */",
                    f"{screen_tokens}\n\n/* ---------- Accessibility ---------- */", 1)
    )
    css += (
        "\n\n@media print {\n"
        + "\n".join("  " + ln for ln in print_tokens.splitlines())
        + "\n}\n"
    )

    js = read_asset(JS_FILE)
    template = read_asset(TEMPLATE)

    content = "\n".join(
        wrap_section(s["id"], s["title"], s["html"]) for s in sections
    )

    out_html = (
        template.replace("{{ title }}", html_mod.escape(unit.title))
        .replace("{{ description }}", html_mod.escape(unit.lede))
        .replace("{{ css }}", css)
        .replace("{{ js }}", js)
        .replace("{{ toc }}", build_toc(toc_entries))
        .replace("{{ meta }}", build_meta(unit, irs, sections))
        .replace("{{ content }}", content)
    )

    out_dir = ROOT / unit.root / "Notes"
    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / f"{unit.out_stem}.html"
    html_path.write_text(out_html, encoding="utf-8")

    return {
        "unit": unit.key,
        "title": unit.title,
        "sources": [
            {"notebook": ir["notebook"], "sha256": ir["sha256"],
             "md_cells": ir["md_cells"], "code_cells": ir["code_cells"]}
            for ir in irs
        ],
        "topics_extracted": sum(len(ir["blocks"]) for ir in irs),
        "sections": [s["id"] for s in sections],
        "html": html_path.relative_to(ROOT).as_posix(),
        "html_bytes": html_path.stat().st_size,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--unit", help="build a single unit by key")
    parser.add_argument("--no-pdf", action="store_true")
    parser.add_argument(
        "--force-pdf",
        action="store_true",
        help="re-render every PDF even if it is newer than its HTML",
    )
    args = parser.parse_args()

    units = UNITS
    if args.unit:
        units = tuple(u for u in UNITS if u.key == args.unit)
        if not units:
            print(f"unknown unit: {args.unit}", file=sys.stderr)
            return 2

    manifest_entries = []
    if MANIFEST.exists():
        try:
            manifest_entries = json.loads(MANIFEST.read_text(encoding="utf-8")).get("units", [])
        except Exception:
            manifest_entries = []
    known = {e["unit"]: e for e in manifest_entries}

    for unit in sorted(units, key=lambda u: u.order):
        entry = render_unit(unit)
        known[unit.key] = entry
        print(f"[html] {unit.key:22} -> {entry['html']}  ({entry['html_bytes'] / 1024:.0f} KB)")

    if not args.no_pdf:
        try:
            from pdf import render_pdfs_for_manifest

            render_pdfs_for_manifest(list(known.values()), print, force=args.force_pdf)
        except ImportError:
            print("[pdf] pdf renderer unavailable, skipping", file=sys.stderr)

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "root": str(ROOT),
        "units": [known[u.key] for u in sorted(UNITS, key=lambda x: x.order) if u.key in known],
    }
    MANIFEST.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"[manifest] {MANIFEST.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())