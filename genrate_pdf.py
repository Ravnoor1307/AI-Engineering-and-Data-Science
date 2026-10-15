#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
generate_pdf_notes.py — scans every sub-folder for .ipynb → HANDWRITTEN-style
notes (grid paper, ink pens, highlighter, taped code screenshots) → PDF.

USAGE:
  python generate_pdf_notes.py [root] --paper grid --logo "🔥"
  python generate_pdf_notes.py --paper lines --no-pdf
"""
import argparse, json, os, re, shutil, subprocess, sys
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
    _PYG_FMT = HtmlFormatter(style="friendly", noclasses=True)   # inline colours → light paper
    HAS_PYG = True
except ImportError:
    HAS_PYG = False

SKIP_DIRS = {".ipynb_checkpoints",".git","__pycache__",".venv","venv","env",
             "node_modules",".pytest_cache",".mypy_cache","dist","build",
             ".virtual_documents"}
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")
H_RE = re.compile(r"<h([1-6])((?:\s[^>]*)?)>(.*?)</h\1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")

def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def natkey(s): return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)",s)]
def prettify(n): return re.sub(r"[-_]+"," ",n).strip().title()

def collect_notebooks(root):
    f=[p for p in root.rglob("*.ipynb") if not any(x in SKIP_DIRS for x in p.parts)
       and not p.name.endswith("-checkpoint.ipynb")]
    f.sort(key=lambda p:(natkey(str(p.parent.relative_to(root)).lower()),natkey(p.name.lower())))
    return f

def group_by_folder(root,nbs):
    g,order={},[]
    for p in nbs:
        k=str(p.parent.relative_to(root))
        if k not in g: g[k]=[];order.append(k)
        g[k].append(p)
    return [(k,g[k]) for k in order]

_NB_CACHE={}
def load_cells(nb_path):
    key=str(nb_path.resolve())
    if key in _NB_CACHE: return _NB_CACHE[key]
    try: nb=json.loads(nb_path.read_text(encoding="utf-8-sig"))
    except Exception as e:
        print("      !! skipped (%s)"%e.__class__.__name__)
        _NB_CACHE[key]=([],{},None); return _NB_CACHE[key]
    cells=nb.get("cells")
    if not cells and "worksheets" in nb: cells=nb["worksheets"][0].get("cells",[])
    _NB_CACHE[key]=(cells or [],nb.get("metadata",{}),None)
    return _NB_CACHE[key]

def src_of(c):
    s=c.get("source","");return "".join(s) if isinstance(s,list) else (s or "")

def parse_output(o):
    t=o.get("output_type"); j=lambda v:"".join(v) if isinstance(v,list) else (v or "")
    if t=="stream": return {"kind":"text","text":ANSI_RE.sub("",j(o.get("text")))}
    if t in ("execute_result","display_data"):
        d=o.get("data",{})
        for m,k in (("image/png","image"),("image/jpeg","image"),("image/svg+xml","svg"),
                    ("text/html","html"),("text/plain","text")):
            if m in d: return {"kind":k,"mime":m,"text":ANSI_RE.sub("",j(d[m]))}
    if t=="error":
        return {"kind":"error","text":ANSI_RE.sub("","\n".join(o.get("traceback",[])))}
    return None

MAX_LEVEL, MD_ENGINE, MAX_IMG_B64, TRUNC = 2, None, 0, 46

def code_html(code,lang):
    if HAS_PYG:
        try: return _pyg(code,get_lexer_by_name(lang,stripnl=False),_PYG_FMT)
        except Exception: pass
    return esc(code)

def md_html(src,cell):
    for f,att in (cell.get("attachments") or {}).items():
        for m,b in att.items():
            src=src.replace("attachment:%s"%f,"data:%s;base64,%s"%(m,re.sub(r"\s","",b)))
    if MD_ENGINE: MD_ENGINE.reset(); return MD_ENGINE.convert(src)
    return "<pre class='shot'>%s</pre>"%esc(src)

def inject_ids(html,pre):
    ent,n=[],[0]
    def r(m):
        n[0]+=1; hid="%s-s%d"%(pre,n[0])
        ent.append({"level":int(m.group(1)),"id":hid,"text":TAG_RE.sub("",m.group(3)).strip()})
        return '<h%s id="%s"%s>%s</h%s>'%(m.group(1),hid,m.group(2),m.group(3),m.group(1))
    return H_RE.sub(r,html),ent

def render_cells(cells,idx,nbfile,stats):
    parts,toc=[],[]
    for i,c in enumerate(cells):
        ct=c.get("cell_type")
        if ct=="raw": continue
        src=src_of(c)
        if ct=="markdown":
            stats["md"]+=1
            body,heads=inject_ids(md_html(src,c),"n%d"%idx)
            toc+=[h for h in heads if h["level"]<=MAX_LEVEL]
            parts.append("<div class='md'>%s</div>"%body)
        elif ct=="code":
            stats["code"]+=1
            outs=[]
            for o in (c.get("outputs") or []):
                po=parse_output(o)
                if not po: continue
                if po["kind"]=="image":
                    b64=re.sub(r"\s","",po["text"])
                    if MAX_IMG_B64 and len(b64)>MAX_IMG_B64:
                        outs.append("<div class='pic'><div class='out-tag red'>image too big "
                                    "(%.1f MB) — not printed</div></div>"%(len(b64)*.75/1e6));continue
                    stats["images"]+=1
                    outs.append("<div class='pic'><img src='data:%s;base64,%s'></div>"%(po["mime"],b64))
                elif po["kind"]=="svg":
                    stats["images"]+=1; outs.append("<div class='pic'>%s</div>"%po["text"])
                elif po["kind"]=="html":
                    outs.append("<div class='rich'>%s</div>"%po["text"])
                else:
                    err=po["kind"]=="error"; lines=po["text"].splitlines()
                    if len(lines)>TRUNC:
                        txt=esc("\n".join(lines[:TRUNC]))+ \
                            "<div class='cut'>... [+%d lines cut]</div>"%(len(lines)-TRUNC)
                    else: txt=esc(po["text"])
                    outs.append("<div class='out'><span class='out-tag %s'>%s</span>"
                                "<pre>%s</pre></div>"%("red" if err else "green",
                                "error ✗" if err else "output ↴", txt))
            long_cls = " long" if src.count("\n")>26 else ""
            parts.append("<div class='shot%s' data-file='%s'>%s</div>"
                         %(long_cls,esc(nbfile),code_html(src,"python")))
            parts.append("".join(outs))
    return "".join(parts),toc

def nb_title(meta,cells,path):
    if meta.get("title"): return str(meta["title"])
    for c in cells:
        if c.get("cell_type")=="markdown":
            m=re.search(r"^#\s+(.+)$",src_of(c),re.M)
            if m: return m.group(1).strip().strip("#").strip()
    return prettify(path.stem)

def render_notebook(idx,path,root,stats):
    cells,meta,_=load_cells(path)
    title=nb_title(meta,cells,path)
    mtime=datetime.fromtimestamp(path.stat().st_mtime).strftime("%d %B %Y  %H:%M")
    body,toc=render_cells(cells,idx,path.name,stats)
    head=("<div class='nb-top'><div><div class='nb-title'>%s</div>"
          "<div class='nb-date'>%s</div></div><div class='logo%emoji%'></div></div>")
    head=("<div class='nb-top'><div><div class='nb-title'>%s</div>"
          "<div class='nb-date'>%s</div></div></div>"%(esc(title),mtime))
    return {"idx":idx,"title":title,
            "html":"<section class='nb' id='nb-%d'>%s%s<div class='end-mark'>— end of “%s” —</div></section>"
                    %(idx,head,body,esc(title)),
            "toc":[{"level":1,"id":"nb-%d"%idx,"text":title}]+toc}

# ═══════════════ handwritten paper CSS ═══════════════
CSS = r"""
@page{size:A4;margin:11mm 12mm 14mm}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;padding:0}
body{background-color:#fbfdff;color:#1e293b;font-size:11.5pt;line-height:1.8;
font-family:'Kalam','Segoe Print','Comic Sans MS',cursive;
background-image:linear-gradient(rgba(147,197,253,.20) 1px,transparent 1px),
linear-gradient(90deg,rgba(147,197,253,.20) 1px,transparent 1px);
background-size:21px 21px}
body.paper-lines{background-image:repeating-linear-gradient(transparent,transparent 27px,
rgba(147,197,253,.35) 28px)}
body.paper-plain{background-image:none;background-color:#fefefe}
p{orphans:3;widows:3}
a{color:#2563eb;text-decoration:underline}
h1,h2,h3,h4{page-break-after:avoid;font-family:'Caveat','Segoe Print',cursive;line-height:1.2}
h1{font-size:23pt;font-weight:700;color:#1d4ed8;margin:7mm 0 2.5mm}
h2{font-size:18.5pt;font-weight:700;color:#2563eb;margin:6mm 0 2mm;
text-decoration:underline;text-decoration-color:#93c5fd;text-underline-offset:4px;text-decoration-thickness:2px}
h3{font-size:16pt;font-weight:700;color:#059669;margin:5mm 0 1.5mm}
h4{font-size:14pt;font-weight:700;color:#d97706;margin:4mm 0 1.5mm}
strong,b{color:#dc2626;font-weight:700}          /* red pen */
mark{background:linear-gradient(100deg,transparent 3%,#fef08a 3%,#fde047 92%,transparent 95%);
padding:0 1.5mm;color:#713f12}
/* markdown body */
.md p{margin:2mm 0}
.md ul{list-style:none;margin:2mm 0 2mm 4mm;padding:0}
.md ul>li{position:relative;padding-left:7mm;margin:1.6mm 0}
.md ul>li::before{content:'•';position:absolute;left:0;color:#2563eb;font-weight:700}
.md ol{list-style:none;counter-reset:hc;margin:2mm 0 2mm 2mm;padding:0}
.md ol>li{counter-increment:hc;position:relative;padding-left:11mm;margin:2.4mm 0}
.md ol>li::before{content:counter(hc);position:absolute;left:0;top:.2mm;width:7.6mm;height:7.6mm;
border:1.7px solid #2563eb;border-radius:50%;display:flex;align-items:center;justify-content:center;
font-family:'Caveat',cursive;font-weight:700;font-size:12.5pt;color:#2563eb;background:#fff}
.md code{font-family:'Caveat',cursive;font-size:14pt;font-weight:600;color:#713f12;
background:linear-gradient(100deg,transparent 3%,#fef08a 3%,#fde047 92%,transparent 95%);
padding:0 1.5mm;border-radius:1mm}
.md pre{font-family:'Cascadia Code',Consolas,monospace;font-size:9pt;background:#fff;
border:1px solid #dbe3ef;border-radius:3mm;padding:3mm;white-space:pre-wrap;word-break:break-word}
.md blockquote{color:#166534;background:rgba(134,239,172,.25);border-left:3px solid #4ade80;
padding:2mm 4mm;border-radius:0 3mm 3mm 0;margin:3mm 0}
.md img{max-width:100%;max-height:120mm;border-radius:2mm}
.md hr{border:none;border-top:2px dashed #93c5fd;margin:6mm 0}
.md table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:3mm 0;background:#fff;
border:1px solid #cbd5e1;border-radius:2mm;overflow:hidden}
.md th{background:#e0f2fe;border:1px solid #dbeafe;padding:1.6mm 2.4mm;text-align:left;
font-family:'Caveat',cursive;font-size:11.5pt;color:#0c4a6e}
.md td{border:1px solid #e2e8f0;padding:1.4mm 2.4mm}
/* taped code screenshot */
.shot{background:#fff;border:1px solid #dbe3ef;border-radius:3mm;position:relative;
box-shadow:0 2mm 5mm rgba(30,58,138,.13);margin:4mm 0;padding:4mm 4mm 3mm;
font-family:'Cascadia Code','DejaVu Sans Mono',Consolas,monospace;
font-size:8.6pt;line-height:1.55;white-space:pre-wrap;word-break:break-word;
page-break-inside:avoid}
.shot.long{page-break-inside:auto}
.shot::before{content:'📄 ' attr(data-file);display:block;font-family:'Kalam',cursive;
font-size:8.5pt;color:#94a3b8;margin-bottom:1.6mm}
.shot::after{content:'';position:absolute;top:-2.4mm;left:50%;width:20mm;height:5.5mm;
transform:translateX(-50%) rotate(-2deg);background:rgba(253,224,71,.55);
border:1px solid rgba(202,138,4,.25);border-radius:1mm}
.shot .highlight{background:transparent}
/* output scribbles */
.out{margin:2.5mm 0 4mm 6mm;page-break-inside:avoid}
.out pre{margin:0;font-family:'Cascadia Code',Consolas,monospace;font-size:8.4pt;
color:#334155;white-space:pre-wrap;word-break:break-word}
.out-tag{display:inline-block;font-family:'Caveat',cursive;font-size:13pt;font-weight:700}
.out-tag.green{color:#059669}.out-tag.red{color:#dc2626}
.cut{color:#94a3b8;font-style:italic;font-size:8.5pt;padding-top:1mm}
.pic{background:#fff;border:1px solid #e2e8f0;padding:2.5mm;box-shadow:0 2mm 5mm rgba(30,58,138,.13);
margin:4mm auto;max-width:94%;page-break-inside:avoid;text-align:center;
transform:rotate(.35deg)}
.pic img{max-width:100%;max-height:120mm}
.rich{page-break-inside:avoid;margin:3mm 0}
.rich table{width:100%;border-collapse:collapse;font-size:9pt;background:#fff;border:1px solid #cbd5e1}
.rich th{background:#e0f2fe;border:1px solid #dbeafe;padding:1.5mm 2.2mm}
.rich td{border:1px solid #e2e8f0;padding:1.3mm 2.2mm}
/* notebook header (OneNote style) */
section.nb{page-break-before:always}
.nb-top{display:flex;justify-content:space-between;align-items:flex-start;
border-bottom:1.5px dashed #93c5fd;padding-bottom:2mm;margin-bottom:4mm}
.nb-title{font-family:'Kalam',cursive;font-size:11pt;color:#475569}
.nb-date{font-size:9pt;color:#94a3b8}
.end-mark{text-align:center;font-family:'Caveat',cursive;font-size:13pt;color:#94a3b8;
margin:8mm 0 2mm}
/* cover */
.cover{page-break-after:always;text-align:center;padding-top:66mm}
.cover .pill{display:inline-block;font-family:'Caveat',cursive;font-size:14pt;color:#7c3aed;
border:2px dashed #c4b5fd;border-radius:999px;padding:1mm 7mm;transform:rotate(-1.5deg)}
.cover h1{font-family:'Caveat',cursive;font-size:46pt;color:#1d4ed8;margin:6mm 0 2mm;
transform:rotate(-.6deg)}
.cover .sub{font-size:12.5pt;color:#475569}
.cover .doodle{margin-top:14mm;font-size:26pt;letter-spacing:6mm;transform:rotate(1deg)}
/* handwritten TOC */
.toc-page{page-break-after:always}
.toc-page h2{font-size:22pt;margin-bottom:4mm}
.toc-g{font-family:'Caveat',cursive;font-size:16.5pt;color:#7c3aed;margin:5mm 0 1mm;font-weight:700}
.toc a{display:flex;align-items:baseline;gap:2mm;font-family:'Caveat',cursive;font-size:14.5pt;
color:#1e293b;text-decoration:none;padding:.8mm 0}
.toc a .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:78%}
.toc a .dots{flex:1;border-bottom:2px dotted #93c5fd;transform:translateY(-1.4mm)}
.toc a.lv2{padding-left:9mm;font-size:12.5pt;color:#475569}
"""

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700'
         '&family=Kalam:wght@300;400;700&display=swap" rel="stylesheet">')

def toc_html(groups):
    out=[]
    for g in groups:
        out.append("<div class='toc-g'>📁 %s</div>"%esc(g["name"]))
        for nb in g["nbs"]:
            out.append("<a href='#nb-%d'><span class='t'>📓 %s</span><span class='dots'></span></a>"
                       %(nb["idx"],esc(nb["title"])))
            for h in nb["toc"]:
                if h["level"]==1: continue
                out.append("<a class='lv2' href='#%s'><span class='t'>✎ %s</span>"
                           "<span class='dots'></span></a>"%(h["id"],esc(h["text"])))
    return "".join(out)

def build_print_html(title,groups,stats,root,paper):
    today=datetime.now().strftime("%d %B %Y")
    cover=("<div class='cover'><div class='pill'>handwritten course notes</div>"
           "<h1>%s</h1><p class='sub'>%d notebooks · %d folders · %s</p>"
           "<div class='doodle'>✏️ 📓 ✨</div></div>"%(esc(title),stats["nbs"],len(groups),today))
    tocdiv="<div class='toc-page'><h2>Contents</h2>%s</div>"%toc_html(groups)
    body=[]
    for g in groups:
        body += [nb["html"] for nb in g["nbs"]]
    h=["<!DOCTYPE html><html><head><meta charset='utf-8'>",
       "<title>%s — Handwritten Notes</title>"%esc(title),FONTS]
    h.append("<style>%s</style></head><body class='paper-%s'>"%(CSS,paper))
    h.append(cover); h.append(tocdiv); h.extend(body)
    h.append("<div class='end-mark'>✦ compiled from %d notebooks · %s ✦</div>"%(stats["nbs"],today))
    h.append("</body></html>")
    return "".join(h)

# ── PDF via Edge/Chrome headless ─────────────────────────────
def find_browser():
    for n in ("chrome","msedge","chromium"):
        p=shutil.which(n)
        if p: return p
    for c in [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
              os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe")]:
        if os.path.exists(c): return c
    return None

def pdf_with_browser(html_path,pdf_path):
    b=find_browser()
    if not b: return False
    html_path,pdf_path=Path(html_path).resolve(),Path(pdf_path).resolve()
    try:
        subprocess.run([b,"--headless","--disable-gpu","--hide-scrollbars",
                        "--virtual-time-budget=20000","--no-pdf-header-footer",
                        "--print-to-pdf="+str(pdf_path),html_path.as_uri()],
                       capture_output=True,timeout=600)
    except Exception:
        return False
    return pdf_path.exists() and pdf_path.stat().st_size>1000

def main():
    global MAX_LEVEL,MD_ENGINE,MAX_IMG_B64
    ap=argparse.ArgumentParser()
    ap.add_argument("root",nargs="?",default=".")
    ap.add_argument("--title",default=None)
    ap.add_argument("--max-level",type=int,default=2)
    ap.add_argument("--max-image-kb",type=int,default=0)
    ap.add_argument("--paper",default="grid",choices=["grid","lines","plain"])
    ap.add_argument("--no-pdf",action="store_true")
    a=ap.parse_args()
    MAX_LEVEL=a.max_level; MAX_IMG_B64=a.max_image_kb*1024*4//3
    if _md: MD_ENGINE=_md.Markdown(extensions=["extra","sane_lists"])
    root=Path(a.root).resolve()
    if not root.is_dir(): sys.exit("[X] Not a folder: %s"%root)
    nbs=collect_notebooks(root)
    if not nbs: sys.exit("[X] No .ipynb under %s"%root)
    groups_raw=group_by_folder(root,nbs)
    print("[OK] %d notebooks in %d folders"%(len(nbs),len(groups_raw)))
    stats={"nbs":0,"code":0,"md":0,"images":0}
    groups,gi=[],[0]
    gi=0
    for gname,paths in groups_raw:
        g={"name":gname,"nbs":[]}
        for p in paths:
            pre,_,_=load_cells(p)
            if not pre: continue
            print("  .. [%3d] %s"%(gi+1,p.relative_to(root)))
            g["nbs"].append(render_notebook(gi,p,root,stats)); gi+=1; stats["nbs"]+=1
        if g["nbs"]: groups.append(g)
    title=a.title or prettify(root.name)
    phtml=root/(root.name+"_Handwritten_print.html")
    phtml.write_text(build_print_html(title,groups,stats,root,a.paper),encoding="utf-8")
    print("\n[OK] Print HTML : %s (%.1f KB)"%(phtml,phtml.stat().st_size/1024))
    if a.no_pdf:
        print("[DONE] open it → Ctrl+P → Save as PDF"); return
    ppdf=root/(root.name+"_Handwritten_Notes.pdf")
    print("[..] Building PDF via Edge/Chrome headless ...")
    if pdf_with_browser(phtml,ppdf):
        print("[OK] PDF        : %s (%.1f KB)\n[DONE]"%(ppdf,ppdf.stat().st_size/1024))
    else:
        print("[!] PDF failed → open %s → Ctrl+P → Save as PDF"%phtml)

if __name__=="__main__":
    main()