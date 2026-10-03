# 🎁 05_Args_Kwargs — Chemist-Thali & Gift-Bag Functions (Section 03 FINALE 👑)

> **Folder path:** `00_Python/03_Pythonic_Thinking/05_Args_Kwargs/`
> **Level:** 🐥→🐔 · **Type:** PRACTICAL 📝 · **Dataset:** products_catalog.csv (30 items)

---

## 📖 5-Line Summary

1. **Positional** (order-match) vs **Keyword** (`name=value`, order-free) — caller side positional PEHLE, keyword BAAD (reverse = SyntaxError allarm)!
2. **Defaults** = optional params; mutable-default (`=[]`) = 🪤 trap — None-guard yaad (03.04!)
3. **`*args`** = extra positionals ka **tuple-pack** 🛍️ (empty-safe; `print()` khud isi ka GOAT 🐐)
4. **`**kwargs`** = named extras ka **fresh-dict** pack 🎁 (`.get(key, default)` = graceful); signature order: pos → defaults → `*args` → **kw-only** → `**kwargs`
5. Call-side **star-openers** ⭐: `f(*list)` positional-unpack, `f(**dict)` name-match unpack; 💾 Smart Bill Maker ₹58,012.5 recipe 📜

## 🌍 Analogy Corner

| Concept | Real life |
|---|---|
| `*args` 🛍️ | chemist-thali — 2 items ya 20, sab ek jhol me (tuple!) |
| `**kwargs` 🎁 | gift-bag tags — name/city pe tag laga bhare, bheed nahi! |
| kw-only zone 👮 | "explicit-name do warna nahi" wala border |
| `f(*list)` ⭐ | gift kholo — elements seedha fingereprints pe |
| `f(**dict)` | label-by-label items matching boxes me |
| `**flags` gobble | form ka *"any other info"* box 📮 — optional writing! |

## 📁 Files Is Folder Me

| File | Kya hai |
|---|---|
| `01_args_kwargs_theory.ipynb` | call-styles + missing/dupe arg errors, `*args` tupleproof, kw-only zone, signature anatomy law |
| `02_unpacking_use_cases.ipynb` | `**kwargs` live, full-sign-combo, call-side star-openers ⭐, partial 🍛, 💾 discount-lab + receipt ₹61,925 |
| `task.ipynb` | 7 tasks ⭐→🏆 — call-wrestling se 💾 **SMART BILL MAKER** (member-discount 15%, Mogambo skip ⚠️) tak |

## 🧾 Cheat Sheet

```python
# SIGNATURE ORDER LAW (fixed!)
def f(pos1, pos2="d", *args, kw_only=0, **kwargs): ...
# caller: f(1, 2, 99, 98, kw_only=5, x=1, y=2)  # pos → defaults → *args → kw-only → **kwargs

*args       # → tuple (immutable!) of extra positionals 🛍️
**kwargs    # → fresh dict of named extras 🎁  (.get(k, default))

# CALL-SIDE STAR-OPENERS ⭐
f(*[10, 20, 30])      # list → positional args
f(**{"name": "Ravi", "city": "Pune"})   # dict → keyword args (name-match!)
max(*[4, 9, 2, 8])    # max khud *args leta!

# PARTIAL (functools) — curry-ka-chhota 🍛
from functools import partial
eighteen_off = partial(discount_calc, 0.18); eighteen_off(48000)  # 39360.0

# ERROR LANDMARKS
missing-arg TypeError   : f() missing 1 required positional argument: 'city'
dupe-arg   TypeError 💥  : got multiple values for argument 'a'
kw-only positional 👮🚨 : takes N positional arguments but M were given
```

## 📊 Dataset Numbers (bash-verified ✅, products_catalog.csv)

| Fact | Value |
|---|---|
| Catalog | 30 products (name2price dict built) |
| 18%-off first-3 | Laptop→39360 · Smartphone→12300 · Headphones→1640 |
| Smart Bill #1 | sub ₹65,000 → member15% → ₹55,250 → +5%GST → **₹58,012.5** |
| Smart Bill #2 (unpack-★) | ₹105 → 5% off ₹99.75 → +5%GST → **₹104.7** |
| Graceful skip | "Mogambo" → `⚠️ skipped` (dict-miss handled!) |

## ⚠️ 5 Common Mistakes

| # | ❌ Galti | ✅ Sahi |
|---|---|---|
| 1 | `f(x=1, 2)` kw-then-pos | positional-first always |
| 2 | `def f(a=1, b)` | required-first: `def f(b, a=1)` |
| 3 | mutable default `= []` 🪤 | `= None` + guard |
| 4 | unordered signature (*args/**kwargs jumbled) | ORDER LAW fix karo! |
| 5 | dupe kwarg (`f(5, a=2)`) 💥 | names dedupe karo |

## ⏭️ Aage Kya?

# 🎉 SECTION 03 — COMPLETE! 5/5 👑
**Next: SECTION 04 `OOP`** 🏗️ — 04.01 `Classes_Objects`: blueprint se building
(Student class from marks.csv!), `self` ka real-role, methods+attributes game!
MASTER_PLAN queue ready — "continue" bolo! 🚀
