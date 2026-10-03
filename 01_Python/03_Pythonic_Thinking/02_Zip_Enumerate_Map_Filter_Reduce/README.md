# 🔗 02_Zip_Enumerate_Map_Filter_Reduce — Assembly Line ka Quartet

> **Folder path:** `00_Python/03_Pythonic_Thinking/02_Zip_Enumerate_Map_Filter_Reduce/`
> **Level:** 🐥→🐔 · **Type:** PRACTICAL 📝 · **Datasets:** students_marks.csv (50) + products_catalog.csv (30)

---

## 📖 5-Line Summary

1. **`zip(a, b)`** = teeth-interlock 🤐 (lazy!, pairs tuples me); uneven lists pe **shortest-stop**, 3.10+ `strict=True` guard; `zip(*z)`=unzip, `dict(zip(k,v))`=factory.
2. **`enumerate(seq, start=1)`** = queue-token counter 🎫 — `range(len(...))` ka pythonic replacement, index-hunt bhi clean.
3. **`map(fn, items)`** = spray-paint machine 🎨 (lazy, multi-iterable!); **`filter(fn, items)`** = quality-gate chhalni ✂️; dono `list()` wrap karke dikhte.
4. **`reduce(fn, items[, init])`** = rolling-pin blender 🌀 (functools import!) — par **built-ins GO**: sum/max/min/math.prod!
5. Pythonic ⚖️: ready-fn → map/filter ✔️ / custom-lambda → comprehension 💛 / count-only → `sum(1 for...)`. 💾 students top: Manish_29 418; class avg 65.69; inventory ₹16.6M!

## 🌍 Analogy Corner

| Concept | Real life |
|---|---|
| zip 🤐 | bag ka zipper — do columns interlock, ek miss-mate pe pure-band! |
| enumerate 🎫 | bank-khanka token — number + saamne-wala dono milte |
| map 🎨 | spray-paint station — HAR item pe same job |
| filter ✂️ | namkeen weight-gate — halki packets gir-jati |
| reduce 🌀 | blender end — sab fruits daalke ONE shake |
| unzip ⭐ | zip kholke dono taang-feet alag! 🦷 |

## 📁 Files Is Folder Me

| File | Kya hai |
|---|---|
| `01_zip_enumerate_theory.ipynb` | Shimla-lunch counters, zip basics+strict-part+unzip+dict-factory, enumerate tokens, 💾 leaderboard combo |
| `02_map_filter_reduce.ipynb` | Factory trio live, 2-iterable map ⚡, reduce+initial safety, pythonic-boxing table, 💾 GST+premium+inventory pipelines |
| `task.ipynb` | 7 tasks ⭐→🏆 — zip-fit se 💾 **CLASS REPORT CARD BOSS** (topper avg 83.6, CS-topper Kavya_22 100!) tak |

## 🧾 Cheat Sheet

```python
zip(a, b)                 # [('x', 1), ...] lazy! shortest-stop
zip(a, b, strict=True)    # mismatched lens → ValueError (3.10+)
dict(zip(keys, vals))     # mini-dict factory
zip(*zipped)              # UNZIP trick! (star khol-deta)

enumerate(items)          # (0, item), (1, item)...
enumerate(items, start=1) # human numbering
[i for i, x in enumerate(xs) if cond]   # index-hunt pythonic!

map(fn, items)            # lazy transformer; list() wrap to see
map(lambda a, b: a+b, A, B)  # MULTI-iterable map!
filter(fn, items)         # lazy gate-keeper; list() wrap
sum(1 for x in xs if cond)   # pythonic anonymous-counter ⭐

from functools import reduce
reduce(lambda a,b: a op b, xs)          # rolling-combine
reduce(fn, xs, initial)                 # empty-safe reduce!
# BUT prefer: sum(xs) max(xs) min(xs) math.prod(xs)
```

## 📊 Dataset Numbers (bash-verified ✅)

| Fact (students_marks.csv, 50 rows) | Value |
|---|---|
| Top-5 totals | Manish_29 418 · Ananya_20 401 · Arjun_11 397 · Sneha_24 393 · Priya_44 390 |
| Top-5 avgs | 83.60 · 80.20 · 79.40 · 78.60 · 78.00 |
| Distinction (avg≥80) | 2 — Manish_29 (83.6), Ananya_20 (80.2) |
| Class avg | 65.69 · **27/50 above class-normal** |
| CS topper | Kavya_22 (100/100) |

| Fact (products_catalog.csv, 30 rows) | Value |
|---|---|
| GST first-3 (18%) | Laptop→56640 · Smartphone→17700 · Headphones→2360 |
| Premium (>₹10k) | 4 — Laptop, Smartphone, Tablet, DSLR_Camera |
| Inventory value | ₹16,629,090 (price×stock sabka sum) |

## ⚠️ 5 Common Mistakes

| # | ❌ Galti | ✅ Sahi |
|---|---|---|
| 1 | zip/map/filter 2nd-pass reuse (silent🤫empty!) | Fresh machine banana, list() store kabaki-hi |
| 2 | uneven zip assume "sab pairs hue" | shortest-stop! guard: strict=True |
| 3 | `reduce` bina import NameError 💥 | `from functools import reduce` |
| 4 | reduce pe sum/max re-implement | Built-ins direct chalao (C-speed + readable) |
| 5 | `for i in range(len(x))` | `for i, x in enumerate(x)` |

## ⏭️ Aage Kya?

**Topic 03.03 — `Shallow_vs_Deep_Copy`** 🪞 — 2 THEORY notebooks: copy karke
bhi OG ka duplicate NAHI banana (aaina-darr!), nested dicts ka 🤯 twist,
ASCII memory-diagrams ke saath. No tasks (THEORY) — par experiments masti-bhare!
