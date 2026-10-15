#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
generate_html_notes.py — scans every sub-folder for .ipynb → ONE 3D animated HTML.
USAGE:  python generate_html_notes.py [root] --theme neon --max-image-kb 600
"""
import argparse, json, re, sys
from datetime import datetime
from pathlib import Path

try:
    import markdown as _md
except ImportError:
    _md = None
try:
    from pygments import highlight as _pyg
    from pygments.lexers import get_lexer_by_name, PythonLexer
    from pygments.formatters import HtmlFormatter
    _PYG_FMT = HtmlFormatter(style="monokai")
    PYG_CSS = _PYG_FMT.get_style_defs(".highlight")
    HAS_PYG = True
except ImportError:
    HAS_PYG = False; PYG_CSS = ""

SKIP_DIRS = {".ipynb_checkpoints", ".git", "__pycache__", ".venv", "venv", "env",
             "node_modules", ".pytest_cache", ".mypy_cache", "dist", "build",
             ".virtual_documents"}
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")
H_RE = re.compile(r"<h([1-6])((?:\s[^>]*)?)>(.*?)</h\1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")

THEMES = {
    "neon":   dict(a="#00e5ff", a2="#a78bfa", a3="#ff4d94", ar="0,229,255",  a2r="167,139,250", a3r="255,77,148",  bg="#060913"),
    "ocean":  dict(a="#22d3ee", a2="#34d399", a3="#f472b6", ar="34,211,238",  a2r="52,211,153",  a3r="244,114,182", bg="#071018"),
    "sunset": dict(a="#fb923c", a2="#f43f5e", a3="#facc15", ar="251,146,60",  a2r="244,63,94",   a3r="250,204,21",  bg="#120a14"),
    "royal":  dict(a="#818cf8", a2="#c084fc", a3="#38bdf8", ar="129,140,248", a2r="192,132,252", a3r="56,189,248",  bg="#0a0a1a"),
}
def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def natkey(s): return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]
def prettify(n): return re.sub(r"[-_]+"," ",n).strip().title()

def collect_notebooks(root: Path):
    found = [p for p in root.rglob("*.ipynb")
             if not any(x in SKIP_DIRS for x in p.parts)
             and not p.name.endswith("-checkpoint.ipynb")]
    found.sort(key=lambda p:(natkey(str(p.parent.relative_to(root)).lower()), natkey(p.name.lower())))
    return found

def group_by_folder(root, nbs):
    g, order = {}, []
    for p in nbs:
        k = str(p.parent.relative_to(root))
        if k not in g: g[k] = []; order.append(k)
        g[k].append(p)
    return [(k, g[k]) for k in order]

_NB_CACHE = {}
def load_cells(nb_path: Path):
    key = str(nb_path.resolve())
    if key in _NB_CACHE: return _NB_CACHE[key]
    try:
        nb = json.loads(nb_path.read_text(encoding="utf-8-sig"))
    except Exception as e:
        print("      !! skipped (%s)" % e.__class__.__name__)
        _NB_CACHE[key] = ([], {}, "python"); return _NB_CACHE[key]
    cells = nb.get("cells")
    if not cells and "worksheets" in nb:
        cells = nb["worksheets"][0].get("cells", [])
    meta = nb.get("metadata", {})
    lang = (meta.get("kernelspec", {}).get("language")
            or meta.get("language_info", {}).get("name") or "python")
    _NB_CACHE[key] = (cells or [], meta, lang)
    return _NB_CACHE[key]

def src_of(c):
    s = c.get("source",""); return "".join(s) if isinstance(s,list) else (s or "")

def parse_output(o):
    t = o.get("output_type")
    j = lambda v: "".join(v) if isinstance(v,list) else (v or "")
    if t == "stream":
        return {"kind":"text","text":ANSI_RE.sub("",j(o.get("text")))}
    if t in ("execute_result","display_data"):
        d = o.get("data",{})
        for m,k in (("image/png","image"),("image/jpeg","image"),("image/svg+xml","svg"),
                    ("text/html","html"),("text/plain","text")):
            if m in d: return {"kind":k,"mime":m,"text":ANSI_RE.sub("",j(d[m]))}
    if t == "error":
        return {"kind":"error","text":ANSI_RE.sub("","\n".join(o.get("traceback",[])))}
    return None

MAX_LEVEL, MD_ENGINE, MAX_IMG_B64, TRUNC = 2, None, 0, 14

def code_html(code, lang):
    if HAS_PYG:
        try: return _pyg(code, get_lexer_by_name(lang, stripnl=False), _PYG_FMT)
        except Exception: pass
    return "<pre class='fallback'><code>%s</code></pre>" % esc(code)

def md_html(src, cell):
    for f, att in (cell.get("attachments") or {}).items():
        for m, b in att.items():
            src = src.replace("attachment:%s"%f, "data:%s;base64,%s"%(m,re.sub(r"\s","",b)))
    if MD_ENGINE:
        MD_ENGINE.reset(); return MD_ENGINE.convert(src)
    return "<pre>%s</pre>" % esc(src)

def inject_ids(html, pre):
    ent, n = [], [0]
    def r(m):
        n[0]+=1; hid="%s-s%d"%(pre,n[0])
        ent.append({"level":int(m.group(1)),"id":hid,"text":TAG_RE.sub("",m.group(3)).strip()})
        return '<h%s id="%s"%s>%s</h%s>'%(m.group(1),hid,m.group(2),m.group(3),m.group(1))
    return H_RE.sub(r,html), ent

def render_cells(cells, lang, idx, stats):
    parts, toc = [], []
    for i,c in enumerate(cells):
        ct = c.get("cell_type")
        if ct == "raw": continue
        src = src_of(c)
        if ct == "markdown":
            stats["md"]+=1; stats["words"]+=len(re.findall(r"\w+",src))
            body, heads = inject_ids(md_html(src,c), "n%d"%idx)
            toc += [h for h in heads if h["level"]<=MAX_LEVEL]
            parts.append("<section class='cell reveal' id='n%d-c%d'>"
                "<div class='cell-chip'>&#128221; Note &middot; %d</div>"
                "<div class='md-body'>%s</div></section>"%(idx,i,i,body))
        elif ct == "code":
            stats["code"]+=1; stats["loc"]+=len([l for l in src.splitlines() if l.strip()])
            outs=[]
            for o in (c.get("outputs") or []):
                po = parse_output(o)
                if not po: continue
                if po["kind"]=="image":
                    b64 = re.sub(r"\s","",po["text"])
                    if MAX_IMG_B64 and len(b64)>MAX_IMG_B64:
                        outs.append("<div class='output-card reveal'><span class='out-label'>"
                            "&#128228; Image skipped (%.1f MB)</span></div>"%(len(b64)*.75/1e6)); continue
                    stats["images"]+=1
                    outs.append("<div class='output-card reveal'><span class='out-label'>"
                        "&#128228; Output &middot; Image</span><div class='output-body'>"
                        "<img class='out-img' src='data:%s;base64,%s'></div></div>"%(po["mime"],b64))
                elif po["kind"]=="svg":
                    stats["images"]+=1
                    outs.append("<div class='output-card reveal'><span class='out-label'>"
                        "&#128228; Output &middot; SVG</span><div class='output-body'>%s</div></div>"%po["text"])
                elif po["kind"]=="html":
                    outs.append("<div class='output-card reveal'><span class='out-label'>"
                        "&#128228; Output &middot; Rich</span><div class='output-body'>%s</div></div>"%po["text"])
                else:
                    err = po["kind"]=="error"; lines = po["text"].splitlines()
                    long_cls, tog = ("","")
                    if len(lines)>TRUNC:
                        long_cls=" long"; tog="<button class='out-toggle'>Show more &#9662;</button>"
                    outs.append("<div class='output-card reveal%s'><span class='out-label'>%s</span>"
                        "<div class='output-body%s'><pre>%s</pre></div>%s</div>"
                        %(" error" if err else "", "&#9888;&#65039; Error" if err else "&#128228; Output",
                          long_cls, esc(po["text"]), tog))
            parts.append("<section class='cell reveal' id='n%d-c%d'>"
                "<div class='cell-chip'>&#128187; Code &middot; %d</div>"
                "<div class='code-card tilt'><div class='code-head'><span class='dot r'></span>"
                "<span class='dot y'></span><span class='dot g'></span>"
                "<span class='lang'>%s</span></div>%s</div>%s</section>"
                %(idx,i,i,esc(lang),code_html(src,lang),"".join(outs)))
    return "".join(parts), toc

def nb_title(meta, cells, path):
    if meta.get("title"): return str(meta["title"])
    for c in cells:
        if c.get("cell_type")=="markdown":
            m = re.search(r"^#\s+(.+)$", src_of(c), re.M)
            if m: return m.group(1).strip().strip("#").strip()
    return prettify(path.stem)

def render_notebook(idx, path, root, stats):
    cells, meta, lang = load_cells(path)
    title = nb_title(meta, cells, path)
    body, toc = render_cells(cells, lang, idx, stats)
    head = ("<div class='nb-head'><span class='chip'>&#128209; Notebook %d</span><h2>%s</h2>"
            "<div class='path'>%s</div></div>"%(idx+1, esc(title), esc(path.relative_to(root))))
    return {"idx":idx,"title":title,
            "html":"<section class='nb' id='nb-%d'>%s%s</section>"%(idx,head,body),
            "toc":[{"level":1,"id":"nb-%d"%idx,"text":title}]+toc}

ROOT_T = (":root{--a:%(a)s;--a2:%(a2)s;--a3:%(a3)s;--ar:%(ar)s;--a2r:%(a2r)s;--a3r:%(a3r)s;"
          "--bg:%(bg)s;--card:rgba(255,255,255,.045);--bd:rgba(255,255,255,.10);"
          "--tx:#e8ecf4;--mut:#93a1b8;--code:#0b0f1a;--r:16px;"
          "--fb:'Poppins',system-ui,sans-serif;--fc:'Fira Code',ui-monospace,Consolas,monospace;"
          "--fd:'Orbitron','Poppins',sans-serif}")

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{font-family:var(--fb);background:var(--bg);color:var(--tx);line-height:1.7;overflow-x:hidden}
::selection{background:rgba(var(--ar),.35)}
::-webkit-scrollbar{width:10px}::-webkit-scrollbar-thumb{border-radius:6px;
background:linear-gradient(var(--a),var(--a2));border:2px solid var(--bg)}
body::before{content:'';position:fixed;inset:0;z-index:-3;
background:radial-gradient(55vw 55vw at 12% 18%,rgba(var(--ar),.13),transparent 60%),
radial-gradient(45vw 45vw at 88% 28%,rgba(var(--a2r),.13),transparent 60%),
radial-gradient(55vw 55vw at 50% 95%,rgba(var(--a3r),.11),transparent 60%),var(--bg);
animation:mesh 16s ease-in-out infinite alternate}
@keyframes mesh{to{filter:hue-rotate(28deg) saturate(1.25)}}
body::after{content:'';position:fixed;inset:0;z-index:-2;
background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),
linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:46px 46px;
-webkit-mask-image:radial-gradient(ellipse at 50% 30%,#000 25%,transparent 75%);
animation:gridMove 26s linear infinite}
@keyframes gridMove{to{background-position:46px 46px}}
.nav{position:fixed;inset:0 0 auto 0;height:52px;z-index:100;display:flex;align-items:center;
background:rgba(6,9,19,.78);backdrop-filter:blur(14px);border-bottom:1px solid var(--bd)}
.nav-in{width:min(1300px,94%);margin:auto;display:flex;align-items:center;gap:1.4rem}
.logo{font-family:var(--fd);font-weight:700;font-size:.95rem;letter-spacing:.08em;
background:linear-gradient(90deg,var(--a),var(--a2),var(--a3));-webkit-background-clip:text;
background-clip:text;color:transparent;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:55%}
.nav a.nl{margin-left:auto;color:var(--mut);text-decoration:none;font-size:.85rem;padding:.35rem .8rem;
border-radius:10px;border:1px solid transparent;transition:.3s}
.nav a.nl:hover{color:var(--tx);border-color:var(--bd);transform:translateY(-2px);
box-shadow:0 6px 16px -8px rgba(var(--ar),.5)}
.prog{position:absolute;bottom:-1px;left:0;height:3px;width:0%;
background:linear-gradient(90deg,var(--a),var(--a2),var(--a3));
box-shadow:0 0 14px rgba(var(--ar),.9);transition:width .1s linear}
.hero{position:relative;text-align:center;padding:126px 5% 54px;overflow:hidden}
.orb{position:absolute;border-radius:50%;filter:blur(46px);opacity:.5;pointer-events:none;
animation:orbF 12s ease-in-out infinite}
.orb.o1{width:340px;height:340px;background:rgba(var(--ar),.35);top:-60px;left:8%}
.orb.o2{width:280px;height:280px;background:rgba(var(--a2r),.35);top:8%;right:10%;animation-delay:-4s}
.orb.o3{width:240px;height:240px;background:rgba(var(--a3r),.3);bottom:-40px;left:45%;animation-delay:-8s}
@keyframes orbF{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(30px,-26px) scale(1.08)}
66%{transform:translate(-24px,18px) scale(.94)}}
.cube-scene{width:128px;height:128px;margin:0 auto 30px;perspective:900px}
.cube{width:100%;height:100%;position:relative;transform-style:preserve-3d;animation:spin 14s linear infinite}
.cube .face{position:absolute;inset:0;display:grid;place-items:center;font-size:2.1rem;
background:linear-gradient(135deg,rgba(var(--ar),.16),rgba(var(--a2r),.16));
border:1px solid rgba(var(--ar),.45);border-radius:10px;
box-shadow:inset 0 0 34px rgba(var(--ar),.22);text-shadow:0 0 16px rgba(var(--ar),.9)}
.f1{transform:rotateY(0) translateZ(64px)}.f2{transform:rotateY(90deg) translateZ(64px)}
.f3{transform:rotateY(180deg) translateZ(64px)}.f4{transform:rotateY(-90deg) translateZ(64px)}
.f5{transform:rotateX(90deg) translateZ(64px)}.f6{transform:rotateX(-90deg) translateZ(64px)}
@keyframes spin{from{transform:rotateX(-22deg) rotateY(0)}to{transform:rotateX(-22deg) rotateY(360deg)}}
.hero-t{font-family:var(--fd);font-weight:800;font-size:clamp(2rem,5.2vw,3.4rem);line-height:1.15;
background:linear-gradient(90deg,var(--a),var(--a2),var(--a3),var(--a));background-size:300% 100%;
-webkit-background-clip:text;background-clip:text;color:transparent;
animation:floatY 5s ease-in-out infinite,shine 6s linear infinite}
@keyframes floatY{0%,100%{transform:translateY(0) rotateX(0)}50%{transform:translateY(-10px) rotateX(4deg)}}
@keyframes shine{to{background-position:300% 0}}
.hero-s{color:var(--mut);margin-top:.8rem}
.badges{display:flex;gap:.7rem;justify-content:center;flex-wrap:wrap;margin-top:1.3rem}
.badge{padding:.4rem 1rem;border-radius:999px;font-size:.78rem;background:var(--card);
border:1px solid var(--bd);animation:floatY 4s ease-in-out infinite;transition:.3s}
.badge:hover{transform:scale(1.08) rotateX(10deg)}
.badge:nth-child(2){animation-delay:-1.3s}.badge:nth-child(3){animation-delay:-2.6s}.badge b{color:var(--a)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(125px,1fr));gap:1rem;
max-width:900px;margin:2.2rem auto 0}
.stat{padding:1.05rem .6rem;text-align:center;border-radius:14px;background:var(--card);
border:1px solid var(--bd);transition:.4s cubic-bezier(.2,.8,.2,1)}
.stat:hover{transform:rotateX(10deg) translateZ(14px);
box-shadow:0 18px 34px -14px rgba(0,0,0,.6),0 0 24px -8px rgba(var(--ar),.5)}
.stat .n{font-family:var(--fd);font-size:1.6rem;color:var(--a);text-shadow:0 0 18px rgba(var(--ar),.65)}
.stat .l{font-size:.66rem;letter-spacing:.18em;color:var(--mut);text-transform:uppercase;margin-top:.3rem}
.cue{display:inline-block;margin-top:2.2rem;color:var(--a);text-decoration:none;font-size:1.4rem;
animation:cueB 1.8s ease-in-out infinite;filter:drop-shadow(0 0 10px rgba(var(--ar),.8))}
@keyframes cueB{0%,100%{transform:translateY(0)}50%{transform:translateY(10px)}}
.layout{display:grid;grid-template-columns:280px minmax(0,1fr);gap:2.2rem;width:min(1300px,94%);
margin:auto;padding:1.6rem 0 4rem}
.toc{position:sticky;top:72px;align-self:start;max-height:calc(100vh - 96px);overflow:auto;
padding:1.1rem;border-radius:var(--r);background:var(--card);border:1px solid var(--bd)}
.toc h3{font-family:var(--fd);font-size:.85rem;letter-spacing:.2em;color:var(--a);margin-bottom:.8rem}
.toc details{margin-bottom:.55rem;border-radius:10px}
.toc details[open]{border:1px solid rgba(var(--ar),.22);background:rgba(var(--ar),.04)}
.toc summary{display:flex;align-items:center;gap:.45rem;cursor:pointer;list-style:none;
padding:.45rem .6rem;border-radius:9px;font-size:.74rem;font-weight:700;letter-spacing:.08em;
color:var(--a2);text-transform:uppercase;user-select:none;transition:.25s}
.toc summary::-webkit-details-marker{display:none}
.toc summary:hover{background:rgba(var(--a2r),.1);transform:translateX(4px)}
.toc summary small{margin-left:auto;color:var(--mut);font-weight:400}
.toc summary::before{content:'\25B8';transition:.25s;color:var(--mut)}
.toc details[open] summary::before{transform:rotate(90deg)}
.toc .tg-body{padding:.15rem .35rem .45rem}
.toc a{display:block;padding:.4rem .7rem;margin:.12rem 0;border-radius:9px;color:var(--mut);
text-decoration:none;font-size:.84rem;border-left:2px solid transparent;transition:.3s}
.toc a:hover{color:var(--tx);background:rgba(var(--ar),.09);transform:translateX(6px) rotateY(8deg);
border-left-color:var(--a);box-shadow:-5px 5px 0 rgba(var(--ar),.14)}
.toc a.on{color:var(--a);border-left-color:var(--a);background:rgba(var(--ar),.07)}
.toc a.lv2{padding-left:1.4rem;font-size:.78rem}
.folder-band{display:flex;align-items:center;gap:.9rem;margin:3rem 0 .4rem;padding:1rem 1.3rem;
border-radius:var(--r);font-family:var(--fd);letter-spacing:.06em;font-size:1.02rem;
background:linear-gradient(90deg,rgba(var(--ar),.13),rgba(var(--a2r),.08));
border:1px solid rgba(var(--ar),.28);box-shadow:0 10px 30px -16px rgba(var(--ar),.5)}
.folder-band .cnt{margin-left:auto;font-family:var(--fb);font-size:.68rem;color:var(--mut);letter-spacing:.2em}
.nb{margin:2.4rem 0 2.8rem;scroll-margin-top:90px}
.nb-head{display:flex;flex-wrap:wrap;gap:.5rem 1rem;align-items:baseline;margin:0 0 1.1rem;
padding-bottom:.75rem;border-bottom:1px dashed var(--bd)}
.nb-head .chip{font-size:.62rem;letter-spacing:.18em;color:var(--a2);text-transform:uppercase;
border:1px solid rgba(var(--a2r),.4);padding:.22rem .7rem;border-radius:999px;background:rgba(var(--a2r),.08)}
.nb-head h2{font-family:var(--fd);font-size:1.3rem;background:linear-gradient(90deg,var(--a),var(--a2));
-webkit-background-clip:text;background-clip:text;color:transparent}
.nb-head .path{color:var(--mut);font-size:.72rem;font-family:var(--fc);word-break:break-all}
.cell{margin-bottom:1.5rem;scroll-margin-top:80px}
.cell-chip{display:inline-flex;align-items:center;gap:.45rem;margin-bottom:.55rem;padding:.28rem .8rem;
border-radius:999px;font-size:.64rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;
color:var(--a);background:rgba(var(--ar),.09);border:1px solid rgba(var(--ar),.35);
box-shadow:3px 3px 0 rgba(var(--ar),.15);transition:.3s}
.cell-chip:hover{transform:translateY(-3px) rotateZ(-1deg)}
.md-body{padding:1.1rem 1.35rem;border-radius:var(--r);background:var(--card);
border:1px solid var(--bd);backdrop-filter:blur(8px)}
.md-body h1{font-family:var(--fd);font-size:1.7rem;margin:1.3rem 0 .85rem;
background:linear-gradient(90deg,var(--a),var(--a2));-webkit-background-clip:text;
background-clip:text;color:transparent}
.md-body h2{font-family:var(--fd);font-size:1.35rem;margin:1.25rem 0 .7rem;position:relative;padding-bottom:.4rem}
.md-body h2::after{content:'';position:absolute;left:0;bottom:0;width:68px;height:3px;border-radius:2px;
background:linear-gradient(90deg,var(--a),var(--a2));box-shadow:0 0 16px rgba(var(--ar),.75)}
.md-body h3{font-size:1.1rem;margin:1.05rem 0 .5rem;color:var(--a)}
.md-body h4{font-size:.96rem;margin:1rem 0 .45rem;color:var(--a2)}
.md-body p{margin:.55rem 0}.md-body a{color:var(--a);text-decoration:none}
.md-body ul,.md-body ol{margin:.55rem 0 .55rem 1.35rem}
.md-body li{margin:.28rem 0}.md-body li::marker{color:var(--a)}
.md-body code{font-family:var(--fc);font-size:.82em;padding:.13em .48em;border-radius:7px;color:var(--a);
background:rgba(var(--ar),.1);border:1px solid rgba(var(--ar),.25)}
.md-body pre{background:var(--code);color:#d6e2f0;border-radius:12px;padding:12px 14px;overflow:auto;
font-family:var(--fc);font-size:.8rem;line-height:1.55;margin:.6rem 0}
.md-body pre code{background:none;border:none;color:inherit;padding:0}
.md-body blockquote{margin:.85rem 0;padding:.8rem 1.1rem;border-left:3px solid var(--a);
border-radius:0 12px 12px 0;background:rgba(var(--ar),.07);box-shadow:5px 5px 0 rgba(var(--ar),.14)}
.md-body img{max-width:100%;border-radius:12px;margin:.5rem 0;border:1px solid var(--bd)}
.md-body hr{border:none;height:1px;margin:1.5rem 0;background:linear-gradient(90deg,transparent,var(--a),transparent)}
.md-body table{width:100%;border-collapse:collapse;margin:.85rem 0;font-size:.85rem}
.md-body th{padding:.55rem .75rem;text-align:left;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;
background:linear-gradient(90deg,rgba(var(--ar),.18),rgba(var(--a2r),.18))}
.md-body td{padding:.5rem .75rem;border-top:1px solid var(--bd)}
.md-body tbody tr:hover{background:rgba(var(--ar),.08)}
.code-card{border-radius:var(--r);overflow:hidden;margin:.85rem 0;
background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));
border:1px solid var(--bd);transition:.35s cubic-bezier(.2,.8,.2,1);will-change:transform}
.code-card:hover{box-shadow:0 22px 50px -18px rgba(0,0,0,.65),0 0 0 1px rgba(var(--ar),.3),
0 0 44px -10px rgba(var(--ar),.4)}
.code-head{display:flex;align-items:center;gap:.45rem;padding:.55rem .95rem;
border-bottom:1px solid var(--bd);background:rgba(0,0,0,.22)}
.dot{width:11px;height:11px;border-radius:50%}
.dot.r{background:#ff5f57}.dot.y{background:#febc2e}.dot.g{background:#28c840}
.lang{margin-left:auto;font-size:.62rem;letter-spacing:.22em;color:var(--a);text-transform:uppercase}
.code-card .highlight{background:transparent}
.code-card pre{margin:0;padding:13px 16px;overflow:auto;font-family:var(--fc);font-size:.82rem;
line-height:1.6;background:var(--code);color:#d6e2f0}
.fallback{background:var(--code)}.fallback code{color:#d6e2f0}
.copy{margin-left:.8rem;padding:.15rem .55rem;font-size:.6rem;color:#93a1b8;background:transparent;
border:1px solid rgba(255,255,255,.12);border-radius:7px;cursor:pointer;transition:.25s;font-family:var(--fb)}
.copy:hover{color:var(--a);border-color:var(--a);box-shadow:0 0 12px rgba(var(--ar),.5)}
.output-card{margin-top:.65rem;border-radius:14px;overflow:hidden;border:1px solid var(--bd);
border-left:3px solid var(--a2);background:rgba(var(--a2r),.06);transition:.35s}
.output-card:hover{transform:rotateY(-2deg) translateZ(6px);box-shadow:0 16px 36px -16px rgba(0,0,0,.55)}
.output-card.error{border-left-color:#ff5470;background:rgba(255,84,112,.08)}
.output-card.error .out-label{color:#ff8095}
.out-label{display:block;padding:.5rem .95rem .15rem;font-size:.62rem;font-weight:600;
letter-spacing:.2em;color:var(--a2);text-transform:uppercase}
.output-body{padding:.55rem .95rem .85rem;overflow:auto}
.output-body pre{font-family:var(--fc);font-size:.79rem;line-height:1.55;white-space:pre-wrap;
word-break:break-word;color:var(--tx)}
.output-body table{width:100%;border-collapse:collapse;font-size:.82rem;margin:.4rem 0}
.output-body th{background:rgba(var(--a2r),.14);padding:.45rem .7rem;text-align:left;font-size:.72rem}
.output-body td{padding:.4rem .7rem;border-top:1px solid var(--bd)}
.out-img{max-width:100%;border-radius:10px;margin:.3rem 0;border:1px solid var(--bd)}
.output-body.long{max-height:260px;overflow:hidden;position:relative}
.output-body.long::after{content:'';position:absolute;bottom:0;left:0;right:0;height:64px;
background:linear-gradient(transparent,var(--bg))}
.output-body.long.expanded{max-height:none}.output-body.long.expanded::after{display:none}
.out-toggle{margin:.15rem .95rem .75rem;padding:.25rem .8rem;font-size:.68rem;color:var(--a);
background:rgba(var(--ar),.08);border:1px solid rgba(var(--ar),.35);border-radius:8px;cursor:pointer;
transition:.25s;font-family:var(--fb)}
.reveal{opacity:0;transform:translateY(38px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.8,.2,1)}
.reveal.vis{opacity:1;transform:none}
footer{text-align:center;padding:2.4rem 1rem 3rem;color:var(--mut);font-size:.8rem;border-top:1px solid var(--bd)}
footer b{background:linear-gradient(90deg,var(--a),var(--a2));-webkit-background-clip:text;
background-clip:text;color:transparent}
.to-top{position:fixed;right:26px;bottom:26px;width:52px;height:52px;border:none;border-radius:15px;
display:grid;place-items:center;font-size:1.25rem;cursor:pointer;color:#04070d;
background:linear-gradient(135deg,var(--a),var(--a2));box-shadow:0 12px 30px -8px rgba(var(--ar),.65);
opacity:0;pointer-events:none;transform:translateY(16px);transition:.35s;animation:floatY 3.6s ease-in-out infinite}
.to-top.show{opacity:1;pointer-events:auto;transform:translateY(0)}
@media(max-width:980px){.layout{grid-template-columns:1fr}.toc{position:static;max-height:none}}
"""

