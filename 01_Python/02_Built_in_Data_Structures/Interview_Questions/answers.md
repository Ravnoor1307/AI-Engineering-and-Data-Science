# Python Data Types - model answers

Crisp answers matched to [`questions.md`](questions.md). Say the first sentence in an interview, then expand only if asked.

## Easy

**1. What is the difference between a list and a set?**

Lists are ordered and allow duplicates; sets are unordered, deduplicated and require hashable members, giving O(1) membership tests.

**2. When would you use a tuple over a list?**

For fixed-size records, for dict keys, and anywhere immutability documents intent or prevents accidental mutation.

**3. Are dictionaries ordered?**

Yes, insertion order is guaranteed from Python 3.7. Do not confuse that with sorted order.

**4. What makes an object hashable?**

A stable `__hash__` and consistent `__eq__`. Immutable built-ins qualify; lists, dicts and sets do not.

**5. How do you remove duplicates from a list?**

`list(set(x))` when order does not matter; `list(dict.fromkeys(x))` when it does.

**6. What does `dict.get` do differently from `dict[key]`?**

`get` returns a default (None) instead of raising KeyError, which is useful when absence is normal.

**7. What is a shallow copy?**

A new outer container holding the same inner references, so mutating a nested object is visible through both copies.

**8. What is a list comprehension?**

An expression that builds a list by mapping and filtering an iterable, faster and clearer than an append loop.

**9. How do you merge two dictionaries?**

`a | b` in 3.9+, or `{**a, **b}`. The right operand wins on key conflicts.

**10. What does `*args` mean?**

It collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict.

## Medium

**11. Why can a tuple be a dict key but not a list?**

Dict keys must be hashable and hashes must not change. Lists are mutable, so their hash would be unstable; tuples of hashables are fine.

**12. Explain the time complexity of common list operations.**

Index O(1), append amortised O(1), insert/pop at front O(n), membership O(n), sort O(n log n).

**13. What is `collections.defaultdict` good for?**

Grouping and counting without a key-existence check: the factory supplies a default on first access.

**14. Difference between `del`, `remove` and `pop`?**

`del` removes by index or slice, `remove` removes the first matching value, `pop` removes by index and returns the item.

**15. How do sets handle unhashable items?**

They raise TypeError. Convert to a tuple, or use a frozenset for nested set-like members.

**16. What is a generator expression versus a list comprehension?**

A generator is lazy and memory-constant; a comprehension materialises the whole list. Use a generator when feeding an aggregate like `sum`.

**17. Explain dict comprehension with a condition.**

`{k: v for k, v in items if cond}` builds a filtered mapping in one pass without an intermediate list.

**18. Why is `list.insert(0, x)` in a loop a red flag?**

Each insert shifts every element, making the loop O(n^2). Use `collections.deque.appendleft`, or append and reverse at the end.

**19. What is the difference between `sort` and `sorted`?**

`sort` mutates a list in place and returns None; `sorted` accepts any iterable and returns a new list.

**20. How does `key=` differ from `cmp` style sorting?**

`key` computes a sort value once per element (a Schwartzian transform), which is O(n) calls instead of O(n log n) comparisons.

## Hard

**21. How is a Python dict implemented?**

An open-addressing hash table with a compact index array plus a dense entries array, which is what makes insertion order free.

**22. What is a hash collision and how does dict handle it?**

Two keys landing in the same slot. CPython probes a pseudo-random sequence of slots until a free one is found, comparing by identity then equality.

**23. Explain memory overhead of a list of a million integers.**

The list holds 8-byte pointers plus over-allocation, while each int is a 28-byte object. A NumPy int64 array holds the same data in 8 MB contiguous.

**24. Why might set iteration order differ between runs?**

String hashes are randomised per process by default (PYTHONHASHSEED) to mitigate collision attacks, so never depend on set order.

**25. What is `__slots__` and when does it help?**

It replaces a class instance `__dict__` with a fixed descriptor layout, cutting memory substantially when you create millions of small objects.

**26. How do you make a custom class usable as a dict key?**

Implement `__hash__` and `__eq__` consistently over the same immutable fields, or use a frozen dataclass which generates both.

**27. Explain the difference between `frozenset` and `set`.**

`frozenset` is immutable and therefore hashable, so it can be a member of another set or a dict key.

**28. What happens when you mutate a list while iterating it?**

The iterator's index-based cursor skips or repeats elements. Iterate a copy, or build a new list with a comprehension.

**29. Describe how `functools.lru_cache` interacts with argument types.**

Arguments must be hashable because they form the cache key; passing a list raises TypeError. Convert to a tuple first.

**30. When is a list of tuples better than a dict?**

When you need duplicate keys, order-sensitive pairs, or cheap sequential scanning rather than random lookup.
