"""Bridge to the Node/Playwright PDF renderer with a Chrome-CLI fallback."""
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RENDER_MJS = HERE / "render_pdf.mjs"

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
]


def find_chrome() -> str | None:
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    for name in ("chrome", "msedge", "chromium", "google-chrome", "chromium-browser"):
        found = shutil.which(name)
        if found:
            return found
    return None


def cli_render(chrome: str, html_path: Path, pdf_path: Path) -> bool:
    """Fallback path: plain --print-to-pdf, without the page-number template."""
    profile = tempfile.mkdtemp(prefix="notes-pdf-")
    try:
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-first-run",
            "--disable-extensions",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=25000",
            "--no-pdf-header-footer",
            f"--user-data-dir={profile}",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ]
        subprocess.run(cmd, capture_output=True, timeout=300)
        return pdf_path.exists() and pdf_path.stat().st_size > 0
    except Exception:
        return False
    finally:
        shutil.rmtree(profile, ignore_errors=True)


def playwright_render(html_path: Path, pdf_path: Path, unit_title: str) -> tuple[bool, str | None]:
    if not RENDER_MJS.exists():
        return False, "render_pdf.mjs missing"
    try:
        proc = subprocess.run(
            ["node", str(RENDER_MJS), str(html_path), str(pdf_path), unit_title],
            capture_output=True,
            timeout=420,
            cwd=str(ROOT),
        )
    except subprocess.TimeoutExpired:
        return False, "node renderer timed out"
    except FileNotFoundError:
        return False, "node not found"

    out = proc.stdout.decode("utf-8", "replace").strip()
    try:
        payload = json.loads(out.splitlines()[-1])
    except Exception:
        return False, f"renderer output unparsable: {out[:200] or proc.stderr.decode('utf-8', 'replace')[:200]}"

    if payload.get("ok") and pdf_path.exists() and pdf_path.stat().st_size > 0:
        return True, None
    return False, payload.get("error") or "renderer reported failure"


def render_pdf(html_path: Path, pdf_path: Path, unit_title: str) -> dict:
    """Render one HTML file to PDF, preferring the header/footer-capable path."""
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    ok, err = playwright_render(html_path, pdf_path, unit_title)
    if ok:
        return {"ok": True, "renderer": "playwright", "bytes": pdf_path.stat().st_size}

    chrome = find_chrome()
    if chrome and cli_render(chrome, html_path, pdf_path):
        return {"ok": True, "renderer": "cli", "bytes": pdf_path.stat().st_size}

    return {"ok": False, "reason": err or "no renderer available"}


def _page_count(data: bytes) -> int | None:
    import re

    counts = [int(m) for m in re.findall(rb"/Type\s*/Pages[^>]*?/Count\s+(\d+)", data)]
    if counts:
        return max(counts)
    found = re.findall(rb"/Type\s*/Page[^s]", data)
    return len(found) if found else None


def validate_pdf(path: Path) -> dict:
    """A real PDF starts with %PDF- and is not a renamed HTML file."""
    if not path.exists():
        return {"valid": False, "reason": "missing"}
    data = path.read_bytes()
    if len(data) < 1000:
        return {"valid": False, "reason": f"suspiciously small ({len(data)} bytes)"}
    if not data.startswith(b"%PDF-"):
        head = data[:200].decode("utf-8", "replace").lower()
        return {"valid": False, "reason": f"no %PDF- header (starts with: {head[:60]!r})"}
    if b"%%EOF" not in data[-2048:]:
        return {"valid": False, "reason": "missing %%EOF trailer"}
    return {"valid": True, "bytes": len(data), "pages": _page_count(data)}


def render_pdfs_for_manifest(entries: list[dict], log=print, force: bool = False) -> None:
    """Render a PDF for each manifest entry that has HTML but no current PDF.

    A cached PDF is only reused when it is newer than the HTML it came from,
    otherwise a rebuilt document would silently keep its previous rendering.
    """
    for entry in entries:
        html_rel = entry.get("html")
        if not html_rel:
            continue
        html_path = ROOT / html_rel
        pdf_path = html_path.with_suffix(".pdf")

        html_mtime = html_path.stat().st_mtime
        stale = force or not pdf_path.exists() or pdf_path.stat().st_mtime < html_mtime

        if not stale:
            existing = validate_pdf(pdf_path)
            if existing.get("valid"):
                entry["pdf"] = pdf_path.relative_to(ROOT).as_posix()
                entry["pdf_bytes"] = existing["bytes"]
                entry["pdf_pages"] = existing.get("pages")
                entry["pdf_renderer"] = "cached"
                entry["pdf_valid"] = True
                log(f"[pdf =] {entry['unit']:24} {entry['pdf']} "
                    f"({existing['bytes'] / 1024:.0f} KB, {existing.get('pages')}p, cached)")
                continue

        result = render_pdf(html_path, pdf_path, entry.get("title", ""))
        if result.get("ok"):
            check = validate_pdf(pdf_path)
            entry["pdf"] = pdf_path.relative_to(ROOT).as_posix()
            entry["pdf_bytes"] = pdf_path.stat().st_size
            entry["pdf_pages"] = check.get("pages")
            entry["pdf_renderer"] = result.get("renderer")
            entry["pdf_valid"] = check.get("valid", False)
            if not check.get("valid"):
                entry["pdf_error"] = check.get("reason")
            log(f"[pdf ] {entry['unit']:24} {entry['pdf']} "
                f"({entry['pdf_bytes'] / 1024:.0f} KB, {check.get('pages')}p, {result.get('renderer')})")
        else:
            entry["pdf_error"] = result.get("reason")
            log(f"[FAIL] {entry['unit']:24} {result.get('reason')}")


if __name__ == "__main__":
    import sys

    target = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else "-"
    p = ROOT / target
    out = p.with_suffix(".pdf")
    res = render_pdf(p, out, title)
    res["validate"] = validate_pdf(out)
    print(json.dumps(res, indent=2))