JS = r"""
var bar=document.getElementById('prog'),topBtn=document.getElementById('toTop');
window.addEventListener('scroll',function(){var h=document.documentElement;
bar.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%';
topBtn.classList.toggle('show',h.scrollTop>600);},{passive:true});
topBtn.addEventListener('click',function(){scrollTo({top:0,behavior:'smooth'});});
var io=new IntersectionObserver(function(es){es.forEach(function(en){
if(en.isIntersecting){en.target.classList.add('vis');io.unobserve(en.target);}});},{threshold:.05});
document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
document.querySelectorAll('.tilt').forEach(function(c){var raf=null;
c.addEventListener('mousemove',function(e){var r=c.getBoundingClientRect();
var x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
if(raf)cancelAnimationFrame(raf);
raf=requestAnimationFrame(function(){c.style.transform='perspective(1000px) rotateY('+(x*5)+
'deg) rotateX('+(-y*5)+'deg) translateZ(8px)';});});
c.addEventListener('mouseleave',function(){if(raf)cancelAnimationFrame(raf);c.style.transform='';});});
document.querySelectorAll('.code-card').forEach(function(card){
var head=card.querySelector('.code-head');if(!head)return;
var btn=document.createElement('button');btn.className='copy';btn.textContent='\u29C9 COPY';
head.appendChild(btn);
btn.addEventListener('click',function(){
navigator.clipboard.writeText(card.querySelector('pre').innerText).then(function(){
btn.textContent='\u2713 COPIED';setTimeout(function(){btn.textContent='\u29C9 COPY';},1500);});});});
document.querySelectorAll('.out-toggle').forEach(function(b){
b.addEventListener('click',function(){var body=b.parentNode.querySelector('.output-body');
body.classList.toggle('expanded');
b.textContent=body.classList.contains('expanded')?'Show less \u25B4':'Show more \u25BE';});});
var links=[].slice.call(document.querySelectorAll('.toc a'));
var map=new Map(links.map(function(a){return[a.getAttribute('href').slice(1),a];}));
if(map.size){var io2=new IntersectionObserver(function(es){
es.forEach(function(en){if(en.isIntersecting){links.forEach(function(l){l.classList.remove('on');});
var a=map.get(en.target.id);if(a)a.classList.add('on');}});},{rootMargin:'-15% 0px -70% 0px'});
map.forEach(function(a,id){var s=document.getElementById(id);if(s)io2.observe(s);});}
"""

