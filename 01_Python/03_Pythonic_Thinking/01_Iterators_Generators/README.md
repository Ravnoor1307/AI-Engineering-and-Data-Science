# ♻️ 01_Iterators_Generators — Lazy Machine Wali Duniya

> **Folder path:** `00_Python/03_Pythonic_Thinking/01_Iterators_Generators/`
> **Level:** 🐥→🐔 · **Type:** THEORY+PRACTICAL 🎓📝 (no separate task notebook — experiments built-in!)

---

## 📖 5-Line Summary

1. **Iteration** = ek-ek item utha ke chalna (koi bhi loop, explicit ya implicit). **Iterator** 🎬 = memory me POORA store kiye bina sequence traverse karne wala object; **iterable** 📦 = object jo `iter()` pe iterator deta hai (list/tuple/dict/set/str/range…).
2. **2 Rules** ⚖️: har iterator iterable HAI, par har iterable iterator NAHI. **Trick** 🔍: iterable ke paas `__iter__`, iterator ke paas `__iter__` + `__next__` — `dir(obj)` se pakdo!
3. **`for` loop ka secret** 🔓 = `iter()` + `next()` + `StopIteration` — Python for-loop ko 3 lines me khud bana sakte ho (`mera_khudka_for_loop`). `iter(iterator)` wapas WAHI iterator deta hai (same `id`)!
4. **Generator** ✨ = `yield` wala function jo bina finish hue values wapas deta hai; class-pair (iterable+iterator) ka 4-line mauka. **Memory bomb** 💣: list `range(100000)` ≈ 800,984 bytes vs genexp ≈ 200 bytes!
5. **Bonus** 🎁: Namespaces + Decorators — LEGB rule, `global`/`nonlocal`, first-class functions, `@decorator` wrapper pattern, `@timer` timing, decorator-arguments (factory→decorator→wrapper).

## 🌍 Analogy Corner

| Concept | Real life |
|---|---|
| iterable 📦 | paan-dabba — andar hi list hai, magar khud item nahi dega |
| iterator 🎬 | cinema wala usher — ek-ek seat(row) dikhata hai, sab seat memory me nahi |
| `next()` 🚦 | token machine — ek baar me ek number, bar-bar dabao |
| `StopIteration` 🛑 | bank ka "last customer" signboard — ab khatam |
| lazy generator ⏳ | nai-nai chai — jab mango tab banao, sab pehle se nahi |
| generator vs list 💾 | dukaan ka godown (sab stock) vs kitchen-order (jamna jamna on demand) |
| namespace 🗂️ | almirah ke labels — name ka object pata karo |
| decorator 🎀 | gift-wrap — function ki power wahi, upar decoration + processing |

## 📁 Files Is Folder Me

| File | Kya hai |
|---|---|
| `Iterators.ipynb` | Iteration/Iterator/Iterable defs, memory-showdown (list vs range), `iter()`+`dir()` trick, for-loop ka desugar, `mera_khudka_for_loop`, `iter(iterator)` self-return, khud ka `range()` (mera_range + mera_range_iterator classes) |
| `generators-demo.ipynb` | Class-boilerplate vs generator, `yield` vs `return`, gen dhaas `square()`, mera_range as generator, generator expressions `(i**2 for ...)`, lazy image-reader, 4 benefits (ease/Memory💾/infinite-streams/chaining) — fibonacci+square sum = 4895 |
| `Namespaces_decorators.ipynb` | 4 namespaces + LEGB, `global` vs `nonlocal`, first-class functions, manual wrapper, `@` syntax, `@timer`, decorator-with-arguments (`sanity_check(int)` famous interview pattern) |

## 🧾 Cheat Sheet

```python
# ITERATION CORE
iter(iterable)      # iterable -> iterator  (e.g. iter([1,2,3]))
next(iterator)      # ek value aage badho;  khatam -> StopIteration
list(iterator) / for i in it: ...   # consume the lazy stream

# EVERY iterator is iterable, but NOT every iterable is iterator!
dir(obj)            # '__iter__' + '__next__' -> iterator hai pakka 📍

# for-loop desugar (Python asli me yehi karta hai):
it = iter(seq)
while True:
    try:
        x = next(it)
    except StopIteration:
        break

# GENERATOR: function + yield
def mera_range(start, end):
    for i in range(start, end):
        yield i

gen = (i**2 for i in range(1, 101))   # generator EXPRESSION (lazy!)
sum(square(fibonacci_numbers(10)))    # chain generators ⛓️
# list = store-sab-memory 💣 | gen = banao-jab-chahiye 💾

# SCOPE / NAMESPACE / DECORATOR
# LEGB: Local -> Enclosing -> Global -> Built-in (name search order)
global a    # function ke andar global ko badlo
nonlocal a  # nested function me enclosing ko badlo
import builtins; dir(builtins)   # built-in scope dikho

def my_decorator(func):
    def wrapper():
        print('****'); func(); print('****')
    return wrapper
@my_decorator                     # sugar of: hello = my_decorator(hello)
def hello(): print('hello')

def sanity_check(data_type):      # decorator WITH arguments
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type: func(*args)
            else: raise TypeError(...)
        return inner_wrapper
    return outer_wrapper
@sanity_check(int)
def square(num): print(num**2)
```

## 📊 Live-facts (executed notebooks ✅)

- `sys.getsizeof(L)/64` list `range(1,10000)` ≈ **1330.875** vs range-object ≈ **0.75** 😱 — sequence type matters!
- `type(iter([1,2,3]))` → `list_iterator` — iterable nahi, ITERATOR hai.
- `iter(iter_obj)` → **SAME `id()`** (2369496748704 = 2369496748704) — iterator apna hi iterator.
- Generator `square(10)`: `next`×3 = 1,4,9 — phir `for` baaki 16…100 (state yaad! 📍)
- `mera_range(15,26)` generator ✅ 15→25; `genexp 1..100` squares ✅
- Memory: list 100k ≈ **800,984 B** vs genexp ≈ **200 B** 💾
- `sum(square(fibonacci_numbers(10)))` = **4895**
- `global a` fix: a=2 → `a+=1` inside → 3,3 ✅ ; `nonlocal` inner 2 / outer 2 ✅
- Decorator `@timer`: hello 2.0007s · square 1.0013s · power ~0.000025s
- `@sanity_check(int) square(2)` → 4 ✅ (wrong-type → `TypeError`)

## ⚠️ 5 Common Mistakes

| # | ❌ Galti | ✅ Sahi |
|---|---|---|
| 1 | Iterator ko 2 baar loop karna (2nd pass empty🤫) | fresh `iter()` lo — ek-baar-wala hafte me shop |
| 2 | `for i in range(len(x))` iterables dekhne ke liye | `enumerate(x)` / direct `for i in x` |
| 3 | Generator ko full list ki tarah entha lena (`indexing`) | `next()` / `for` / `list(gen)` — wahi available |
| 4 | `global`/`nonlocal` bhool ke variable REBIND karna (UnboundLocalError) | explicit `global a` / `nonlocal a` |
| 5 | Decorator me `*args` miss karna (arguments wali function fat-ti) | wrapper me `def wrapper(*args, **kwargs): func(*args, **kwargs)` |

## ⏭️ Aage Kya?

**Topic 03.02 — `Zip_Enumerate_Map_Filter_Reduce`** 🔗 — factory-tools quartet:
`zip(a,b)` teeth-interlock, `enumerate` queue-token, `map` spray-paint, `filter`
quality-gate, `reduce` rolling-blender — pythonic pipelines ka asli arsenal,
students_marks + products_catalog lab ke saath! 👑