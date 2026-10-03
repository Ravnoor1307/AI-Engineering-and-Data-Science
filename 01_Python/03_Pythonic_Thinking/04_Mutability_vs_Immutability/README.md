# 🧊🔥 04_Mutability_vs_Immutability — Whiteboard ya Stone-Tablet?

> **Folder path:** `00_Python/03_Pythonic_Thinking/04_Mutability_vs_Immutability/`
> **Level:** 🐔 · **Type:** THEORY 🎓 (no tasks — id() X-ray lab only!)

---

## 📖 5-Line Summary

1. **Mutable** 🔥 = whiteboard: in-place edits, SAME id (list, dict, set, bytearray). **Immutable** 🧊 = stone-tablet: har change = NEW object/id (int, float, bool, str, tuple, frozenset, bytes, None).
2. `+=` **double-standards**: list pe in-place 🔥, tuple/num/str pe REBUILD 🧊 — pakka-diff yaad!
3. **Hashability rule** 🎫: dict-keys/set-fams frozen-only (str/num/pure-tuple/frozenset) — `tuple-with-list` = `unhashable type: 'list'` 💥.
4. **Mutable default-arg TRAP** 🪤 (interview legend!): `def f(box=[])` default sirf EK baar banti → shared plate; FIX = `box=None` + guard ✨.
5. `==` = values, `is` = identity (aadhar-check 💳); interning CPython-jugaad (rely NAI!); join > concat-loop ⭐; defensive-`.copy()` pattern 🛡️.

## 🌍 Analogy Corner

| Concept | Real life |
|---|---|
| mutable 🔥 | office whiteboard — mita, ussi pe likh (sab viewers affect!) |
| immutable 🧊 | stone-tablet — nai line? nayi tablet manga! |
| `+=` on list | dabbe me adda — dabba wahi, subzi badhi |
| `+=` on tuple | nayi thali meng — purani dispose! |
| hash-key club 🎫 | "only frozen members allowed" signboard |
| default-arg trap 🪤 | mess ki plate — pehle guest ke leftovers agle ko! |
| `is` vs `==` | aadhar-card match 💳 vs photo-compare 👯 |

## 📁 Files Is Folder Me

| File | Kya hai |
|---|---|
| `01_mutability_theory.ipynb` | 2-family census, 4 id() X-rays (num/str/list/tuple), hash-rule demo, interning + is-vs-== preview |
| `02_memory_behavior_experiments.ipynb` | caller-whiteboard effect 🖼️, 🪤 default-arg trap + None-fix, defensive-copy, immutability superpowers table, concat-vs-join |

## 🧾 Cheat Sheet

```python
# FAMILIES
MUTABLE  : list, dict, set, bytearray            🔥 (id stable on edit)
IMMUTABLE: int, float, bool, str, tuple, frozenset, bytes, None  🧊 (id changes)

# X-RAY (id() = aadhaar-card 💳)
x += 1          # int/str/tuple → NEW id  🧊
lst.append(i)   # list/dict/set   → SAME id 🔥

# HASH RULES (dict-key / set-member)
hash("ok")  hash(42)  hash((1,2))       # ✅ frozen club
hash([1])   hash({})  hash({1})         # ❌ TypeError — mutable rejected

# DEFAULT-ARG TRAP & FIX 🪤✨
def f(box=[]): ...      # ❌ shared plate across calls!
def f(box=None):        # ✅ None-guard pattern
    box = [] if box is None else box

# BEHAVIOR PATTERNS
def f(lst): lst.append(x)   # caller CHANGED (reference-share)
def f(lst): lst = []        # caller SAFE (reassignment local)
def f(lst): lst = lst.copy()  # DEFENSIVE — apni board! 🛡️

# is vs ==
a == b   # values match?  |  a is b   # SAME object? (id match)
# join > concat-loop for built strings ⭐
```

## 📊 Live-facts (executed notebooks ✅)

- `x=100 → x+1` : id CHANGED 🧊 · `lst.append`/`lst+=` : id SAME 🔥 · `t+=(4,)` : id REBUILD
- Default-arg 3 calls: `['math'] → ['math','math'] → ×3` 😱 → None-guard: har call fresh ✨
- `hash((['a','b'],2))` → `TypeError: unhashable type: 'list'` 💥
- `int("1000") is int("1000")` → False; small ints → True (interning = CPython jugaad, rely nai!)
- `"hero".upper()` → OG untouched 🪨 (tablet power!)

## ⚠️ 5 Common Mistakes

| # | ❌ Galti | ✅ Sahi |
|---|---|---|
| 1 | `is` values-compare ke liye | `==` (values) / `is` (identity/None) |
| 2 | Mutable default args | None-guard pattern |
| 3 | Function-mutation caller-surprise | `.copy()` defensive / document karo |
| 4 | loop me string `+=` | `"".join()` |
| 5 | dict-key me list | immutables/pure-tuples/frozenset |

## ⏭️ Aage Kya?

**Topic 03.05 — `Args_Kwargs`** 📦 — Section 03 FINALE (PRACTICAL 📝):
`*args` tuples-pack, `**kwargs` dict-pack, call-site unpack `f(*l)`/`f(**d)`,
💾 products flexible-discount lab — phir Section 03 ka crown! 👑
