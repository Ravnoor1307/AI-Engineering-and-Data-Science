# NumPy - model answers

Crisp answers matched to [`questions.md`](questions.md). Say the first sentence in an interview, then expand only if asked.

## Easy

**1. What is an ndarray?**

A fixed-type, N-dimensional array stored in contiguous memory with a shape and strides, which is why elementwise operations run at C speed.

**2. How does a NumPy array differ from a Python list?**

The array is homogeneous, contiguous and compact; a list holds pointers to boxed objects and cannot be vectorised.

**3. What is dtype?**

The element type of an array, fixed at creation. It determines memory use, precision and overflow behaviour.

**4. What does shape mean?**

A tuple giving the size along each dimension; its product is the number of elements.

**5. How do you create an array of zeros?**

`np.zeros(shape, dtype=...)`, with `np.ones`, `np.full` and `np.empty` as siblings.

**6. What does reshape do?**

It returns a new view with a different shape and the same data, as long as the total element count is unchanged.

**7. What is axis 0 versus axis 1?**

Axis 0 runs down the rows and axis 1 across the columns, so `sum(axis=0)` gives one total per column.

**8. How do you find the maximum of an array?**

`arr.max()` for the value and `arr.argmax()` for the flat index of it.

**9. What is elementwise multiplication versus matrix multiplication?**

`a * b` multiplies elementwise; `a @ b` or `np.dot` performs matrix multiplication.

**10. What does np.linspace do?**

It returns evenly spaced numbers over an interval, inclusive of the endpoint by default, unlike arange.

## Medium

**11. Explain broadcasting.**

Shapes are aligned from the trailing dimension; each pair must be equal or one of them must be 1, and size-1 dimensions are virtually repeated without copying data.

**12. View versus copy - how do you tell?**

Basic slicing gives a view sharing memory, fancy and boolean indexing give copies. Check `arr.base` or use `np.shares_memory`.

**13. Why is NumPy faster than a Python loop?**

Contiguous typed memory, no per-element boxing, C loops, and SIMD vectorisation in the underlying BLAS.

**14. What is a ufunc?**

A universal function applying an operation elementwise in compiled code, with broadcasting plus `out=` and `where=` support.

**15. How do you handle NaN in aggregation?**

Use nan-aware functions such as `np.nanmean` and `np.nansum`, since a single NaN poisons an ordinary reduction.

**16. What does np.where do?**

Vectorised conditional selection returning a new array, or with one argument the indices where the condition holds.

**17. Explain strides.**

The byte step to move one element along each axis. Transposes and slices change strides without copying data.

**18. How do you concatenate arrays?**

`np.concatenate` along an existing axis, or `vstack`/`hstack`/`stack` for common cases; stack adds a new axis.

**19. When should you use int32 over int64?**

When values fit and the array is large - it halves memory and improves cache behaviour, at the cost of overflow risk.

**20. What is np.random.default_rng?**

The modern generator API with better statistical properties and explicit state, replacing the legacy global `np.random.seed` functions.

## Hard

**21. Explain memory layout, C order versus Fortran order.**

C order stores rows contiguously, Fortran order stores columns. Iterating against the layout causes cache misses and can be several times slower.

**22. How would you compute pairwise distances for a million points?**

Not with an n-squared broadcast, which needs terabytes. Use chunking, a KD tree or a library such as FAISS, and exploit the expanded squared norm formula to reuse dot products.

**23. What is np.einsum and when is it worth it?**

A concise notation for sums over index products. It fuses transposes and reductions into one pass, avoiding intermediate arrays.

**24. Explain how NumPy handles integer overflow.**

Fixed-width integers wrap silently, unlike Python ints. Guard with a wider dtype or explicit range checks before aggregation.

**25. What is a structured array?**

An array with a compound dtype of named fields, giving a record-like layout in one contiguous block. Pandas usually serves the purpose better.

**26. How do masked arrays differ from NaN?**

`np.ma` tracks validity in a separate boolean mask, so integer arrays can carry missing values, which NaN cannot express.

**27. What causes a copy you did not expect?**

Fancy indexing, non-contiguous slicing followed by reshape, dtype promotion, and functions with no `out=` parameter.

**28. Explain the relationship between NumPy and BLAS.**

Linear algebra calls are dispatched to an optimised BLAS/LAPACK library such as OpenBLAS or MKL, which supplies the multithreaded kernels.

**29. How do you profile memory in a NumPy pipeline?**

Track `nbytes` per array, prefer in-place ufuncs with `out=`, delete intermediates, use memory-mapped arrays for data larger than RAM.

**30. What is np.memmap for?**

Mapping an on-disk array into memory so slices are paged in on demand, letting you work with files larger than RAM.
