"""Read-only inventory of notebooks grouped by meaningful unit."""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SKIP_DIR_PARTS = {".ipynb_checkpoints", ".virtual_documents", ".git", "tools"}

PRACTICE_PATTERNS = re.compile(
    r"(practice|solution|task|assignment|exercise|challenge|interview|"
    r"question|homework|project_?brief|revision_?test|mock)",
    re.IGNORECASE,
)

CASE_STUDY_PATTERNS = re.compile(r"(case_?study|project)", re.IGNORECASE)


def is_skipped(path: Path) -> bool:
    return any(part in SKIP_DIR_PARTS for part in path.parts)


def load_nb(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:  # pragma: no cover - inventory resilience
        return {"_error": str(exc), "cells": []}


def summarize(path: Path) -> dict:
    nb = load_nb(path)
    cells = nb.get("cells", [])
    md_cells = [c for c in cells if c.get("cell_type") == "markdown"]
    code_cells = [c for c in cells if c.get("cell_type") == "code"]

    headings: list[str] = []
    md_chars = 0
    for cell in md_cells:
        src = "".join(cell.get("source", []))
        md_chars += len(src)
        for line in src.splitlines():
            m = re.match(r"^(#{1,3})\s+(.*\S)\s*$", line)
            if m:
                headings.append(f"{'#' * len(m.group(1))} {m.group(2)}")

    code_lines = sum(
        len("".join(c.get("source", [])).strip().splitlines())
        for c in code_cells
    )

    rel = path.relative_to(ROOT).as_posix()
    return {
        "rel": rel,
        "name": path.stem,
        "md_cells": len(md_cells),
        "code_cells": len(code_cells),
        "md_chars": md_chars,
        "code_lines": code_lines,
        "headings": headings,
        "practice": bool(PRACTICE_PATTERNS.search(path.stem)),
        "case_study": bool(CASE_STUDY_PATTERNS.search(path.stem)),
        "error": nb.get("_error"),
    }


def unit_key(path: Path) -> str:
    """Deepest directory that groups theory notebooks into one unit."""
    return path.parent.relative_to(ROOT).as_posix()


def main() -> None:
    out_path = Path(os.environ.get("NOTES_INVENTORY_OUT", "")) if os.environ.get(
        "NOTES_INVENTORY_OUT"
    ) else None
    real_stdout = sys.stdout
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        sys.stdout = out_path.open("w", encoding="utf-8")
    try:
        _run(real_stdout)
    finally:
        if out_path:
            sys.stdout.close()
        sys.stdout = real_stdout


def _run(_real_stdout) -> None:
    notebooks = sorted(
        p
        for p in ROOT.rglob("*.ipynb")
        if not is_skipped(p.relative_to(ROOT))
    )

    groups: dict[str, list[dict]] = defaultdict(list)
    for nb in notebooks:
        groups[unit_key(nb)].append(summarize(nb))

    total_cells = 0
    for unit in sorted(groups):
        entries = groups[unit]
        theory = [e for e in entries if not e["practice"]]
        practice = [e for e in entries if e["practice"]]
        total_cells += sum(e["md_cells"] + e["code_cells"] for e in entries)

        print("=" * 78)
        print(f"UNIT  {unit}")
        print(
            f"      theory={len(theory)}  practice={len(practice)}  "
            f"md_cells={sum(e['md_cells'] for e in entries)}  "
            f"code_cells={sum(e['code_cells'] for e in entries)}  "
            f"code_lines={sum(e['code_lines'] for e in entries)}"
        )
        for entry in entries:
            flags = []
            if entry["practice"]:
                flags.append("PRACTICE")
            if entry["case_study"]:
                flags.append("CASE-STUDY")
            if entry["error"]:
                flags.append(f"ERROR:{entry['error']}")
            tag = " [" + ", ".join(flags) + "]" if flags else ""
            print(
                f"   - {entry['name']}.ipynb  "
                f"(md={entry['md_cells']}, code={entry['code_cells']}, "
                f"lines={entry['code_lines']}){tag}"
            )
            for heading in entry["headings"][:12]:
                print(f"         {heading}")
            if len(entry["headings"]) > 12:
                print(f"         ... +{len(entry['headings']) - 12} more headings")

    print("=" * 78)
    print(f"TOTAL notebooks: {len(notebooks)}")
    print(f"TOTAL units:     {len(groups)}")
    print(f"TOTAL cells:     {total_cells}")


if __name__ == "__main__":
    main()