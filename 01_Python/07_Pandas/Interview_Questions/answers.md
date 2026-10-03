# Pandas - model answers

Crisp answers matched to [`questions.md`](questions.md). Say the first sentence in an interview, then expand only if asked.

## Easy

**1. What is a DataFrame?**

A two-dimensional labelled table of columns, each a Series with its own dtype, all sharing one row index.

**2. Difference between loc and iloc?**

loc selects by label and includes the stop; iloc selects by integer position and excludes the stop.

**3. How do you read a CSV?**

`pd.read_csv(path)`, with dtype, parse_dates, usecols and nrows as the arguments worth knowing early.

**4. What does head() do?**

Returns the first n rows, five by default - the fastest sanity check after loading data.

**5. How do you check for missing values?**

`df.isna().sum()` per column, or `df.isna().mean()` for the proportion.

**6. What is value_counts?**

A Series method counting occurrences of each distinct value, with normalize=True for proportions.

**7. How do you drop a column?**

`df.drop(columns=['a'])`, which returns a new frame unless inplace is set.

**8. What does describe() show?**

Count, mean, standard deviation, min, quartiles and max for numeric columns.

**9. How do you rename columns?**

`df.rename(columns={'old': 'new'})`, or assign a full list to df.columns.

**10. What is the index?**

The row labels. It powers alignment, fast lookup and time series functionality.

## Medium

**11. Explain split-apply-combine.**

groupby splits rows by key, a function is applied to each group, and the results are combined. agg reduces, transform preserves shape, filter selects whole groups.

**12. Difference between merge and join?**

merge is the general key-based function mirroring SQL joins; join is a convenience method that defaults to joining on the index.

**13. What is SettingWithCopyWarning?**

Pandas cannot tell whether you are writing to a view or a copy. Fix it by using a single .loc assignment or an explicit .copy().

**14. How do you optimise memory in pandas?**

Convert repeated strings to category, downcast numerics, load only needed columns, and read in chunks for large files.

**15. What does apply do and why avoid it?**

It runs a Python function per row or column, which is a loop in disguise. Prefer vectorised operations or groupby aggregations.

**16. Explain pivot_table versus pivot.**

pivot requires unique index-column pairs; pivot_table aggregates duplicates with a function and can add margins.

**17. How do you handle duplicate rows?**

Define uniqueness first, then `drop_duplicates(subset=..., keep=...)`. Count with duplicated() before deleting anything.

**18. What is method chaining and why is it useful?**

Composing operations in one expression with assign, query and pipe, which avoids intermediate variables and accidental mutation.

**19. How do you resample a time series?**

With a DatetimeIndex, `resample('ME').sum()` aggregates by period; rolling computes moving windows.

**20. Difference between concat and merge?**

concat stacks frames along an axis by alignment of the other axis; merge joins on key values.

## Hard

**21. How does pandas store data internally?**

In a BlockManager that groups columns of the same dtype into 2-D blocks. This is why adding a column of a new dtype can trigger a copy.

**22. Why can groupby.apply be slow?**

It materialises a sub-frame per group and calls Python for each. Built-in aggregations dispatch to Cython and are far faster.

**23. Explain copy-on-write in recent pandas.**

Assignments no longer propagate to parents through views; pandas defers the copy until a write happens, removing SettingWithCopy ambiguity.

**24. How would you process a 50 GB CSV?**

Chunked reading with an aggregation per chunk, or switch to Parquet with column pruning, or use Dask, Polars or DuckDB for out-of-core execution.

**25. What is a MultiIndex and when is it worth it?**

A hierarchical index enabling grouped selection and cross-sections. Useful for panel data, but flatten it before handing data to most model APIs.

**26. Explain the difference between NaN, None and pd.NA.**

NaN is a float sentinel, None is a Python object, pd.NA is the dtype-agnostic missing marker used by nullable extension dtypes.

**27. How do you make a pandas pipeline reproducible?**

Pin versions, fix random seeds, express steps as pure functions composed with pipe, and validate schema and row counts with assertions.

**28. What is the cost of a merge and how do you speed it up?**

Roughly hash-join cost plus the output size. Speed it by joining on indexed, narrow, correctly-typed keys and by filtering before joining.

**29. When would you choose Polars or DuckDB over pandas?**

For larger-than-memory data, multi-threaded execution, or SQL-style analytics where a lazy query optimiser beats eager row-by-row pandas.

**30. How do you detect data drift between two snapshots?**

Compare schema, null rates, cardinality and distribution statistics per column, and run a test such as Kolmogorov-Smirnov on numeric fields.