def toc_html(groups):
    out=[]
    for g in groups:
        out.append("<details open><summary>&#128193; %s <small>%d</small></summary><div class='tg-body'>"
                   %(esc(g["name"]),len(g["nbs"])))
        for nb in g["nbs"]:
            out.append("<a href='#nb-%d'>&#128209; %s</a>"%(nb["idx"],esc(nb["title"])))
            for h in nb["toc"]:
                if h["level"]==1: continue
                out.append("<a class='lv%d' href='#%s'>&#8226; %s</a>"%(min(h["level"],2),h["id"],esc(h["text"])))
        out.append("</div></details>")
    return "".join(out)

def build_html(title, groups, stats, theme, root):
    t=THEMES[theme]; today=datetime.now().strftime("%d %b %Y")
    mins=max(1,round(stats["words"]/200))
    faces="".join("<div class='face f%d'>%s</div>"%(i+1,f) for i,f in
                  enumerate(["\U0001F4C1","\U0001F4D3","%","{ }","\U0001F40D","\u26A1"]))
    sbox="".join("<div class='stat reveal'><div class='n'>%s</div><div class='l'>%s</div></div>"%(v,l)
        for v,l in [(len(groups),"Folders"),(stats["nbs"],"Notebooks"),(stats["code"],"Code cells"),
                    (stats["md"],"Notes"),(stats["images"],"Images"),(stats["loc"],"Lines")])
    body=[]
    for g in groups:
        body.append("<div class='folder-band reveal'>&#128193; %s<span class='cnt'>%d NOTEBOOKS</span></div>"
                    %(esc(g["name"]),len(g["nbs"])))
        body += [nb["html"] for nb in g["nbs"]]
    h=["<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>",
       "<meta name='viewport' content='width=device-width,initial-scale=1'>",
       "<title>%s — 3D Notes</title>"%esc(title),
       "<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800&family=Poppins:"
       "wght@300;400;500;600&family=Fira+Code:wght@400;500&display=swap' rel='stylesheet'>",
       "<script>window.MathJax={tex:{inlineMath:[['$','$'],['\\\\(','\\\\)']]}};</script>",
       "<script async src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js'></script>"]
    if HAS_PYG: h.append("<style>%s</style>"%PYG_CSS)
    h.append("<style>%s%s</style></head><body>"%(ROOT_T%t,CSS))
    h.append("<nav class='nav'><div class='nav-in'><span class='logo'>\u26A1 %s</span>"
             "<a class='nl' href='#toc'>\u2630 Contents</a></div><div class='prog' id='prog'></div></nav>"%esc(title))
    h.append("<header class='hero'><div class='orb o1'></div><div class='orb o2'></div><div class='orb o3'></div>"
             "<div class='cube-scene'><div class='cube'>%s</div></div><h1 class='hero-t'>%s</h1>"%(faces,esc(title))
             +"<p class='hero-s'>All-in-one 3D study notes · %d notebooks · %d folders · %s</p>"
               %(stats["nbs"],len(groups),today)
             +"<div class='badges'><span class='badge'>\U0001F4D3 <b>%d</b> notebooks</span>"%stats["nbs"]
             +"<span class='badge'>\u23F1\uFE0F ~<b>%d</b> min read</span>"%mins
             +"<span class='badge'>\U0001F5A4 <b>%s</b> theme</span></div>"%theme
             +"<div class='stats'>%s</div><a class='cue' href='#toc'>\u25BC</a></header>"%sbox)
    h.append("<main class='layout'><aside class='toc' id='toc'><h3>\U0001F4DA CONTENTS</h3>%s</aside>"
             "<div class='content'>%s</div></main>"%(toc_html(groups),"".join(body)))
    h.append("<footer>Generated from <b>%d notebooks</b> under <b>%s</b> · %s</footer>"
             %(stats["nbs"],esc(root.name),today))
    h.append("<button class='to-top' id='toTop'>\u2191</button><script>%s</script></body></html>"%JS)
    return "".join(h)

