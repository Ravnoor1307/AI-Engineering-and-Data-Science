"""Markdown and code rendering helpers for the notes builder."""
from __future__ import annotations

import html as html_mod
import re

import markdown2
from pygments import highlight as pygments_highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.util import ClassNotFound

MD_EXTRAS = [
    "fenced-code-blocks",
    "tables",
    "strike",
    "task_list",
    "sane_lists",
    "cuddled-lists",
    "header-ids",
    "target-blank-links",
    "wiki-tables",
]

# Notebook prose is rendered *inside* a section that already owns an <h2>.
# Any headings the author wrote inside a cell must therefore be demoted so the
# document outline stays valid and the sidebar TOC does not desynchronise.
HEADING_DEMOTE = 3
_HEADING_TAG_RE = re.compile(r"<h([1-6])(\s[^>]*)?>(.*?)</h\1>", re.DOTALL)


def _demote_headings(html: str) -> str:
    def repl(match: re.Match[str]) -> str:
        level = int(match.group(1))
        attrs = match.group(2) or ""
        new_level = min(level + HEADING_DEMOTE, 6)
        return f"<h{new_level}{attrs}>{match.group(3)}</h{new_level}>"

    return _HEADING_TAG_RE.sub(repl, html)

_SCREEN_STYLE = "default"
_PRINT_STYLE = "friendly"

_LANG_ALIASES = {
    "py": "python",
    "python3": "python",
    "ipython": "python",
    "sh": "bash",
    "shell": "bash",
    "zsh": "bash",
    "console": "bash",
    "js": "javascript",
    "ts": "typescript",
    "yml": "yaml",
    "md": "markdown",
    "ps1": "powershell",
    "postgresql": "sql",
    "postgres": "sql",
    "psql": "sql",
    "mysql": "sql",
    "sqlite": "sql",
}


def md(text: str) -> str:
    """Convert Markdown to HTML."""
    if not text or not text.strip():
        return ""
    html = markdown2.markdown(text, extras=MD_EXTRAS)
    html = _demote_headings(html)
    html = _localize_images(html)
    html = _repair_html(html)
    return _wrap_tables(_tidy_links(html))


# Elements that must never sit inside a <p>.
BLOCK_TAGS = {
    "ul", "ol", "table", "div", "pre", "blockquote", "section", "figure",
    "h1", "h2", "h3", "h4", "h5", "h6", "hr",
}

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

# Tags that may be implicitly closed to rescue an otherwise broken nest.
INLINE_TAGS = {
    "a", "b", "i", "em", "strong", "span", "code", "small", "sub", "sup",
    "u", "s", "abbr", "cite", "q", "mark", "kbd", "var", "time",
}

_TOKEN_RE = re.compile(r"<(/?)([a-zA-Z][\w-]*)((?:\"[^\"]*\"|'[^']*'|[^>])*?)(/?)>")
_HEADING_P_RE = re.compile(
    r"(<h[1-6][^>]*>)\s*<p>(.*?)</p>\s*(</h[1-6]>)", re.DOTALL
)


def _repair_html(html: str) -> str:
    """Normalise structurally invalid HTML produced from messy Markdown.

    Notebook prose regularly writes a list that continues a paragraph (a nested
    list followed by loose items). Markdown renders that as a <p> wrapped around
    <li>/<ul>, which is invalid HTML and corrupts the document outline that the
    sidebar TOC depends on.

    This is a real token pass rather than a chain of substitutions: it closes an
    open <p> before any block element, drops closing tags that were never
    opened, and closes anything still open at the end.
    """
    html = _HEADING_P_RE.sub(r"\1\2\3", html)

    out: list[str] = []
    stack: list[str] = []
    pos = 0

    for match in _TOKEN_RE.finditer(html):
        out.append(html[pos:match.start()])
        pos = match.end()

        closing, tag, self_closing = match.group(1), match.group(2).lower(), match.group(4)

        if tag in VOID_TAGS or self_closing:
            out.append(match.group(0))
            continue

        if not closing:
            if tag in BLOCK_TAGS and stack and stack[-1] == "p":
                out.append("</p>")
                stack.pop()
            stack.append(tag)
            out.append(match.group(0))
            continue

        if tag not in stack:
            # A closing tag with no opener: drop it.
            continue

        while stack and stack[-1] != tag:
            dropped = stack.pop()
            out.append(f"</{dropped}>")
        stack.pop()
        out.append(match.group(0))

    out.append(html[pos:])
    for leftover in reversed(stack):
        out.append(f"</{leftover}>")

    return "".join(out)


def _wrap_tables(html: str) -> str:
    def repl(match: re.Match[str]) -> str:
        return f'<div class="table-wrap">{match.group(0)}</div>'

    return re.sub(r"<table>.*?</table>", repl, html, flags=re.DOTALL | re.IGNORECASE)


def _tidy_links(html: str) -> str:
    # Drop the empty heading anchors markdown2 injects; we manage our own.
    html = re.sub(r'<h([1-6]) id="[^"]*"></h\1>', "", html)
    # Collapse heading ids we did not ask for, keeping text intact.
    html = re.sub(r'<h([2-4]) id="[^"]*">(.*?)</h\1>', r"<h\1>\2</h\1>", html, flags=re.DOTALL)
    return html


_IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
_IMG_SRC_RE = re.compile(r"""src\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
_IMG_ALT_RE = re.compile(r"""alt\s*=\s*["']([^"']*)["']""", re.IGNORECASE)


def _localize_images(html: str) -> str:
    """Strip remote images so a notes file stays fully self-contained.

    An ``<img>`` pointing at a third-party host breaks the "open the file and it
    just works" guarantee: the reader sees a broken frame with no diagram. The
    caption text (if any) is retained, and the callout tells the reader where
    the original lives.
    """
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        src_match = _IMG_SRC_RE.search(tag)
        if not src_match:
            return ""
        src = src_match.group(1)
        if not re.match(r"^(https?:)?//", src, re.IGNORECASE):
            return tag

        alt_match = _IMG_ALT_RE.search(tag)
        alt = alt_match.group(1).strip() if alt_match else ""
        label = alt or "Source diagram"
        return (
            f'<p class="external-figure"><span class="external-figure-label">'
            f"{html_mod.escape(label)}</span> "
            f'<a href="{html_mod.escape(src)}" target="_blank" rel="noopener">'
            f"open the original figure</a></p>"
        )

    return _IMG_RE.sub(repl, html)


def normalize_lang(lang: str | None) -> str:
    if not lang:
        return "text"
    key = lang.strip().lower().split()[0]
    return _LANG_ALIASES.get(key, key)


def highlight_code(code: str, lang: str | None) -> str:
    """Syntax-highlight code with both a screen and a print CSS scope."""
    language = normalize_lang(lang)
    if language in {"text", "plaintext", ""}:
        lexer = guess_lexer(code)
    else:
        try:
            lexer = get_lexer_by_name(language)
        except ClassNotFound:
            lexer = guess_lexer(code)
    formatter = HtmlFormatter(nowrap=True, cssclass="tok")
    return pygments_highlight(code, lexer, formatter)


def pygments_css(style_name: str, scope: str) -> str:
    """Return Pygments token CSS rewritten under a scope selector."""
    css = HtmlFormatter(style=style_name).get_style_defs(".tok")
    lines = []
    for line in css.splitlines():
        stripped = line.strip()
        if stripped.startswith("@"):
            lines.append("  " + line)
            continue
        m = re.match(r"^(\.[\w\-\.]+)", line)
        if m:
            lines.append(f"{scope} {line}")
        else:
            lines.append(line)
    return "\n".join(lines)


def code_shell(code: str, lang: str | None = None, caption: str | None = None) -> str:
    language = normalize_lang(lang)
    body = highlight_code(code, language)
    label = html_mod.escape(language if language != "text" else "code")
    cap_html = ""
    if caption:
        cap_html = f'<div class="code-caption">{html_mod.escape(caption)}</div>'
    return (
        f'<div class="code-shell">'
        f'<div class="code-toolbar">'
        f'<span class="code-lang">{label}</span>'
        f'<button class="copy-code" type="button" aria-label="Copy code">'
        f'<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f'<rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>'
        f'<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>'
        f"</svg><span>Copy</span></button>"
        f"</div>"
        f"{cap_html}"
        f'<pre class="tok"><code class="tok">{body}</code></pre>'
        f"</div>"
    )


def callout(kind: str, title: str, body_html: str, icon: str | None = None) -> str:
    icon_svg = icon or CALLOUT_ICONS.get(kind, CALLOUT_ICONS["info"])
    return (
        f'<aside class="callout callout-{kind}">'
        f'<span class="callout-icon">{icon_svg}</span>'
        f'<p class="callout-title">{html_mod.escape(title)}</p>'
        f"{body_html}"
        f"</aside>"
    )


CALLOUT_ICONS = {
    "info": (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
        '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line>'
        '<line x1="12" y1="8" x2="12.01" y2="8"></line></svg>'
    ),
    "important": (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
        '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>'
        '<path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>'
    ),
    "tip": (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="true" aria-hidden="true">'
        '<path d="M9 18h6"></path><path d="M10 22h4"></path>'
        '<path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"></path></svg>'
    ),
    "warning": (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>'
        '<line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'
    ),
    "danger": (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line>'
        '<line x1="9" y1="9" x2="15" y2="15"></line></svg>'
    ),
    "hinglish": (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>'
    ),
    "ai": (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<rect x="7" y="7" width="10" height="10" rx="2" ry="2"></rect>'
        '<path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1'
        'M19.1 4.9 17 7M7 17l-2.1 2.1"></path></svg>'
    ),
}

SVG_COPY = (
    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>'
    '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>'
)

SVG_INFO_CIRCLE = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
    '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line>'
    '<line x1="12" y1="8" x2="12.01" y2="8"></line></svg>'
)


def diagram_flow(nodes: list[str], title: str | None = None) -> str:
    """Render a horizontal flow diagram."""
    parts = []
    for i, node in enumerate(nodes):
        if i:
            parts.append(
                '<span class="flow-arrow" aria-hidden="true">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
                '<line x1="5" y1="12" x2="19" y2="12"></line>'
                '<polyline points="12 5 19 12 12 19"></polyline></svg></span>'
            )
        parts.append(f'<span class="flow-node">{html_mod.escape(node)}</span>')
    cap = f'<div class="diagram-title">{html_mod.escape(title)}</div>' if title else ""
    return f'<div class="diagram">{cap}<div class="flow">{"".join(parts)}</div></div>'