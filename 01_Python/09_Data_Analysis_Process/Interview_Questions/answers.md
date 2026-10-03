# Data Analysis Process - model answers

Crisp answers matched to [`questions.md`](questions.md). Say the first sentence in an interview, then expand only if asked.

## Easy

**1. What are the stages of the data analysis process?**

Frame the question, gather data, assess quality, clean, explore, analyse, and communicate the result.

**2. What is EDA?**

Exploratory data analysis: summarising and visualising a dataset to understand its structure, relationships and defects before modelling.

**3. What is the difference between quality and tidiness issues?**

Quality is about wrong content - nulls, bad values, duplicates. Tidiness is about wrong structure - variables in rows, multiple values in one cell.

**4. Name the dimensions of data quality.**

Completeness, validity, accuracy, consistency, uniqueness and timeliness.

**5. What is univariate analysis?**

Examining one variable at a time: its distribution, centre, spread and missingness.

**6. Why assess before cleaning?**

So every defect is catalogued and no fix is forgotten or applied twice. It also produces the audit trail reviewers ask for.

**7. What makes data tidy?**

Each variable is a column, each observation is a row, and each observational unit forms its own table.

**8. What is a data dictionary?**

A document defining every column: meaning, type, unit, allowed values and source. It prevents two people computing the same metric differently.

**9. What is the first thing you do with a new dataset?**

Check shape, dtypes, nulls, duplicates and a sample of actual rows, before forming any opinion about it.

**10. Why keep the raw data immutable?**

So every derived result is reproducible from a known starting point, and a cleaning mistake is always recoverable.

## Medium

**11. How do you decide whether to drop or impute missing values?**

By mechanism and volume: if data is missing completely at random and the share is small, dropping is safe. Otherwise impute, and add an indicator column so the model can use the missingness itself.

**12. What is the difference between MCAR, MAR and MNAR?**

Missing completely at random depends on nothing; missing at random depends on observed variables; missing not at random depends on the unobserved value itself, which is the dangerous case.

**13. How do you detect outliers?**

IQR fences, z-scores, isolation forests, or domain rules. Statistical detection only flags candidates; domain knowledge decides.

**14. Should you always remove outliers?**

No. Remove only provable errors. Cap or transform distorting-but-real values, and keep them when the extremes are the phenomenon you study.

**15. What is data leakage in the analysis stage?**

Letting information from the test period or the target influence preprocessing - fitting a scaler or imputer on the full dataset is the classic case.

**16. How do you validate a cleaning pipeline?**

Assert on the output: row counts, uniqueness, dtypes, value ranges and null rates. Run those assertions on every future refresh.

**17. What is Simpson's paradox?**

A trend present in each subgroup that reverses when the groups are pooled, caused by an unbalanced confounder.

**18. How do you handle duplicate records that are not identical?**

Normalise the key fields (case, whitespace, formatting), then match on the normalised key or use fuzzy matching with a reviewed threshold.

**19. How do you report a result you are not confident in?**

State the estimate, the interval, the assumptions and what would change your mind. Confidence is a property of the evidence, not the presenter.

**20. What is the role of a baseline in analysis?**

It is the number your result must beat to be interesting - last period, the majority class, or the current process.

## Hard

**21. How would you design a data quality monitoring system?**

Codify expectations as testable rules on every load: schema, null rates, ranges, referential integrity, row-count deltas against a trailing median. Alert on violations, version the rules, and record every result so quality itself becomes a time series.

**22. How do you analyse an experiment that was not randomised?**

Use a quasi-experimental design: difference in differences, matching or synthetic control. State the identifying assumption explicitly and test it with a pre-treatment parallel-trends check.

**23. A stakeholder disputes your numbers. How do you respond?**

Reconcile definitions first - most disputes are metric mismatches, not arithmetic errors. Reproduce both numbers from raw data, show the divergence point, and agree one definition going forward.

**24. How do you analyse a dataset too large for memory?**

Chunked reads with aggregation, columnar formats such as Parquet, a query engine like DuckDB, or pushing the aggregation into the warehouse. Sample for exploration, use the full data only for the final number.

**25. How do you quantify the business impact of an analysis?**

Tie the finding to a decision and a monetary or user-facing quantity, with a stated counterfactual. 'Reallocating spend from web/south saves X per month if the observed gap persists' beats a correlation coefficient.

**26. Explain survivorship bias with a concrete example.**

Analysing only current customers to learn what drives retention: the churned users who would explain it are absent from the sample, so every conclusion is conditioned on having survived.

**27. How do you decide when the analysis is finished?**

When the framed question is answered to the agreed precision and further work would not change the decision. Define that stopping rule before you start.

**28. How do you handle conflicting data sources?**

Establish a single source of truth per metric, document the lineage, quantify the discrepancy, and investigate its mechanism rather than averaging it away.

**29. What is p-hacking and how do you guard against it?**

Searching many hypotheses and reporting only significant ones. Guard with a pre-registered hypothesis, multiple-comparison correction, and holding out a confirmation sample.

**30. How would you structure an analysis repository for reproducibility?**

Immutable raw data, numbered notebooks for narrative, importable modules for logic, a pinned environment, seeds fixed, parameters in a config file, and a single command that regenerates every output.
