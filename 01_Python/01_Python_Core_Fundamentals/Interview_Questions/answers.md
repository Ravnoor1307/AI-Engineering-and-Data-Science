# Python Basics - model answers

Crisp answers matched to [`questions.md`](questions.md). Say the first sentence in an interview, then expand only if asked.

## Easy

**1. What is the difference between a list and a tuple?**

Lists are mutable and use more memory; tuples are immutable, hashable when their contents are, and can serve as dictionary keys.

**2. Is Python interpreted or compiled?**

Source is compiled to bytecode, which the CPython virtual machine interprets. So: both, with the compilation step hidden.

**3. What does dynamic typing mean?**

Types belong to objects, not names. A name can be rebound to an object of any type, and type errors surface at runtime.

**4. What is the difference between `is` and `==`?**

`==` compares values via `__eq__`; `is` compares identity (memory address). Use `is` only with `None`, `True`, `False` and sentinels.

**5. Why does `0.1 + 0.2 != 0.3`?**

Floats are binary approximations of decimal fractions. Compare with `math.isclose`, or use `decimal.Decimal` for money.

**6. What is PEP 8?**

The style guide for Python code: 4-space indents, snake_case for functions and variables, PascalCase for classes, 79-99 character lines.

**7. What are f-strings?**

Literal string interpolation introduced in 3.6: `f'{x:.2f}'`. They are evaluated at runtime, are the fastest formatting option, and support `{x=}` for debugging.

**8. What is the difference between `/` and `//`?**

`/` is true division returning a float; `//` is floor division returning the largest integer less than or equal to the quotient.

**9. How do you swap two variables?**

`a, b = b, a`. The right side is packed into a tuple first, so no temporary variable is needed.

**10. What does `range(2, 10, 3)` produce?**

A lazy sequence yielding 2, 5, 8. The stop value is exclusive and the object stores only start, stop and step.

## Medium

**11. Explain short-circuit evaluation.**

`and` returns the first falsy operand, `or` the first truthy one, and neither evaluates the right side unnecessarily. This allows guards like `if items and items[0]`.

**12. What is the `for ... else` construct?**

The `else` block runs only if the loop finished without `break`. It is the cleanest way to express 'searched everything and found nothing'.

**13. How does string immutability affect performance?**

Repeated concatenation in a loop is O(n^2) because each step copies. Build a list and `''.join()` it instead, which is O(n).

**14. What is the difference between `find` and `index`?**

`find` returns -1 when the substring is absent; `index` raises ValueError. Use `find` when absence is expected, `index` when it is a bug.

**15. Explain the walrus operator.**

`:=` assigns inside an expression: `while (line := f.readline()):`. It removes duplicated calls but should be used sparingly for readability.

**16. What is the difference between `str` and `bytes`?**

`str` is a sequence of Unicode code points; `bytes` is raw storage. `encode()` and `decode()` convert, and the encoding must match the source.

**17. How does Python handle integer overflow?**

It does not overflow - `int` grows to arbitrary precision limited only by memory. NumPy integers, by contrast, are fixed width and do wrap.

**18. What is the `match` statement?**

Structural pattern matching from Python 3.10. It matches shape as well as value, supports guards and capture patterns, and is not a C-style switch.

**19. Why is mutable default argument a trap?**

The default is evaluated once at definition time, so a shared list persists across calls. Use `None` as the default and create the list inside.

**20. Explain operator precedence for `-3 ** 2`.**

Exponentiation binds tighter than unary minus, so this is `-(3 ** 2)` = -9.

## Hard

**21. How does CPython's small-integer cache affect `is`?**

Integers from -5 to 256 are interned singletons, so `256 is 256` is True but `257 is 257` may be False outside a single compilation unit. Never rely on it.

**22. What is string interning and when does it happen?**

Identifier-like string literals are interned at compile time to speed up dictionary lookups. `sys.intern` forces it. Comparison semantics should never depend on it.

**23. Explain the GIL's impact on CPU-bound loops.**

Only one thread executes bytecode at a time, so threads do not speed up CPU-bound Python. Use `multiprocessing`, or push the work into NumPy/C extensions that release the lock.

**24. Why is `sum()` slow for large numeric arrays?**

It iterates Python objects with per-element dispatch. `np.sum` runs a tight C loop over contiguous memory, typically 20-100x faster.

**25. What does `sys.getsizeof` actually measure?**

The shallow size of the object itself, excluding referenced objects. A list of a million ints reports only the pointer array, not the ints.

**26. How would you profile a slow script?**

`cProfile` for function-level costs, `line_profiler` for hot lines, `timeit` for micro-benchmarks, and `tracemalloc` for memory. Measure before you optimise.

**27. Explain how `round()` breaks ties.**

Banker's rounding: ties go to the nearest even value, so `round(0.5) == 0` and `round(1.5) == 2`. This reduces bias in aggregates.

**28. What happens at import time versus call time?**

Module-level code runs once on first import and its result is cached in `sys.modules`. Default arguments, decorators and class bodies all execute at import time.

**29. How do you make a script both importable and runnable?**

Guard the entry point with `if __name__ == '__main__':` so importing the module does not trigger side effects.

**30. Describe the memory model behind `a = b = []`.**

Both names bind to a single list object, so mutating through one name is visible through the other. Copy explicitly with `list(b)` when that is not what you want.