def main():
    global MAX_LEVEL, MD_ENGINE, MAX_IMG_B64
    ap=argparse.ArgumentParser()
    ap.add_argument("root",nargs="?",default=".")
    ap.add_argument("--theme",default="neon",choices=list(THEMES))
    ap.add_argument("--title",default=None)
    ap.add_argument("--max-level",type=int,default=2)
    ap.add_argument("--max-image-kb",type=int,default=0)
    ap.add_argument("--list-themes",action="store_true")
    a=ap.parse_args()
    if a.list_themes:
        for n,t in THEMES.items(): print("  %-8s %s / %s / %s"%(n,t["a"],t["a2"],t["a3"]))
        return
    MAX_LEVEL=a.max_level; MAX_IMG_B64=a.max_image_kb*1024*4//3
    if _md: MD_ENGINE=_md.Markdown(extensions=["extra","sane_lists"])
    root=Path(a.root).resolve()
    if not root.is_dir(): sys.exit("[X] Not a folder: %s"%root)
    nbs=collect_notebooks(root)
    if not nbs: sys.exit("[X] No .ipynb under %s"%root)
    groups_raw=group_by_folder(root,nbs)
    print("[OK] %d notebooks in %d folders"%(len(nbs),len(groups_raw)))
    stats={"nbs":0,"code":0,"md":0,"images":0,"loc":0,"words":0}
    groups, gi = [], 0
    for gname,paths in groups_raw:
        g={"name":gname,"nbs":[]}
        for p in paths:
            pre,_,_ = load_cells(p)
            if not pre: continue
            print("  .. [%3d] %s"%(gi+1,p.relative_to(root)))
            g["nbs"].append(render_notebook(gi,p,root,stats)); gi+=1; stats["nbs"]+=1
        if g["nbs"]: groups.append(g)
    title=a.title or prettify(root.name)
    out=root/(root.name+"_Notes_3D.html")
    out.write_text(build_html(title,groups,stats,a.theme,root),encoding="utf-8")
    print("\n[DONE] %s (%.1f KB)\n"%(out,out.stat().st_size/1024))

if __name__=="__main__":
    main()