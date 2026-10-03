# Python Advanced - model answers

Crisp answers matched to [`questions.md`](questions.md). Say the first sentence in an interview, then expand only if asked.

## Easy

**1. What is a class versus an instance?**

A class is the template describing state and behaviour; an instance is one concrete object built from it with its own attributes.

**2. What does `self` refer to?**

The instance the method was called on, passed implicitly by the descriptor protocol when you call `obj.method()`.

**3. What is `__init__`?**

The initialiser, run after `__new__` creates the object. It sets up instance state and must return None.

**4. Why use `with open(...)`?**

The context manager closes the file on both normal and exceptional exit, preventing descriptor leaks and partial writes.

**5. What is a decorator?**

A callable that takes a function and returns a replacement, used for cross-cutting behaviour such as timing, caching or auth.

**6. What does `yield` do?**

It suspends the function, hands a value to the caller, and resumes from the same point on the next iteration.

**7. Difference between `str` and `repr`?**

`str` is the friendly form for users; `repr` is the unambiguous developer form and ideally is valid Python.

**8. What is inheritance?**

A mechanism where a subclass reuses and extends a parent class, resolved through the method resolution order.

**9. When do you use `try/finally`?**

When cleanup must happen regardless of success: closing files, releasing locks, restoring state.

**10. What is a custom exception?**

A user-defined class inheriting from Exception so callers can catch your domain failures specifically.

## Medium

**11. Difference between `@staticmethod` and `@classmethod`?**

A classmethod receives the class as `cls` and is the idiomatic alternative constructor; a staticmethod receives nothing and is a namespaced function.

**12. What is the MRO?**

Method Resolution Order, computed by C3 linearisation, determining which parent implementation `super()` reaches under multiple inheritance.

**13. How does a generator differ from a list in memory?**

A generator holds only its frame state, a few hundred bytes, while a list materialises every element.

**14. What does `functools.wraps` fix?**

Without it the wrapper replaces `__name__`, `__doc__` and `__wrapped__`, breaking introspection, help() and some frameworks.

**15. When prefer composition to inheritance?**

When the relation is 'has a', when you must swap the collaborator at runtime, or when inheritance would expose parent internals.

**16. Explain `__enter__` and `__exit__`.**

They implement the context manager protocol. `__exit__` receives exception details, and returning True suppresses the exception.

**17. Difference between `raise` and `raise ... from`?**

`from` sets `__cause__`, so the traceback shows the original error as the explicit cause rather than an incidental one.

**18. What is a closure and why does it matter?**

A nested function capturing variables from the enclosing scope, keeping them alive after the outer call returns. It underpins decorators.

**19. How do you make a class iterable?**

Implement `__iter__` returning an iterator, or `__getitem__` with integer indexing for the legacy protocol.

**20. What is `yield from`?**

It delegates to a sub-generator, forwarding values, sends and exceptions, and returns the sub-generator's return value.

## Hard

**21. How do stacked decorators apply?**

Bottom up: the decorator nearest the def wraps first, and the topmost wrapper is what the name ends up bound to.

**22. What is a metaclass?**

The class of a class, controlling class creation. `type` is the default; frameworks use custom metaclasses for registration and validation.

**23. How does `__slots__` change attribute lookup?**

Attributes become class-level descriptors with fixed storage, removing the per-instance dict and cutting memory, at the cost of dynamic attributes.

**24. Explain generator `send()`.**

`send(value)` resumes the generator, making the paused `yield` expression evaluate to that value. It is the mechanism underneath older coroutines.

**25. What are descriptors?**

Objects implementing `__get__`/`__set__`, the protocol behind properties, methods, classmethod and staticmethod.

**26. How does garbage collection handle reference cycles?**

Reference counting cannot free cycles, so a generational cycle collector periodically traces and reclaims them.

**27. Why can a decorator break pickling?**

Pickle stores a qualified name; a nested wrapper with a different qualname fails lookup on load. `functools.wraps` mitigates part of this.

**28. Iterator versus iterable?**

An iterable produces an iterator via `__iter__`; an iterator also implements `__next__` and is consumed exactly once.

**29. Explain context manager suppression semantics.**

A truthy return from `__exit__` swallows the exception - the mechanism behind `contextlib.suppress`, and a common accidental bug.

**30. How would you implement `lru_cache` yourself?**

A dict keyed on the hashable argument tuple plus an OrderedDict for recency, evicting the least recently used entry on overflow.
