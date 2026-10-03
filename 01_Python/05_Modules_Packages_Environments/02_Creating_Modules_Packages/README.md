# 🛠️ 02_Creating_Modules_Packages — Khud-Ki-Library ka Dabba! 🥡

> **Folder path:** `00_Python/06_Modules_Packages_Environments/02_Creating_Modules_Packages/`
> **Level:** 🐥→🐔 · **Type:** PRACTICAL 📝 · **Concepts:** apna-module, __main__-guard, sys.path, packages+__init__.py, relative-imports

---

## 📖 5-Line Summary

1. **Apna module** = koi-bhi `.py` file jo tum import kar sakte ho — private-library ka dabba 🥡 (dabba-recipes ka photo-copy nahi — ek book share!)
2. **Import-cycle** 🔄: sys.modules-cache → sys.path-folders-scan → file-execute → namespace-bind (cache → 2nd-import CHEAP!)
3. **`__name__ == "__main__"`** 🔑 = gate-keeper: import-side silent (library-mode!), script-side loud (demo/self-tests!) — unguarded prints = import-noise kharch!
4. **Package** = folder + `__init__.py` (index-card 📣 — banner-fire + re-export shortcuts!); 3-styles: `import pkg` / `from pkg import mod` / `from pkg.mod import fn`; **relative-imports** sibling-link (`from .billing import tax`, entry-file root-must! 🧭)
5. Dunder-zoo-peep: `__name__/__doc__/__package__` + dir()-public-filter (`not n.startswith("_")`) — module-guide build! 🔍

## 🌍 Analogy Corner

| Concept | Real life |
|---|---|
| apna-module 📦 | apni dabba-recipe-book (counters share!) |
| sys.path 🗺️ | postman ka pata-daftar (folders-scan!) |
| sys.modules cache 🧠 | already-served dabba tray (again FREE!) |
| `__main__` guard 🔑 | stage-Rehearsal vs public-performance switch! |
| package-folder 🏪 | almaari with labeled drawers (index-card!) |
| `__init__.py` 📣 | drawer-ka index-card (welcome + shortcuts!) |
| relative-imports 🔌 | same-dabba-box ke andar ki tubes (root-run pe fail!) |
| heavy-init 🐌 | welcome-desk pe chai-banao (kaam-ruksha!) |

## 📁 Files Is Folder Me

| File | Kya hai |
|---|---|
| `01_own_modules_theory.ipynb` | grade_utils.py live-build+import, dir/docstring peep, cache-proof, guard-twins (import-silent vs script-loud via subprocess!) 🔑 |
| `02_packages_structure.ipynb` | dukan-package tree 🏪, banner-fire, 3-import-styles, relative-import gyaan, dunder-peep |
| `task.ipynb` | 7 tasks ⭐→🏆 — salam-module se **Kotini-Toolkit audit-card** (banner + re-exports + 4-line straight-table! 📋) tak |

## 🧾 Cheat Sheet

```python
# APNA MODULE:
# grade_utils.py (file!) → sys.path me folder → import!
import sys
sys.path.insert(0, "/path/haan-file")
import grade_utils as gu
gu.__doc__                                  # self-guide 📖
[n for n in dir(gu) if not n.startswith("_")]   # public-filter! 🔍

# CLEANUP-professional (demos ke baadh!):
sys.path.pop(0)
sys.modules.pop("grade_utils", None)        # cache-flush 🧹

# __MAIN__-GUARD 🔑:
def kaam(): ...
if __name__ == "__main__":
    print("script-mode!")                   # import pe silent! 🤫

# PACKAGE STRUCTURE:
# dukan/
# ├── __init__.py   → doc + banner + `from .billing import total_bill`
# ├── billing.py    → TAX + tax() + total_bill()
# └── catalog.py    → ITEMS + describe()
import dukan                                # banner-FIRES!
dukan.total_bill(1000)                      # re-export shortcut! 📣
from dukan.billing import tax               # dotted-import
from dukan import catalog                   # module-import
# sibling: from .catalog import ITEMS  (relative — root-run pe ❌!)
```

## 📊 Live-facts (executed ✅)

- grade_utils: `average([80,90,70]) = 80.0` · `grade_letter(88) = B` · `topper = Priya`
- Subprocess-magic: SAME-file import pe sirf baaraat 🎺 / script pe dono-prints 🔑
- cache-proof: `gu is gu_2 → True` (same-object!)
- dukan: banner + `total_bill(1000)=1050.0` · `tax(2000)=100.0` · jalebi ₹80
- kedai: banner 🔔 + `total_bill(2000)=2100.0`
- BOSS: Kotini-card 4-lines aligned · tax 5000.0 · savings-rate 25.0% — audit-ready 🛡️

## ⚠️ 5 Common Mistakes

| # | ❌ Galti | ✅ Sahi |
|---|---|---|
| 1 | loud-prints unguarded module me | `__name__` guard 🔑 |
| 2 | sys.path dirty-chunks | pop + modules.pop cleanup 🧹 |
| 3 | edit ke-baadh "purana-result?!" (cache!) | `importlib.reload(module)` 🔄 |
| 4 | `python pkg/sub.py` (relative-fail!) | entry-file root me, dotted-call! 🧭 |
| 5 | heavy-compute __init__ me 🐌 | light-wiring (shortcuts/docs!) |

## ⏭️ Aage Kya?

**06.03 `Virtual_Environments`** (no-task — terminal commands! 🏰) —
**venv** ka separate-kitchen philosophy (dependency-isolation!),
create/activate/freeze ka recipe-flow + **conda vs pip vs uv ⚡** tools
compare — bullet-train speed ka evolution-chart! 🚀
