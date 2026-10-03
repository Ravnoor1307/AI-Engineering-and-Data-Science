# 🪞 03_Shallow_vs_Deep_Copy — Aaina-Darr: Naya Box, Purani Goods?

> **Folder path:** `00_Python/03_Pythonic_Thinking/03_Shallow_vs_Deep_Copy/`
> **Level:** 🐔 · **Type:** THEORY 🎓 (no tasks — sirf id() experiments!)

---

## 📖 5-Line Summary

1. **Aliasing** `b = a` = copy NAHI — same object, do tags 🏷️🏷️; ek badla, dono badle!
2. **Shallow copy** (`.copy()`, `[:]`, `copy.copy()`): outer-fresh, **inner goods shared** 📎 — nested pe mutate karo to OG reflect-ho-jata! 🤯
3. **Deep copy** (`copy.deepcopy`): recursive full-independence — nested trees tak fresh ✂️.
4. Tuples/strings/ints immutable — `[:]` pe SAME-object reuse (optimization 🐚); par tuple-KE-ANDAR ka list deepcopy pe alag hoti!
5. JSON-roundtrip jugaad (`json.loads(json.dumps(x))`) = quick deep-copy, par set ❌, tuple→list 🧨, int-keys→str traps.

## 🌍 Analogy Corner

| Concept | Real life |
|---|---|
| aliasing 🏷️🏷️ | Ek banda, do naam — Ramu/Ram babu same ladka! |
| shallow copy 📎 | Xerox cover + staples-shared andar ke pages |
| deep copy ✂️ | page-by-page poora Xerox — koi rishtaa nahi |
| id() experiment 🪞 | aaina-dekho test — sach dikhata memory |
| JSON jugaad 🔄 | intern-ship chhota hack — types ki chot samajhdaari se |

## 📁 Files Is Folder Me

| File | Kya hai |
|---|---|
| `01_copy_concepts_theory.ipynb` | aliasing-vs-shallow-vs-deep live id() proofs; 🤯 nested-list matrix trap; 3 shallow tools same-story |
| `02_memory_diagrams_demo.ipynb` | ASCII warehouse maps 🗺️, nested-dict registry twist 🗂️, tuple-of-lists edge 🐚, JSON jugaad + 3 traps 💣 |

## 🧾 Cheat Sheet

```python
b = a                    # ❌ NOT a copy — ALIASING!
import copy
b = a.copy()             # shallow: outer fresh, inner shared 📎
b = a[:]                 # shallow (lists; tuples pe SAME object reuse!)
b = copy.copy(a)         # shallow (works on dicts/tuples/etc too)
b = copy.deepcopy(a)     # DEEP: everything fresh ✂️ (nested SAFE)

# id() experiments (sach-checkers!):
b is a                   # True → same object (aliasing / immutable-reuse)
a.copy() is a            # False (new outer) BUT:
a.copy()[0] is a[0]      # True for nested (INNER SHARED!) 😱

# JSON jugaad:
clone = json.loads(json.dumps(tree))   # deep-ish, with type-traps 💣
```

## 📊 Live-facts (from executed notebooks ✅)

- Flat list: `c = a.copy(); c.append(99)` → **a SAFE** (shallow enough) ✅
- Nested `matrix.copy()`: `c[0].append(99)` → **matrix TOO changed** 🤯 (inner shared 📎)
- deepcopy same op → matrix untouched 💔✅
- Tuple `t[:] is t` → **True** (immutable shells never copied)
- dict `.copy()` pe inner list append → dono registries me dikhta! 🗂️

## ⚠️ 5 Common Mistakes

| # | ❌ Galti | ✅ Sahi |
|---|---|---|
| 1 | `b = a` copy samajhna | `.copy()` / `[:]` / deepcopy |
| 2 | Nested pe shallow trust | `copy.deepcopy` |
| 3 | `copy.copy` nested pe deep expect | Shallow hi hota — method ≠ deep |
| 4 | Tuple slice se copy expect | Same object (no-op 🐚) |
| 5 | Bade tree pe deepcopy blind | Slow! Flat=shallow, nested=deep |

## ⏭️ Aage Kya?

**Topic 03.04 — `Mutability_vs_Immutability`** 🧊🔥 — copy ka poora game ISS family
pe chalta! 2 THEORY notebooks: clubs ka census, id() X-rays, `is` vs `==`,
mutable-default-arg traps, string-surgery costs. Sirf concepts — bohor zyada clarity!
