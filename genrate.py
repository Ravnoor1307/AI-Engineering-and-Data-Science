
from pathlib import Path
import importlib.util
import subprocess
import sys

if importlib.util.find_spec("nbformat") is None:
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "nbformat"
    ])

import nbformat as nbf

ROOT = Path("D:/GENAI/AI-Engineering-Foundations")
NOTEBOOK_PATH = (
    ROOT
    / "02-SQL-Databases"
    / "SQL_Databases_Complete.ipynb"
)

if not NOTEBOOK_PATH.exists():
    raise FileNotFoundError(
        f"Notebook not found:\n{NOTEBOOK_PATH}\n"
        "Parts 1-10 must exist before Part 11 is appended."
    )

nb = nbf.read(NOTEBOOK_PATH, as_version=4)


def md(text):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text):
    return nbf.v4.new_code_cell(text.strip())


def heading_locations(notebook, heading):
    locations = []

    for index, cell in enumerate(notebook.cells):
        if cell.cell_type != "markdown":
            continue

        source = cell.source.strip()

        if not source:
            continue

        first_line = source.splitlines()[0].strip()

        if first_line == heading:
            locations.append(index)

    return locations


required_markers = [
    "# SQL and Relational Database Engineering",
    "# Querying Data with SELECT",
    "# Aggregation and Grouped Analysis",
    "# Joining Relational Data",
    "# Subqueries, Common Table Expressions, and Set Operations",
    "# SQL Window Functions",
    "# Data Modification and Transaction Engineering",
    "# Indexes, Query Plans, and SQL Performance Engineering",
    "# Schema Design, Normalization, and Data Modeling",
    "# Production Database Features and Operational Engineering",
]

for marker in required_markers:
    locations = heading_locations(nb, marker)

    if len(locations) != 1:
        raise RuntimeError(
            f"Expected exactly one prior section {marker!r}, "
            f"but found {len(locations)} at {locations}."
        )


PART11 = "# Advanced SQL Patterns and Data Pipeline Engineering"

existing = heading_locations(nb, PART11)

if existing:
    raise RuntimeError(
        f"Part 11 already exists at {existing}. "
        "Aborting to prevent duplicate content."
    )

start_count = len(nb.cells)
cells = []


cells.append(md(r"""
# Advanced SQL Patterns and Data Pipeline Engineering

The previous sections developed SQL from relational foundations through querying, aggregation, joins, subqueries, window functions, transactions, indexing, modeling, and production database architecture.

This section integrates those ideas into patterns commonly found in analytics, data engineering, product systems, and AI pipelines.

The difficulty of advanced SQL is usually not syntax alone.

The difficult questions are often:

- What is the grain of the source data?
- What exactly is the metric?
- Which event counts as the first event?
- Which timestamp should define the cohort?
- Can the same entity appear more than once?
- Are late-arriving rows possible?
- Is the transformation idempotent?
- Is the pipeline using event time or ingestion time?
- Can historical data change after it was processed?
- Is the feature point-in-time correct?
- Can the query be tested automatically?
- What happens when the pipeline is rerun?

We will study:

- reusable analytical query structure
- cohort analysis
- retention analysis
- funnel analysis
- ordered funnels
- deduplication
- latest-row patterns
- gaps and islands
- streak analysis
- relational division awareness
- conditional pivoting
- pivot/unpivot awareness
- dynamic SQL awareness
- JSON in SQL
- full-text-search awareness
- temporal/history modeling
- effective-dated records
- audit tables
- snapshot versus event data
- ETL
- ELT
- staging layers
- incremental processing
- high-water marks
- compound watermarks
- late-arriving data
- lookback windows
- idempotency
- batch identifiers
- merge/upsert concepts
- change data capture awareness
- soft deletes in pipelines
- data-quality checks
- SQL assertions
- SQL testing
- reconciliation
- maintainable SQL style
- lineage and provenance
- feature pipeline patterns
- label leakage
- point-in-time features
- end-to-end SQL pipeline architecture

The central principle is:

> Advanced SQL engineering is the design of correct, reproducible transformations over changing data—not merely writing complicated queries.
"""))


cells.append(md(r"""
# Building an Integration Laboratory

We will create a dedicated SQLite database containing:

- users
- product events
- subscriptions
- historical customer tiers
- ingestion batches

The data is deliberately small enough to inspect manually while containing enough structure to demonstrate advanced analytical patterns.

These examples are educational. Production schemas and SQL syntax can differ substantially between SQLite, PostgreSQL, MySQL, warehouses, and distributed analytical systems.
"""))


cells.append(code(r'''
import sqlite3
import pandas as pd
from IPython.display import display

adv_conn = sqlite3.connect(":memory:")
adv_conn.execute("PRAGMA foreign_keys = ON")

adv_conn.executescript("""
CREATE TABLE app_users_adv (
    user_id INTEGER PRIMARY KEY,
    signup_date TEXT NOT NULL,
    region TEXT NOT NULL
);

CREATE TABLE product_events_adv (
    event_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    event_time TEXT NOT NULL,
    event_name TEXT NOT NULL,
    ingestion_time TEXT NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES app_users_adv(user_id)
);

CREATE TABLE subscriptions_adv (
    subscription_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    started_at TEXT NOT NULL,
    ended_at TEXT,
    plan TEXT NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES app_users_adv(user_id)
);

CREATE TABLE customer_tier_history_adv (
    history_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    tier TEXT NOT NULL,
    valid_from TEXT NOT NULL,
    valid_to TEXT,
    FOREIGN KEY (user_id)
        REFERENCES app_users_adv(user_id)
);

INSERT INTO app_users_adv
VALUES
    (1, '2026-01-02', 'north'),
    (2, '2026-01-05', 'west'),
    (3, '2026-01-09', 'north'),
    (4, '2026-02-02', 'south'),
    (5, '2026-02-12', 'west'),
    (6, '2026-02-18', 'east');

INSERT INTO product_events_adv
VALUES
    (1, 1, '2026-01-02 09:00:00', 'signup',
        '2026-01-02 09:00:05'),
    (2, 1, '2026-01-03 10:00:00', 'view_product',
        '2026-01-03 10:00:04'),
    (3, 1, '2026-01-03 10:05:00', 'add_to_cart',
        '2026-01-03 10:05:03'),
    (4, 1, '2026-01-03 10:10:00', 'purchase',
        '2026-01-03 10:10:08'),
    (5, 1, '2026-02-04 11:00:00', 'login',
        '2026-02-04 11:00:03'),

    (6, 2, '2026-01-05 12:00:00', 'signup',
        '2026-01-05 12:00:02'),
    (7, 2, '2026-01-06 13:00:00', 'view_product',
        '2026-01-06 13:00:01'),
    (8, 2, '2026-02-07 09:00:00', 'login',
        '2026-02-07 09:00:03'),
    (9, 2, '2026-02-07 09:10:00', 'purchase',
        '2026-02-07 09:10:04'),

    (10, 3, '2026-01-09 08:00:00', 'signup',
        '2026-01-09 08:00:02'),
    (11, 3, '2026-01-10 09:00:00', 'view_product',
        '2026-01-10 09:00:01'),

    (12, 4, '2026-02-02 10:00:00', 'signup',
        '2026-02-02 10:00:02'),
    (13, 4, '2026-02-03 11:00:00', 'view_product',
        '2026-02-03 11:00:01'),
    (14, 4, '2026-02-03 11:03:00', 'add_to_cart',
        '2026-02-03 11:03:02'),

    (15, 5, '2026-02-12 15:00:00', 'signup',
        '2026-02-12 15:00:03'),
    (16, 5, '2026-02-13 16:00:00', 'view_product',
        '2026-02-13 16:00:02'),
    (17, 5, '2026-02-13 16:15:00', 'purchase',
        '2026-02-13 16:15:06'),

    (18, 6, '2026-02-18 07:00:00', 'signup',
        '2026-02-18 07:00:04'),
    (19, 6, '2026-03-02 07:30:00', 'login',
        '2026-03-02 07:30:04');

INSERT INTO subscriptions_adv
VALUES
    (1, 1, '2026-01-03', NULL, 'pro'),
    (2, 2, '2026-02-07', NULL, 'pro'),
    (3, 5, '2026-02-13', NULL, 'pro');

INSERT INTO customer_tier_history_adv
VALUES
    (1, 1, 'standard', '2026-01-02', '2026-02-01'),
    (2, 1, 'gold',     '2026-02-01', NULL),

    (3, 2, 'standard', '2026-01-05', NULL),

    (4, 3, 'standard', '2026-01-09', NULL),

    (5, 4, 'standard', '2026-02-02', NULL),

    (6, 5, 'standard', '2026-02-12', '2026-03-01'),
    (7, 5, 'gold',     '2026-03-01', NULL),

    (8, 6, 'standard', '2026-02-18', NULL);
""")

adv_conn.commit()

display(pd.read_sql_query(
    """
    SELECT *
    FROM product_events_adv
    ORDER BY user_id, event_time, event_id
    """,
    adv_conn
))
'''))


cells.append(md(r"""
# Analytical SQL Starts with Metric Definition

Before writing a query for a metric such as retention, conversion, churn, or active users, define the metric precisely.

Consider:

> What is a monthly active user?

Possible definitions include:

- any user producing any event
- any user logging in
- any user performing a meaningful product action
- any paying user
- any user with at least N actions
- any user excluding internal/test accounts

All of these can produce different SQL while each query is syntactically correct.

Therefore analytical SQL begins with semantics.

A useful workflow is:

```text
business question
-> precise metric definition
-> grain
-> eligible population
-> time boundaries
-> SQL implementation
-> validation
```

Do not let the query silently define the metric after the fact.
"""))


cells.append(md(r"""
# Cohort Analysis

A cohort groups entities according to a shared starting characteristic.

A common example is the month in which users signed up.

Users who signed up in January belong to one cohort; users who signed up in February belong to another.

Cohorts help answer questions such as:

- Do newer users retain better?
- Did a product change improve long-term engagement?
- Does one acquisition period behave differently?
- Do users from different onboarding versions convert differently?

The most important decision is defining the **cohort anchor**.

Possible anchors include:

```text
signup time
first purchase
first paid subscription
first model deployment
first successful API call
```

Different anchors answer different questions.
"""))


cells.append(code(r'''
cohorts = pd.read_sql_query(
    """
    SELECT
        user_id,
        signup_date,
        strftime('%Y-%m', signup_date) AS signup_cohort
    FROM app_users_adv
    ORDER BY user_id
    """,
    adv_conn
)

display(cohorts)
'''))


cells.append(md(r"""
# Cohort Grain

The cohort assignment should generally have one row per entity being analyzed.

For user retention:

```text
one row per user
```

If cohort assignment accidentally has several rows per user, joining it with activity events can multiply activity and corrupt counts.

This is a recurring advanced SQL principle:

> Validate the grain of every intermediate relation before joining it.
"""))


cells.append(md(r"""
# Activity Periods

Retention analysis also needs an activity period.

For monthly retention we might convert event timestamps into:

```text
2026-01
2026-02
2026-03
```

However, a user may produce hundreds of events in one month.

Retention normally asks whether the user was active, not how many events they generated.

So an intermediate relation often has grain:

```text
one row per user per activity month
```

This prevents highly active users from being counted repeatedly.
"""))


cells.append(code(r'''
user_month_activity = pd.read_sql_query(
    """
    SELECT DISTINCT
        user_id,
        strftime('%Y-%m', event_time) AS activity_month
    FROM product_events_adv
    WHERE event_name <> 'signup'
    ORDER BY user_id, activity_month
    """,
    adv_conn
)

display(user_month_activity)
'''))


cells.append(md(r"""
# Monthly Retention

A retention table usually compares:

```text
cohort period
```

with:

```text
activity period
```

and computes how far activity occurs from the cohort start.

For a January cohort:

```text
month 0 -> January
month 1 -> February
month 2 -> March
```

A common retention rate is:

```text
active users from cohort in period N
------------------------------------
original cohort size
```

The denominator must remain the original cohort population, not the number active in the previous period unless the metric explicitly defines something else.
"""))


cells.append(code(r'''
retention = pd.read_sql_query(
    """
    WITH cohorts AS (
        SELECT
            user_id,
            date(
                signup_date,
                'start of month'
            ) AS cohort_month
        FROM app_users_adv
    ),
    activity AS (
        SELECT DISTINCT
            user_id,
            date(
                event_time,
                'start of month'
            ) AS activity_month
        FROM product_events_adv
        WHERE event_name <> 'signup'
    ),
    joined AS (
        SELECT
            c.user_id,
            c.cohort_month,
            a.activity_month,
            (
                (
                    CAST(strftime('%Y', a.activity_month) AS INTEGER)
                    -
                    CAST(strftime('%Y', c.cohort_month) AS INTEGER)
                ) * 12
                +
                (
                    CAST(strftime('%m', a.activity_month) AS INTEGER)
                    -
                    CAST(strftime('%m', c.cohort_month) AS INTEGER)
                )
            ) AS month_number
        FROM cohorts AS c
        JOIN activity AS a
            ON a.user_id = c.user_id
           AND a.activity_month >= c.cohort_month
    ),
    cohort_sizes AS (
        SELECT
            cohort_month,
            COUNT(*) AS cohort_size
        FROM cohorts
        GROUP BY cohort_month
    ),
    retained AS (
        SELECT
            cohort_month,
            month_number,
            COUNT(DISTINCT user_id) AS active_users
        FROM joined
        GROUP BY
            cohort_month,
            month_number
    )
    SELECT
        r.cohort_month,
        r.month_number,
        s.cohort_size,
        r.active_users,
        ROUND(
            100.0 * r.active_users / s.cohort_size,
            2
        ) AS retention_percent
    FROM retained AS r
    JOIN cohort_sizes AS s
        ON s.cohort_month = r.cohort_month
    ORDER BY
        r.cohort_month,
        r.month_number
    """,
    adv_conn
)

display(retention)
'''))


cells.append(md(r"""
# Retention Interpretation

The query separates retention into explicit stages:

```text
cohorts
activity
joined periods
cohort size
retained users
final rate
```

This is intentionally more verbose than forcing everything into one expression.

Well-named intermediate CTEs make analytical definitions easier to audit.

Notice that activity uses:

```sql
SELECT DISTINCT user_id, activity_month
```

because the metric counts active users, not raw events.

Without this deduplication, a user with 100 events could incorrectly contribute 100 units to the numerator.
"""))


cells.append(md(r"""
# Retention Has Many Definitions

"Retention" is not one universal metric.

Possible definitions include:

- returned on exactly day 7
- returned during days 7–13
- active in calendar month 1
- active in every period through month N
- ever returned after signup
- still subscribed
- still paying
- performed a specific meaningful action

These metrics answer different questions.

Always document:

- anchor event
- activity event
- time window
- denominator
- timezone
- eligibility filters

A retention percentage without its definition is incomplete.
"""))


cells.append(md(r"""
# Hinglish Intuition

Retention query mein sabse dangerous mistake SQL syntax nahi, denominator aur grain ka confusion hota hai.

Suppose January mein 100 users signup hue.

February mein unmein se 40 active the.

A simple month-1 retention ho sakta hai:

```text
40 / 100 = 40%
```

Ab agar those 40 users ne total 500 events kiye, numerator 500 nahi banega.

Why?

Kyuki metric hai:

```text
kitne users wapas aaye?
```

not:

```text
kitne events generate hue?
```

Isliye intermediate grain ko consciously define karo:

```text
one row per user per activity period
```

Advanced analytics mein query ka result tabhi trustworthy hai jab tum har intermediate table ka meaning ek sentence mein explain kar sako.
"""))


cells.append(md(r"""
# Funnel Analysis

A funnel measures progression through a sequence of actions.

For an e-commerce product:

```text
view product
-> add to cart
-> purchase
```

For an AI developer platform:

```text
create account
-> create API key
-> first API request
-> first successful production deployment
```

A basic funnel might ask:

- how many users viewed?
- how many added to cart?
- how many purchased?

But a serious funnel definition must answer:

- must events happen in order?
- can they happen on different days?
- how long is the allowed conversion window?
- does any purchase count?
- can users repeat steps?
- what is the population?
"""))


cells.append(code(r'''
basic_funnel = pd.read_sql_query(
    """
    SELECT
        COUNT(DISTINCT CASE
            WHEN event_name = 'view_product'
            THEN user_id
        END) AS viewed_users,

        COUNT(DISTINCT CASE
            WHEN event_name = 'add_to_cart'
            THEN user_id
        END) AS cart_users,

        COUNT(DISTINCT CASE
            WHEN event_name = 'purchase'
            THEN user_id
        END) AS purchaser_users
    FROM product_events_adv
    """,
    adv_conn
)

display(basic_funnel)
'''))


cells.append(md(r"""
# Basic Funnel Versus Ordered Funnel

The previous query counts whether users ever performed each event.

It does not prove that:

```text
view
happened before
cart
happened before
purchase
```

A user could theoretically purchase first and view later and still appear in both counts.

If event order matters, SQL must encode order explicitly.

This is an important distinction between:

```text
event membership
```

and:

```text
ordered behavior
```
"""))


cells.append(md(r"""
# First Event Time Pattern

One useful pattern is to calculate each user's first occurrence of each funnel step.

Conditional aggregation can produce:

```text
first_view_time
first_cart_time
first_purchase_time
```

Then the query can compare timestamps.

This works well when the funnel definition specifically concerns first occurrences.

More complicated funnels may require sequence logic, session boundaries, or repeated-attempt modeling.
"""))


cells.append(code(r'''
ordered_funnel = pd.read_sql_query(
    """
    WITH first_steps AS (
        SELECT
            user_id,

            MIN(CASE
                WHEN event_name = 'view_product'
                THEN event_time
            END) AS first_view,

            MIN(CASE
                WHEN event_name = 'add_to_cart'
                THEN event_time
            END) AS first_cart,

            MIN(CASE
                WHEN event_name = 'purchase'
                THEN event_time
            END) AS first_purchase

        FROM product_events_adv
        GROUP BY user_id
    )
    SELECT
        user_id,
        first_view,
        first_cart,
        first_purchase,

        CASE
            WHEN first_view IS NOT NULL
            THEN 1 ELSE 0
        END AS reached_view,

        CASE
            WHEN first_cart IS NOT NULL
             AND first_view IS NOT NULL
             AND first_cart >= first_view
            THEN 1 ELSE 0
        END AS reached_cart_after_view,

        CASE
            WHEN first_purchase IS NOT NULL
             AND first_view IS NOT NULL
             AND (
                    first_cart IS NULL
                    OR first_purchase >= first_cart
                 )
             AND first_purchase >= first_view
            THEN 1 ELSE 0
        END AS reached_purchase_after_prior_step

    FROM first_steps
    ORDER BY user_id
    """,
    adv_conn
)

display(ordered_funnel)
'''))


cells.append(md(r"""
# Funnel Logic Can Become Subtle

The previous query is educational, but a production funnel needs a precisely defined sequence.

Questions include:

- Is `add_to_cart` mandatory before purchase?
- If a user views three products, which view belongs to the purchase?
- Can multiple purchase attempts exist?
- Does a new session reset the funnel?
- Must conversion happen within 30 minutes?
- What if timestamps tie?
- What if events arrive late?

For event analytics, the business definition should be written before implementing increasingly complex SQL.
"""))


cells.append(md(r"""
# Conversion Rates

Suppose a funnel has:

```text
1000 viewers
500 cart users
200 purchasers
```

Possible metrics include:

```text
view -> cart conversion = 500 / 1000

cart -> purchase conversion = 200 / 500

overall conversion = 200 / 1000
```

Always specify the denominator.

A dashboard showing:

```text
conversion = 40%
```

without saying which stage is the denominator is ambiguous.
"""))


cells.append(md(r"""
# Deduplication

Real data often contains duplicates.

But "duplicate" must be defined.

Possible meanings include:

- identical rows
- same external event ID
- repeated business transaction
- multiple versions of one record
- same entity loaded by multiple batches
- retry-generated copies

Deleting rows because several columns happen to match can destroy legitimate data.

Deduplication starts by identifying the **business key** and the rule for choosing the surviving record.
"""))


cells.append(code(r'''
adv_conn.executescript("""
CREATE TABLE raw_customer_updates_adv (
    row_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    ingestion_time TEXT NOT NULL
);

INSERT INTO raw_customer_updates_adv
VALUES
    (1, 100, 'Anika', '2026-01-01 09:00:00',
        '2026-01-01 09:01:00'),

    (2, 100, 'Anika Singh', '2026-01-05 12:00:00',
        '2026-01-05 12:01:00'),

    (3, 101, 'Dev', '2026-01-03 10:00:00',
        '2026-01-03 10:02:00'),

    (4, 101, 'Dev Kumar', '2026-01-03 10:00:00',
        '2026-01-03 10:03:00'),

    (5, 102, 'Sara', '2026-01-04 08:00:00',
        '2026-01-04 08:01:00');
""")

adv_conn.commit()

display(pd.read_sql_query(
    """
    SELECT *
    FROM raw_customer_updates_adv
    ORDER BY customer_id, updated_at, ingestion_time
    """,
    adv_conn
))
'''))


cells.append(md(r"""
# Latest Row per Business Key

A classic deduplication pattern uses:

```sql
ROW_NUMBER()
OVER (
    PARTITION BY business_key
    ORDER BY recency_column DESC
)
```

Then retain:

```text
row_number = 1
```

For our example:

```text
customer_id
```

is the business key.

`updated_at` indicates source recency.

But two rows can share the same `updated_at`, so we also need a deterministic tiebreaker.

We will use:

```text
ingestion_time DESC
row_id DESC
```

as additional ordering.
"""))


cells.append(code(r'''
latest_customers = pd.read_sql_query(
    """
    WITH ranked AS (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id
                ORDER BY
                    updated_at DESC,
                    ingestion_time DESC,
                    row_id DESC
            ) AS rn
        FROM raw_customer_updates_adv
    )
    SELECT
        row_id,
        customer_id,
        customer_name,
        updated_at,
        ingestion_time
    FROM ranked
    WHERE rn = 1
    ORDER BY customer_id
    """,
    adv_conn
)

display(latest_customers)
'''))


cells.append(md(r"""
# Deduplication Must Be Deterministic

Suppose two versions have the same:

```text
customer_id
updated_at
```

If the window ordering contains only:

```sql
ORDER BY updated_at DESC
```

the database is not given a complete rule for choosing between tied records.

Results may be unstable.

A production deduplication rule should ideally define a deterministic total preference using trusted columns such as:

- source version
- event sequence
- ingestion timestamp
- batch ID
- unique row ID

The chosen rule should reflect source semantics rather than arbitrary convenience.
"""))


cells.append(md(r"""
# Exact Duplicates Versus Versioned Records

These are different problems.

Exact duplicates:

```text
same logical event accidentally delivered twice
```

may require deduplication using an event ID or content fingerprint.

Versioned records:

```text
same customer represented by several legitimate updates
```

require a "latest valid version" rule.

Do not use `SELECT DISTINCT` as a universal deduplication solution.

`DISTINCT` only removes rows identical across selected expressions. It does not understand business identity or recency.
"""))


cells.append(md(r"""
# Gaps and Islands

"Gaps and islands" describes a family of SQL problems involving consecutive sequences.

Examples:

- consecutive active days
- consecutive machine-failure periods
- continuous subscription periods
- runs of missing observations
- consecutive IDs
- streaks of model-serving errors

An **island** is a consecutive run.

A **gap** separates islands.

Window functions are often central to solving these problems.
"""))


cells.append(code(r'''
adv_conn.executescript("""
CREATE TABLE daily_activity_adv (
    user_id INTEGER NOT NULL,
    activity_date TEXT NOT NULL,
    PRIMARY KEY (user_id, activity_date)
);

INSERT INTO daily_activity_adv
VALUES
    (1, '2026-03-01'),
    (1, '2026-03-02'),
    (1, '2026-03-03'),
    (1, '2026-03-06'),
    (1, '2026-03-07'),
    (1, '2026-03-10'),

    (2, '2026-03-01'),
    (2, '2026-03-04'),
    (2, '2026-03-05');
""")

adv_conn.commit()

display(pd.read_sql_query(
    """
    SELECT *
    FROM daily_activity_adv
    ORDER BY user_id, activity_date
    """,
    adv_conn
))
'''))


cells.append(md(r"""
# Gaps with LAG

The easiest first step is often to compare each date with the previous date.

For each user:

```sql
LAG(activity_date)
OVER (
    PARTITION BY user_id
    ORDER BY activity_date
)
```

Then calculate the difference.

If the difference is greater than one day, a new island starts.
"""))


cells.append(code(r'''
gaps = pd.read_sql_query(
    """
    SELECT
        user_id,
        activity_date,

        LAG(activity_date) OVER (
            PARTITION BY user_id
            ORDER BY activity_date
        ) AS previous_date,

        julianday(activity_date)
        -
        julianday(
            LAG(activity_date) OVER (
                PARTITION BY user_id
                ORDER BY activity_date
            )
        ) AS gap_days

    FROM daily_activity_adv
    ORDER BY user_id, activity_date
    """,
    adv_conn
)

display(gaps)
'''))


cells.append(md(r"""
# Building Islands

Once we identify where a new sequence begins, we can create an island identifier.

A common approach is:

1. flag the beginning of each new island
2. cumulatively sum those flags
3. group by the resulting island number

This demonstrates an important window-function composition pattern:

```text
LAG
-> boundary flag
-> cumulative SUM
-> GROUP BY
```
"""))


cells.append(code(r'''
islands = pd.read_sql_query(
    """
    WITH previous_dates AS (
        SELECT
            user_id,
            activity_date,

            LAG(activity_date) OVER (
                PARTITION BY user_id
                ORDER BY activity_date
            ) AS previous_date

        FROM daily_activity_adv
    ),
    boundaries AS (
        SELECT
            user_id,
            activity_date,

            CASE
                WHEN previous_date IS NULL
                  OR julianday(activity_date)
                     - julianday(previous_date) > 1
                THEN 1
                ELSE 0
            END AS starts_new_island

        FROM previous_dates
    ),
    numbered AS (
        SELECT
            user_id,
            activity_date,

            SUM(starts_new_island) OVER (
                PARTITION BY user_id
                ORDER BY activity_date
                ROWS BETWEEN
                    UNBOUNDED PRECEDING
                    AND CURRENT ROW
            ) AS island_id

        FROM boundaries
    )
    SELECT
        user_id,
        island_id,
        MIN(activity_date) AS start_date,
        MAX(activity_date) AS end_date,
        COUNT(*) AS streak_days
    FROM numbered
    GROUP BY
        user_id,
        island_id
    ORDER BY
        user_id,
        start_date
    """,
    adv_conn
)

display(islands)
'''))


cells.append(md(r"""
# Streak Analysis

Once islands are identified, streak questions become ordinary grouped analysis.

For example:

```text
longest consecutive active streak per user
```

can be computed by:

```text
build islands
-> count rows in each island
-> rank island lengths per user
```

The same architecture applies to:

- consecutive failures
- uptime intervals
- repeated daily purchases
- data-quality incident streaks
- model drift alert periods
"""))


cells.append(code(r'''
longest_streak = pd.read_sql_query(
    """
    WITH previous_dates AS (
        SELECT
            user_id,
            activity_date,
            LAG(activity_date) OVER (
                PARTITION BY user_id
                ORDER BY activity_date
            ) AS previous_date
        FROM daily_activity_adv
    ),
    boundaries AS (
        SELECT
            user_id,
            activity_date,
            CASE
                WHEN previous_date IS NULL
                  OR julianday(activity_date)
                     - julianday(previous_date) > 1
                THEN 1
                ELSE 0
            END AS start_flag
        FROM previous_dates
    ),
    numbered AS (
        SELECT
            user_id,
            activity_date,
            SUM(start_flag) OVER (
                PARTITION BY user_id
                ORDER BY activity_date
            ) AS island_id
        FROM boundaries
    ),
    streaks AS (
        SELECT
            user_id,
            island_id,
            MIN(activity_date) AS start_date,
            MAX(activity_date) AS end_date,
            COUNT(*) AS streak_days
        FROM numbered
        GROUP BY
            user_id,
            island_id
    ),
    ranked AS (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY user_id
                ORDER BY
                    streak_days DESC,
                    start_date
            ) AS rn
        FROM streaks
    )
    SELECT
        user_id,
        start_date,
        end_date,
        streak_days
    FROM ranked
    WHERE rn = 1
    ORDER BY user_id
    """,
    adv_conn
)

display(longest_streak)
'''))


cells.append(md(r"""
# Relational Division Awareness

Some SQL questions ask:

> Which entities are related to all required values?

Examples:

- students who completed every required course
- suppliers who provide every required component
- models evaluated on every mandatory benchmark
- users who possess every required permission

This family of problems is sometimes described as **relational division**.

SQL does not normally use a literal `DIVIDE` keyword. Instead, common patterns use:

- double `NOT EXISTS`
- grouped counts
- set comparisons
"""))


cells.append(md(r"""
# Double NOT EXISTS Pattern

Suppose we want models evaluated on every required benchmark.

Conceptually:

```text
find models for which
there does NOT exist
a required benchmark for which
there does NOT exist
a matching evaluation
```

This sounds awkward in English, but logically it means:

```text
no required item is missing
```

The double-`NOT EXISTS` pattern is therefore powerful for "all requirements satisfied" queries.
"""))


cells.append(code(r'''
adv_conn.executescript("""
CREATE TABLE required_checks_adv (
    check_name TEXT PRIMARY KEY
);

CREATE TABLE model_checks_adv (
    model_name TEXT NOT NULL,
    check_name TEXT NOT NULL,
    passed INTEGER NOT NULL,
    PRIMARY KEY (model_name, check_name)
);

INSERT INTO required_checks_adv
VALUES
    ('accuracy'),
    ('latency'),
    ('security');

INSERT INTO model_checks_adv
VALUES
    ('model_a', 'accuracy', 1),
    ('model_a', 'latency', 1),
    ('model_a', 'security', 1),

    ('model_b', 'accuracy', 1),
    ('model_b', 'latency', 1),

    ('model_c', 'accuracy', 1),
    ('model_c', 'latency', 1),
    ('model_c', 'security', 0);
""")

adv_conn.commit()

qualified_models = pd.read_sql_query(
    """
    SELECT DISTINCT mc.model_name
    FROM model_checks_adv AS mc
    WHERE NOT EXISTS (
        SELECT 1
        FROM required_checks_adv AS rc
        WHERE NOT EXISTS (
            SELECT 1
            FROM model_checks_adv AS x
            WHERE x.model_name = mc.model_name
              AND x.check_name = rc.check_name
              AND x.passed = 1
        )
    )
    ORDER BY mc.model_name
    """,
    adv_conn
)

display(qualified_models)
'''))


cells.append(md(r"""
# Pivoting with Conditional Aggregation

Relational data is usually stored in rows, but reports sometimes need categories transformed into columns.

Suppose event counts are stored as:

```text
user_id | event_name | count
```

A report may want:

```text
user_id | views | carts | purchases
```

A portable SQL pattern uses conditional aggregation:

```sql
SUM(CASE WHEN ... THEN 1 ELSE 0 END)
```

This is effectively a manual pivot.
"""))


cells.append(code(r'''
event_pivot = pd.read_sql_query(
    """
    SELECT
        user_id,

        SUM(CASE
            WHEN event_name = 'view_product'
            THEN 1 ELSE 0
        END) AS views,

        SUM(CASE
            WHEN event_name = 'add_to_cart'
            THEN 1 ELSE 0
        END) AS cart_events,

        SUM(CASE
            WHEN event_name = 'purchase'
            THEN 1 ELSE 0
        END) AS purchases,

        SUM(CASE
            WHEN event_name = 'login'
            THEN 1 ELSE 0
        END) AS logins

    FROM product_events_adv
    GROUP BY user_id
    ORDER BY user_id
    """,
    adv_conn
)

display(event_pivot)
'''))


cells.append(md(r"""
# Native PIVOT Features

Some database systems provide dedicated pivot syntax.

Others rely primarily on conditional aggregation or database-specific extensions.

Native pivot syntax is not fully portable across SQL engines.

Conditional aggregation remains important because it is conceptually simple and works across many relational systems.

However, manually writing hundreds of category columns is usually a sign that the reporting shape should be reconsidered or generated carefully.
"""))


cells.append(md(r"""
# Unpivot Awareness

Unpivoting transforms columns into rows.

Suppose a wide table contains:

```text
model_id
accuracy
precision
recall
f1
```

A long representation could be:

```text
model_id
metric_name
metric_value
```

Long-form metric data often becomes easier to:

- filter
- aggregate
- visualize
- extend with new metric names

Some databases provide `UNPIVOT`-style syntax; otherwise `UNION ALL` or engine-specific techniques can produce long form.
"""))


cells.append(md(r"""
# Static Versus Dynamic Pivoting

Conditional aggregation assumes known categories:

```text
views
purchases
logins
```

But suppose categories are discovered dynamically.

Then the SQL column list itself must change.

Value parameters cannot normally replace SQL identifiers, so dynamic pivoting may require dynamic SQL generation.

Dynamic SQL should be treated carefully because it introduces:

- injection risks
- quoting complexity
- changing output schema
- difficult testing
- database-specific syntax

Often it is simpler to return long-form data and pivot in a reporting/analysis layer.
"""))


cells.append(md(r"""
# Dynamic SQL

Dynamic SQL means constructing SQL structure programmatically.

Sometimes it is genuinely required—for example, generating a report over an allowed set of columns.

But this is fundamentally different from parameterizing values.

Safe:

```python
cursor.execute(
    "SELECT * FROM users WHERE user_id = ?",
    (user_id,)
)
```

This cannot generally parameterize:

```text
table name
column name
ASC / DESC keyword
SQL operator
```

When SQL structure must be dynamic, use strict allowlists and trusted query-building techniques.
"""))


cells.append(code(r'''
allowed_sort_columns = {
    "event_time",
    "event_name",
    "user_id",
}

requested_sort = "event_time"

if requested_sort not in allowed_sort_columns:
    raise ValueError("Invalid sort column.")

# Safe here because the structural identifier came
# from a strict application-controlled allowlist.
sql = f"""
SELECT
    event_id,
    user_id,
    event_name,
    event_time
FROM product_events_adv
ORDER BY {requested_sort}
LIMIT ?
"""

rows = adv_conn.execute(sql, (5,)).fetchall()

for row in rows:
    print(row)
'''))


cells.append(md(r"""
# JSON in Relational Databases

Modern relational databases frequently support JSON.

JSON can be valuable when input contains flexible or semi-structured attributes.

Examples include:

- external API payloads
- model inference metadata
- experiment configuration
- optional event properties
- evolving integration fields

But JSON should not automatically replace relational schema.

If an attribute is central to:

- joins
- uniqueness
- foreign keys
- filtering
- grouping
- integrity constraints

a typed relational column is often easier to manage.
"""))


cells.append(code(r'''
json_supported = False

try:
    value = adv_conn.execute(
        """
        SELECT json_extract(
            '{"model":"fraud_v2","score":0.87}',
            '$.model'
        )
        """
    ).fetchone()[0]

    json_supported = True
    print("JSON extraction result:", value)

except sqlite3.OperationalError as exc:
    print(
        "JSON function unavailable in this SQLite build:",
        exc
    )
'''))


cells.append(md(r"""
# Querying JSON

Where supported, SQL JSON functions can extract nested values.

Conceptually:

```sql
json_extract(payload, '$.model')
```

may access a model identifier in a JSON document.

Production databases differ significantly in:

- JSON data types
- operators
- indexing
- path syntax
- validation
- performance

For frequently queried fields, consider whether they deserve first-class typed columns rather than repeated runtime JSON extraction.
"""))


cells.append(md(r"""
# JSON and AI Event Payloads

An inference event might have stable fields:

```text
request_id
model_version_id
timestamp
latency_ms
status
```

plus flexible metadata:

```text
device
client version
experiment flags
optional diagnostics
```

A hybrid schema can be reasonable:

```text
stable important fields -> typed columns
flexible auxiliary metadata -> JSON
```

This preserves relational integrity for critical fields while allowing controlled flexibility where the shape legitimately changes.
"""))


cells.append(md(r"""
# Full-Text Search

A normal B-tree index is not designed to solve general document search such as:

```text
find documents containing concepts related to these words
```

Full-text search systems tokenize textual content and maintain specialized inverted indexes.

Capabilities may include:

- token search
- phrase search
- ranking
- stemming
- language-aware processing
- prefix matching

SQLite provides FTS extensions such as FTS5 when available. PostgreSQL, MySQL, and specialized search systems provide their own mechanisms.
"""))


cells.append(md(r"""
# LIKE Is Not a Full-Text Search Engine

A query such as:

```sql
WHERE document_text LIKE '%transformer%'
```

can be useful for small data but is not a substitute for a full-text index at scale.

Leading-wildcard substring searches often cannot efficiently navigate a normal B-tree.

Full-text search uses a different data structure designed around terms and documents.

This reinforces a general database principle:

> Index structures are designed for particular query geometries.
"""))


cells.append(code(r'''
fts_available = False

try:
    adv_conn.execute("""
    CREATE VIRTUAL TABLE docs_fts_adv
    USING fts5(title, body)
    """)

    adv_conn.executemany(
        """
        INSERT INTO docs_fts_adv (title, body)
        VALUES (?, ?)
        """,
        [
            (
                "SQL Transactions",
                "Transactions provide atomic database updates."
            ),
            (
                "Model Serving",
                "Model serving exposes machine learning inference APIs."
            ),
            (
                "SQL Indexes",
                "Indexes improve selected relational lookup patterns."
            ),
        ],
    )

    fts_available = True

    display(pd.read_sql_query(
        """
        SELECT
            title,
            body
        FROM docs_fts_adv
        WHERE docs_fts_adv MATCH 'SQL'
        """,
        adv_conn
    ))

except sqlite3.OperationalError as exc:
    print(
        "FTS5 is unavailable in this SQLite build:",
        exc
    )
'''))


cells.append(md(r"""
# Full-Text Search Versus Vector Search

Full-text search and vector similarity search solve different problems.

Full-text search commonly uses token/term matching.

Vector search compares embedding representations to retrieve semantically similar items.

Modern retrieval systems may combine:

```text
keyword search
+
vector search
+
metadata filtering
```

This foundation course only introduces the distinction. Advanced vector databases, RAG, and advanced retrieval engineering belong to later LLM-focused study.
"""))


cells.append(md(r"""
# Temporal Data

Many databases need to answer not only:

> What is true now?

but:

> What was true at time T?

Examples include:

- customer's region at purchase time
- employee's department on a historical date
- model deployed when a prediction occurred
- feature value available at prediction time
- account status before a transaction

Temporal requirements affect schema design, query logic, indexes, and correctness.
"""))


cells.append(md(r"""
# Effective-Dated Records

A common history design stores:

```text
valid_from
valid_to
```

For example:

```text
user_id | tier     | valid_from | valid_to
1       | standard | Jan 2      | Feb 1
1       | gold     | Feb 1      | NULL
```

A row with:

```text
valid_to IS NULL
```

often represents the current version.

A historical query needs the version whose validity interval contains the target time.
"""))


cells.append(md(r"""
# Half-Open Validity Intervals

A particularly useful temporal convention is:

```text
[valid_from, valid_to)
```

meaning:

```text
valid_from <= timestamp
AND
timestamp < valid_to
```

The start is included and the end is excluded.

For open-ended current rows:

```text
valid_to IS NULL
```

This convention prevents two adjacent versions from both claiming the exact boundary timestamp.
"""))


cells.append(code(r'''
tier_at_event = pd.read_sql_query(
    """
    SELECT
        e.event_id,
        e.user_id,
        e.event_time,
        e.event_name,
        h.tier
    FROM product_events_adv AS e
    JOIN customer_tier_history_adv AS h
        ON h.user_id = e.user_id
       AND date(e.event_time) >= h.valid_from
       AND (
            h.valid_to IS NULL
            OR date(e.event_time) < h.valid_to
       )
    WHERE e.user_id IN (1, 5)
    ORDER BY e.user_id, e.event_time
    """,
    adv_conn
)

display(tier_at_event)
'''))


cells.append(md(r"""
# Temporal Join Correctness

A naïve join:

```sql
events
JOIN current_customer
```

may attach today's customer state to historical events.

That can rewrite history accidentally.

For some analyses, current state is exactly what we want.

For historical attribution, we need state valid at the event time.

This distinction is critical in ML feature engineering because joining future state to past labels can introduce temporal leakage.
"""))


cells.append(md(r"""
# Overlapping Validity Intervals

Effective-dated tables become dangerous if one entity has overlapping versions.

For example:

```text
standard: Jan 1 -> Mar 1
gold:     Feb 1 -> Apr 1
```

What tier applies on February 15?

Both rows match.

A robust temporal model needs rules preventing or resolving overlaps.

Some databases provide advanced range types or exclusion constraints; otherwise application/database validation logic may be required.
"""))


cells.append(md(r"""
# Audit History

An audit history records changes for accountability or reconstruction.

A useful audit record may include:

- entity ID
- changed timestamp
- actor/service
- operation
- old value
- new value
- request/correlation ID

Audit history and temporal business history are related but not necessarily identical.

An audit log answers:

> Who changed what?

A temporal business table may answer:

> Which state was valid at time T?

One structure does not automatically satisfy every use case.
"""))


cells.append(md(r"""
# Snapshot Data Versus Event Data

A snapshot captures state at a point in time:

```text
customer balance at midnight
inventory at end of day
daily model metrics
```

Event data records changes or occurrences:

```text
payment received
order created
model deployed
prediction generated
```

Events preserve the sequence of activity.

Snapshots can make state reconstruction faster.

Many systems use both:

```text
event history
+
periodic snapshots
```

The distinction matters when designing analytical pipelines.
"""))


cells.append(md(r"""
# ETL

ETL stands for:

```text
Extract
Transform
Load
```

Conceptually:

1. extract data from source
2. transform it outside the destination system
3. load the transformed result

Traditional ETL pipelines often transformed data before loading it into a warehouse.

The exact architecture depends on platform and era; ETL is a data-flow pattern, not one specific product.
"""))


cells.append(md(r"""
# ELT

ELT stands for:

```text
Extract
Load
Transform
```

Data is first loaded into the destination analytical platform, then transformed using the platform's compute engine—often with SQL.

Modern cloud warehouses made ELT especially common because they can process large datasets directly.

Neither ETL nor ELT is universally superior.

The choice depends on:

- source systems
- compute architecture
- data volume
- governance
- transformation tooling
- latency
- security
"""))


cells.append(md(r"""
# Staging Layers

A common data pipeline architecture separates raw ingestion from cleaned and modeled data.

Conceptually:

```text
source
  |
  v
raw / staging
  |
  v
cleaned / standardized
  |
  v
modeled
  |
  v
analytics / features
```

A staging area helps preserve source fidelity while allowing downstream transformations to be rerun.

The exact number and naming of layers varies across organizations.
"""))


cells.append(md(r"""
# Why Preserve Raw Input?

Suppose a transformation bug is discovered two months later.

If only transformed output was kept and the raw source was discarded, rebuilding correctly may be impossible.

Preserving appropriate raw or immutable source snapshots can support:

- reprocessing
- debugging
- lineage
- audits
- schema evolution
- reproducibility

Retention, privacy, and storage cost still apply. "Keep everything forever" is not automatically a sound policy.
"""))


cells.append(md(r"""
# Full Refresh

The simplest pipeline can rebuild its entire destination.

Conceptually:

```text
DELETE/TRUNCATE destination
-> recompute everything
-> reload
```

Advantages:

- easy reasoning
- naturally captures source corrections
- often idempotent

Disadvantages:

- expensive for large data
- long runtime
- large compute usage
- potentially disruptive publication

Full refresh is excellent when datasets are small enough. Incremental complexity should be introduced only when necessary.
"""))


cells.append(md(r"""
# Incremental Processing

An incremental pipeline processes only data believed to be new or changed since the previous successful run.

For example:

```sql
WHERE updated_at > last_processed_time
```

This can drastically reduce work.

But incremental pipelines are harder to make correct.

Questions include:

- What if two rows share the same timestamp?
- What if data arrives late?
- What if a source row is corrected?
- What if a row is deleted?
- What if a batch partially fails?
- What if the pipeline reruns?
- What if clocks differ?
"""))


cells.append(md(r"""
# High-Water Marks

A high-water mark records how far a pipeline has safely processed.

Example:

```text
last_processed_event_id = 987654
```

The next run processes:

```sql
WHERE event_id > 987654
```

After successful publication, the watermark advances.

The watermark itself is operational state and should usually advance only after the corresponding batch has completed successfully.
"""))


cells.append(code(r'''
adv_conn.executescript("""
CREATE TABLE source_events_incremental_adv (
    event_id INTEGER PRIMARY KEY,
    payload TEXT NOT NULL
);

CREATE TABLE processed_events_adv (
    event_id INTEGER PRIMARY KEY,
    payload TEXT NOT NULL
);

CREATE TABLE pipeline_state_adv (
    pipeline_name TEXT PRIMARY KEY,
    last_event_id INTEGER NOT NULL
);

INSERT INTO source_events_incremental_adv
VALUES
    (1, 'alpha'),
    (2, 'beta'),
    (3, 'gamma'),
    (4, 'delta'),
    (5, 'epsilon');

INSERT INTO pipeline_state_adv
VALUES
    ('event_copy', 0);
""")

adv_conn.commit()


def run_incremental_copy(conn):
    try:
        conn.execute("BEGIN")

        last_id = conn.execute(
            """
            SELECT last_event_id
            FROM pipeline_state_adv
            WHERE pipeline_name = ?
            """,
            ("event_copy",)
        ).fetchone()[0]

        new_rows = conn.execute(
            """
            SELECT event_id, payload
            FROM source_events_incremental_adv
            WHERE event_id > ?
            ORDER BY event_id
            """,
            (last_id,)
        ).fetchall()

        conn.executemany(
            """
            INSERT INTO processed_events_adv (
                event_id,
                payload
            )
            VALUES (?, ?)
            ON CONFLICT(event_id)
            DO UPDATE SET
                payload = excluded.payload
            """,
            new_rows
        )

        if new_rows:
            new_last_id = max(row[0] for row in new_rows)

            conn.execute(
                """
                UPDATE pipeline_state_adv
                SET last_event_id = ?
                WHERE pipeline_name = ?
                """,
                (new_last_id, "event_copy")
            )

        conn.commit()

    except Exception:
        conn.rollback()
        raise


run_incremental_copy(adv_conn)

display(pd.read_sql_query(
    """
    SELECT *
    FROM processed_events_adv
    ORDER BY event_id
    """,
    adv_conn
))

display(pd.read_sql_query(
    "SELECT * FROM pipeline_state_adv",
    adv_conn
))
'''))


cells.append(md(r"""
# Watermark Advancement Must Be Atomic with Processing State

Imagine:

1. watermark advances to 1000
2. destination write fails after row 850
3. pipeline restarts
4. it begins after 1000

Rows 851–1000 may never be processed.

The state change and the associated database writes should therefore be coordinated safely when they share the same transactional system.

If the destination is external—such as object storage or another warehouse—coordination becomes a distributed-systems problem.
"""))


cells.append(md(r"""
# Timestamp Watermarks

A common incremental predicate is:

```sql
WHERE updated_at > ?
```

But timestamps can be dangerous if multiple rows share the same timestamp.

Suppose the final processed row has:

```text
updated_at = 12:00:00
```

and another unprocessed row also has exactly `12:00:00`.

Using:

```sql
updated_at > '12:00:00'
```

may skip that second row.

A robust design may need a compound cursor.
"""))


cells.append(md(r"""
# Compound Watermarks

A compound high-water mark might use:

```text
(updated_at, row_id)
```

with deterministic ordering:

```sql
ORDER BY updated_at, row_id
```

The next batch can use a keyset-style predicate:

```sql
WHERE updated_at > ?
   OR (
        updated_at = ?
        AND row_id > ?
   )
```

This is conceptually the same principle used in stable keyset pagination.

A deterministic total order makes incremental progress safer.
"""))


cells.append(md(r"""
# Event Time Versus Ingestion Time

Two timestamps commonly exist in data pipelines:

**Event time**

When the event actually occurred.

**Ingestion time**

When the pipeline received or stored it.

Example:

```text
event occurred:
10:00

network delay

event ingested:
10:15
```

Using only event time as an incremental cursor can be dangerous when late events arrive with timestamps older than the current watermark.
"""))


cells.append(md(r"""
# Late-Arriving Data

Suppose a pipeline has already processed event time through:

```text
12:00
```

At 12:10, an event arrives whose actual event time is:

```text
11:45
```

If the next query is:

```sql
WHERE event_time > '12:00'
```

the late event may never be processed.

Possible strategies include:

- ingestion-time cursors
- overlapping lookback windows
- CDC streams
- source sequence IDs
- periodic reconciliation
- idempotent reprocessing
"""))


cells.append(md(r"""
# Lookback Windows

A common incremental strategy deliberately reprocesses recent history.

Instead of:

```text
process strictly after last timestamp
```

use:

```text
reprocess previous N hours/days
```

This captures some late-arriving changes.

Because rows are intentionally reprocessed, the destination must support idempotent merge/upsert behavior.

The lookback size is a trade-off:

```text
larger lookback
=
more late data captured
+
more repeated computation
```
"""))


cells.append(md(r"""
# Idempotent Pipelines

A pipeline is idempotent when rerunning the same logical batch does not incorrectly duplicate its effects.

Suppose batch 42 is retried.

Bad result:

```text
rows inserted twice
metrics doubled
```

Desired result:

```text
same final database state
```

Techniques include:

- natural/business unique keys
- UPSERT
- batch IDs
- replace-partition strategies
- atomic publication
- deterministic transformations
"""))


cells.append(md(r"""
# Batch Identifiers

Assigning each ingestion run a batch identifier can improve traceability.

Example:

```text
batch_id = ingest_2026_10_04_001
```

Rows or metadata can then record:

- source
- started time
- completed time
- row count
- success/failure
- checksum
- watermark
- pipeline version

Batch metadata helps answer:

> Which pipeline execution produced this row or dataset?
"""))


cells.append(code(r'''
adv_conn.executescript("""
CREATE TABLE pipeline_batches_adv (
    batch_id TEXT PRIMARY KEY,
    pipeline_name TEXT NOT NULL,
    status TEXT NOT NULL
        CHECK (
            status IN (
                'running',
                'completed',
                'failed'
            )
        ),
    started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completed_at TEXT,
    rows_processed INTEGER
);
""")

adv_conn.execute(
    """
    INSERT INTO pipeline_batches_adv (
        batch_id,
        pipeline_name,
        status
    )
    VALUES (?, ?, ?)
    """,
    (
        "batch_2026_10_04_001",
        "customer_features",
        "running"
    )
)

adv_conn.execute(
    """
    UPDATE pipeline_batches_adv
    SET
        status = 'completed',
        completed_at = CURRENT_TIMESTAMP,
        rows_processed = ?
    WHERE batch_id = ?
    """,
    (1250, "batch_2026_10_04_001")
)

adv_conn.commit()

display(pd.read_sql_query(
    "SELECT * FROM pipeline_batches_adv",
    adv_conn
))
'''))


cells.append(md(r"""
# UPSERT in Data Pipelines

Incremental loads often need:

```text
insert unseen record
update changed record
```

UPSERT can support this pattern.

However, the key question is:

> Which columns define record identity?

If the wrong conflict key is chosen, unrelated records can overwrite each other.

A robust pipeline defines:

- business key
- source version
- update precedence
- immutable fields
- mutable fields

before writing the UPSERT.
"""))


cells.append(md(r"""
# MERGE Awareness

Many relational and analytical database systems support some form of `MERGE` operation.

Conceptually, it compares source and target and can perform actions such as:

```text
WHEN MATCHED
    -> UPDATE

WHEN NOT MATCHED
    -> INSERT
```

Some systems can also process deletion-like semantics.

`MERGE` syntax and historical correctness guarantees differ by database product and version.

Do not copy a `MERGE` statement between platforms without reading platform-specific documentation.
"""))


cells.append(md(r"""
# Change Data Capture

Change Data Capture, or CDC, captures changes occurring in a source database.

Instead of repeatedly asking:

```text
which rows changed since yesterday?
```

CDC may expose a change stream derived from mechanisms such as:

- database transaction logs
- replication logs
- triggers
- change tables
- managed database streams

Events may describe:

```text
insert
update
delete
```

CDC is an important bridge between operational databases and downstream analytical systems.
"""))


cells.append(md(r"""
# CDC Is Not Just updated_at Filtering

An `updated_at` column can support incremental extraction, but it has limitations:

- deletions may disappear entirely
- clients may forget to update the timestamp
- multiple changes can collapse into one final state
- timestamp collisions can occur
- late transactions complicate ordering

Log-based CDC can capture a richer ordered history of database changes.

However, it introduces operational infrastructure and delivery semantics that must be understood.
"""))


cells.append(md(r"""
# CDC Delivery Semantics

Change streams may provide delivery models such as:

- at-most-once
- at-least-once
- stronger system-specific guarantees

At-least-once delivery means duplicates are possible.

Consumers therefore often need:

- stable change identifiers
- ordering metadata
- idempotent processing
- checkpointing

Never assume receiving a change event once means the distributed pipeline cannot replay it.
"""))


cells.append(md(r"""
# Deletes in Incremental Pipelines

Suppose source row 10 existed yesterday and is deleted today.

A pipeline that only queries:

```sql
WHERE updated_at > last_run
```

may never learn that row 10 disappeared.

Possible designs include:

- CDC delete events
- soft-delete markers
- snapshot comparison
- tombstone rows
- periodic full reconciliation

Deletion propagation must be designed explicitly.
"""))


cells.append(md(r"""
# Tombstones

A tombstone is a record indicating that an entity or key was deleted.

Instead of silently disappearing, a change stream might produce:

```text
key = customer_100
operation = delete
```

Downstream systems can then remove or deactivate their corresponding representation.

Tombstones are particularly important in replicated and eventually consistent systems.
"""))


cells.append(md(r"""
# Data Quality

A successful SQL query does not imply valid data.

A pipeline can run without exceptions and still produce:

- duplicate business keys
- missing IDs
- impossible dates
- negative prices
- orphan foreign keys
- unexpected categories
- row-count collapses
- future leakage

Data quality should therefore be tested explicitly.
"""))


cells.append(md(r"""
# Data Quality Dimensions

Common quality dimensions include:

**Completeness**

Are required values present?

**Uniqueness**

Are identifiers unique where required?

**Validity**

Do values satisfy domain rules?

**Referential integrity**

Do references point to known entities?

**Consistency**

Do related values agree?

**Timeliness**

Is the data sufficiently fresh?

**Volume**

Did expected data arrive?

Different datasets require different quality contracts.
"""))


cells.append(md(r"""
# SQL Quality Check: Missing Values

A simple completeness check:

```sql
SELECT COUNT(*)
FROM table
WHERE required_column IS NULL;
```

The desired count may be zero.

But quality expectations should be field-specific.

`NULL` may be valid for an optional field while unacceptable for a primary business attribute.
"""))


cells.append(code(r'''
quality_missing = adv_conn.execute(
    """
    SELECT COUNT(*)
    FROM app_users_adv
    WHERE signup_date IS NULL
       OR region IS NULL
    """
).fetchone()[0]

print("Rows missing required values:", quality_missing)
'''))


cells.append(md(r"""
# SQL Quality Check: Duplicate Business Keys

Suppose `event_id` should be unique.

A general duplicate check is:

```sql
SELECT business_key, COUNT(*)
FROM table
GROUP BY business_key
HAVING COUNT(*) > 1;
```

Even when a database constraint already enforces uniqueness, quality checks are valuable in staging/raw systems where source data may not yet be constrained.
"""))


cells.append(code(r'''
duplicate_users = pd.read_sql_query(
    """
    SELECT
        user_id,
        COUNT(*) AS row_count
    FROM app_users_adv
    GROUP BY user_id
    HAVING COUNT(*) > 1
    """,
    adv_conn
)

display(duplicate_users)
'''))


cells.append(md(r"""
# SQL Quality Check: Orphans

An orphan is a child reference with no matching parent.

A common check is:

```sql
SELECT child.*
FROM child
LEFT JOIN parent
    ON ...
WHERE parent.key IS NULL;
```

Production foreign keys can prevent many orphans, but raw ingestion areas may intentionally load unvalidated data before validation.
"""))


cells.append(code(r'''
orphans = pd.read_sql_query(
    """
    SELECT e.*
    FROM product_events_adv AS e
    LEFT JOIN app_users_adv AS u
        ON u.user_id = e.user_id
    WHERE u.user_id IS NULL
    """,
    adv_conn
)

display(orphans)
'''))


cells.append(md(r"""
# SQL Quality Check: Accepted Values

Suppose event names are expected to belong to a controlled set.

A quality query can identify unknown categories:

```sql
WHERE event_name NOT IN (...)
```

In a normalized operational system, a foreign key or `CHECK` constraint may be stronger.

In an analytical pipeline, discovering a new category can be important because it may indicate:

- legitimate schema evolution
- source bug
- upstream typo
- undocumented product event
"""))


cells.append(code(r'''
unexpected_events = pd.read_sql_query(
    """
    SELECT
        event_name,
        COUNT(*) AS row_count
    FROM product_events_adv
    WHERE event_name NOT IN (
        'signup',
        'view_product',
        'add_to_cart',
        'purchase',
        'login'
    )
    GROUP BY event_name
    """,
    adv_conn
)

display(unexpected_events)
'''))


cells.append(md(r"""
# Volume Checks

A pipeline can technically succeed while receiving almost no data.

Suppose yesterday produced:

```text
10,000,000 events
```

and today produces:

```text
13 events
```

That may be possible, but it deserves investigation.

Volume checks can compare:

- row count
- distinct entities
- partition size
- event count by source
- historical baseline

Static thresholds are useful for some datasets; dynamic anomaly detection may be appropriate for others.
"""))


cells.append(md(r"""
# Freshness Checks

A dataset can be structurally valid but stale.

A simple freshness check might inspect:

```sql
MAX(event_time)
```

Then compare it with expected recency.

For example:

```text
stream expected every 5 minutes
latest event is 3 hours old
```

This indicates pipeline or source failure even if all existing rows satisfy their constraints.
"""))


cells.append(code(r'''
latest_event = adv_conn.execute(
    """
    SELECT MAX(event_time)
    FROM product_events_adv
    """
).fetchone()[0]

print("Latest event in example data:", latest_event)
'''))


cells.append(md(r"""
# Reconciliation

A migration or pipeline may be validated by comparing source and destination.

Possible reconciliation checks include:

- row counts
- distinct key counts
- sums
- minimum/maximum dates
- checksum-like aggregates
- unmatched keys
- category distributions

For example:

```text
source total payment amount
versus
destination total payment amount
```

A matching total does not prove every row is correct, but reconciliation provides strong additional evidence when combined with other tests.
"""))


cells.append(md(r"""
# SQL Assertions

A quality check becomes more operationally useful when failure is explicit.

In Python:

```python
count = ...
if count != 0:
    raise RuntimeError(...)
```

In dedicated data-quality frameworks, assertions can be declared as tests.

The important idea is:

> Bad data should fail loudly before it silently contaminates downstream models and reports.
"""))


cells.append(code(r'''
def assert_zero(conn, sql, message):
    count = conn.execute(sql).fetchone()[0]

    if count != 0:
        raise AssertionError(
            f"{message}. Failing row count: {count}"
        )

    return count


assert_zero(
    adv_conn,
    """
    SELECT COUNT(*)
    FROM product_events_adv
    WHERE user_id IS NULL
       OR event_time IS NULL
       OR event_name IS NULL
    """,
    "Required event fields contain NULL values"
)

print("Required-field assertion passed.")
'''))


cells.append(md(r"""
# Testing SQL

SQL should be tested like application code.

Useful test categories include:

- schema tests
- constraint tests
- transformation tests
- edge-case tests
- regression tests
- integration tests
- data-quality tests
- performance tests

A complex analytical query deserves known input data and expected outputs.

Do not rely only on visually inspecting a few rows in production.
"""))


cells.append(md(r"""
# Unit Testing a SQL Transformation

A useful SQL transformation test can:

1. create a small isolated database
2. insert carefully chosen rows
3. run the transformation
4. compare results with expected values

Test data should include edge cases such as:

- `NULL`
- duplicate timestamps
- missing related rows
- zero values
- boundary dates
- tied rankings
- users with no activity
"""))


cells.append(code(r'''
test_conn = sqlite3.connect(":memory:")

test_conn.executescript("""
CREATE TABLE values_test (
    group_id INTEGER NOT NULL,
    amount REAL
);

INSERT INTO values_test
VALUES
    (1, 10),
    (1, 20),
    (1, NULL),
    (2, NULL);
""")

actual = test_conn.execute("""
SELECT
    group_id,
    COUNT(*) AS rows_total,
    COUNT(amount) AS non_null_amounts,
    SUM(amount) AS amount_sum
FROM values_test
GROUP BY group_id
ORDER BY group_id
""").fetchall()

expected = [
    (1, 3, 2, 30.0),
    (2, 1, 0, None),
]

assert actual == expected, (
    f"Unexpected result:\n"
    f"actual={actual}\n"
    f"expected={expected}"
)

print("Transformation test passed.")

test_conn.close()
'''))


cells.append(md(r"""
# Test the Boundary Cases

Most SQL errors occur at boundaries:

- midnight
- month-end
- year-end
- inclusive/exclusive date endpoints
- empty tables
- single-row partitions
- tied values
- `NULL`
- duplicate keys
- no matching join row
- several matching join rows

Good test data deliberately includes these cases rather than only clean happy-path examples.
"""))


cells.append(md(r"""
# Test Grain Invariants

Suppose a feature table should contain:

```text
one row per customer per snapshot_date
```

A direct test is:

```sql
SELECT
    customer_id,
    snapshot_date,
    COUNT(*)
FROM feature_table
GROUP BY
    customer_id,
    snapshot_date
HAVING COUNT(*) > 1;
```

An empty result confirms the uniqueness invariant for the current data.

Better still, where appropriate, enforce it with a database uniqueness constraint.
"""))


cells.append(md(r"""
# SQL Style Matters

SQL can become difficult to maintain when every query uses different formatting and naming conventions.

Readable SQL generally benefits from:

- consistent keyword casing
- meaningful aliases
- one logical expression per line
- clear indentation
- explicit join conditions
- named CTEs
- limited nesting
- comments explaining why
- deterministic ordering when needed

Style is not cosmetic when queries implement important business logic.
"""))


cells.append(md(r"""
# Meaningful CTE Names

Compare:

```sql
WITH a AS (...),
     b AS (...),
     c AS (...)
```

with:

```sql
WITH customer_cohorts AS (...),
     monthly_activity AS (...),
     retained_users AS (...)
```

The second version communicates transformation stages.

CTE names should describe the relation produced by that stage.

For complicated data pipelines, the SQL itself becomes a form of executable documentation.
"""))


cells.append(md(r"""
# Comments Should Explain Why

A weak comment:

```sql
-- filter date
WHERE event_date >= ...
```

The SQL already says that.

A useful comment:

```sql
-- Use only data available before the prediction cutoff
-- to prevent target leakage.
WHERE event_time < prediction_time
```

Comments should explain business reasoning, non-obvious constraints, and compatibility decisions.
"""))


cells.append(md(r"""
# Avoid Magic Values

A query containing:

```sql
WHERE status <> 7
```

may be incomprehensible.

Prefer meaningful values, reference tables, parameters, or documented constants.

Likewise, unexplained dates such as:

```text
2024-07-17
```

should have a reason.

Magic values make analytical logic difficult to audit and change.
"""))


cells.append(md(r"""
# Reusable SQL Models

Data transformation projects often structure SQL into reusable models.

Conceptually:

```text
raw_orders
    ->
clean_orders
    ->
customer_daily_orders
    ->
customer_features
```

Each stage should have a clear grain and responsibility.

This modular structure improves:

- testing
- lineage
- readability
- reuse
- incremental processing

Avoid creating a single 2000-line query when meaningful relational stages can be named and validated.
"""))


cells.append(md(r"""
# Lineage

Data lineage answers:

> Where did this data come from?

For a derived feature:

```text
customer_30d_spend
```

lineage might be:

```text
payments table
-> validated payments
-> customer daily spend
-> rolling 30-day feature
```

Lineage becomes important when:

- source schema changes
- data quality fails
- a model behaves unexpectedly
- metrics disagree
- compliance asks where data originated
"""))


cells.append(md(r"""
# Provenance

Provenance is related to lineage but often emphasizes exact origin and processing context.

Useful provenance metadata may include:

- source dataset
- source version
- transformation version
- execution ID
- code commit
- parameters
- timestamp
- destination version

For AI systems, provenance is essential for reproducibility.

Knowing a model used "customer data" is insufficient. We need to know which customer-data snapshot and which transformations.
"""))


cells.append(md(r"""
# Feature Engineering with SQL

SQL is extremely useful for tabular feature engineering.

Examples include:

```text
30-day transaction count
average purchase amount
days since last login
number of failed payments
customer lifetime spend
latest account state
```

These features often combine:

- joins
- aggregation
- date filtering
- window functions
- point-in-time constraints

The most important ML-specific concern is avoiding leakage.
"""))


cells.append(md(r"""
# Point-in-Time Correct Features

Suppose a training row represents a prediction at:

```text
2026-03-10 12:00
```

A valid historical feature must use only information available at or before the allowed cutoff.

For example:

```sql
WHERE transaction_time < prediction_time
```

or another precisely defined boundary.

If the feature query accidentally uses transactions from March 11, the model sees information from the future.

This is temporal data leakage.
"""))


cells.append(md(r"""
# Feature Window Boundaries

Consider a 30-day purchase feature.

A conceptual definition might be:

```text
prediction_time - 30 days
<= transaction_time
<
prediction_time
```

Using a half-open interval prevents the event occurring exactly at prediction time from being ambiguously included when it should not be visible.

The correct inclusivity depends on the application, but it must be explicit.
"""))


cells.append(code(r'''
adv_conn.executescript("""
CREATE TABLE prediction_points_adv (
    prediction_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    prediction_time TEXT NOT NULL
);

CREATE TABLE purchases_adv (
    purchase_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    purchase_time TEXT NOT NULL,
    amount REAL NOT NULL
);

INSERT INTO prediction_points_adv
VALUES
    (1, 1, '2026-03-10 12:00:00'),
    (2, 2, '2026-03-10 12:00:00');

INSERT INTO purchases_adv
VALUES
    (1, 1, '2026-02-15 10:00:00', 100.0),
    (2, 1, '2026-03-01 09:00:00', 200.0),
    (3, 1, '2026-03-11 09:00:00', 9999.0),
    (4, 2, '2026-02-01 08:00:00', 500.0),
    (5, 2, '2026-03-05 08:00:00', 75.0);
""")

adv_conn.commit()

point_in_time_features = pd.read_sql_query(
    """
    SELECT
        p.prediction_id,
        p.user_id,
        p.prediction_time,

        COUNT(x.purchase_id) AS purchase_count_30d,

        COALESCE(
            SUM(x.amount),
            0
        ) AS purchase_amount_30d

    FROM prediction_points_adv AS p

    LEFT JOIN purchases_adv AS x
        ON x.user_id = p.user_id
       AND x.purchase_time >= datetime(
            p.prediction_time,
            '-30 days'
       )
       AND x.purchase_time < p.prediction_time

    GROUP BY
        p.prediction_id,
        p.user_id,
        p.prediction_time

    ORDER BY p.prediction_id
    """,
    adv_conn
)

display(point_in_time_features)
'''))


cells.append(md(r"""
Notice that user 1's purchase after the prediction timestamp is not included, even though its amount is very large.

This is the correct behavior for a historical feature.

A query that simply aggregated all purchases by user and joined the result to historical prediction rows would leak future information.
"""))


cells.append(md(r"""
# Label Construction

ML labels also require precise SQL definitions.

Suppose a fraud model predicts whether a transaction will be followed by a chargeback within 30 days.

The label query needs:

- prediction/reference event
- outcome event
- future observation window
- boundary rules
- sufficient follow-up time

A transaction from yesterday cannot always be labeled negative merely because no chargeback has appeared yet. The observation window may not have completed.

This is called label maturity or outcome completeness.
"""))


cells.append(md(r"""
# Feature Time and Label Time Are Different

For supervised learning:

```text
past / present
    -> features

future
    -> label
```

The feature query must not cross forward into the label window.

The label query often intentionally looks forward.

Confusing these two windows is a major source of leakage.

A well-designed training dataset documents:

```text
prediction time
feature cutoff
label window
observation end
```
"""))


cells.append(md(r"""
# Current-State Tables Can Leak Future Information

Suppose today's customer table says:

```text
customer_id = 5
status = delinquent
```

We build a historical training example from six months ago and join the current customer table.

If the customer became delinquent only last month, the historical training row now contains future information.

Current-state tables are therefore dangerous in retrospective ML training unless the field is truly time-invariant.

Historical feature reconstruction often requires versioned or event-based source data.
"""))


cells.append(md(r"""
# Snapshot Feature Tables

One architecture computes features at periodic snapshots.

Example grain:

```text
one row per customer per feature_date
```

Columns might include:

```text
purchase_count_30d
average_order_value_90d
days_since_last_login
failed_payment_count_7d
```

Advantages:

- reusable training inputs
- easier auditing
- faster downstream training
- explicit point-in-time dates

Costs include:

- storage
- refresh logic
- backfills
- feature-definition versioning
"""))


cells.append(md(r"""
# Online and Offline Feature Consistency

A model may train using SQL-computed offline features but serve using features computed by application code.

If the definitions differ, training-serving skew occurs.

For example:

```text
offline:
30 days inclusive

online:
30 * 24 hours exclusive
```

or:

```text
offline:
ignore cancelled orders

online:
include cancelled orders
```

Feature definitions should be shared, tested, versioned, or otherwise governed to reduce skew.
"""))


cells.append(md(r"""
# Incremental Feature Computation

Suppose daily customer features depend on years of history.

Recomputing everything every day may become expensive.

Incremental strategies can maintain intermediate aggregates such as:

```text
customer daily spend
customer daily event counts
```

Then longer feature windows can aggregate smaller daily tables.

This is a classic trade-off between:

- storage
- computation
- freshness
- complexity

Correctness under late-arriving events must still be addressed.
"""))


cells.append(md(r"""
# Feature Backfills

When a feature definition changes, historical values may need to be recomputed.

For example:

```text
v1:
count all transactions

v2:
exclude reversed transactions
```

A feature pipeline should know:

- which version generated existing data
- what date range needs backfill
- whether online consumers can tolerate mixed versions
- how publication occurs atomically

Versioning is therefore not only for models. Data transformations also have versions.
"""))


cells.append(md(r"""
# Data Contracts

A data contract defines expectations between data producers and consumers.

It may describe:

- schema
- types
- allowed values
- keys
- nullability
- semantics
- freshness
- ownership
- compatibility expectations

A source adding a column is usually easier to tolerate than changing:

```text
amount
```

from:

```text
currency units
```

to:

```text
currency cents
```

without notice.

Semantic changes can be more dangerous than structural changes.
"""))


cells.append(md(r"""
# Schema Drift

Schema drift occurs when incoming structure changes unexpectedly.

Examples:

- new column
- removed column
- renamed field
- type change
- nested JSON shape change

Pipelines should decide whether unexpected drift should:

- fail
- warn
- quarantine records
- accept compatible additions
- trigger schema evolution

Silently coercing everything into strings may keep a pipeline "green" while destroying data meaning.
"""))


cells.append(md(r"""
# Quarantine Patterns

Bad rows do not always need to crash an entire large ingestion batch.

Some systems route invalid records into a quarantine/dead-letter structure containing:

- original record
- validation error
- source
- ingestion time
- batch ID

Valid rows continue while invalid rows remain observable for investigation.

This is appropriate only when partial acceptance matches business requirements. Financial or strongly transactional imports may instead require atomic rejection.
"""))


cells.append(md(r"""
# Reprocessing

Reliable data platforms assume transformations may need to run again.

Reasons include:

- fixed bug
- new business logic
- late source data
- schema change
- corruption recovery
- feature backfill

Reprocessing becomes easier when:

- raw inputs are reproducibly available
- transformations are deterministic
- outputs are versioned
- jobs are idempotent
- lineage is recorded
"""))


cells.append(md(r"""
# Exactly-Once Processing Awareness

"Exactly once" is often used loosely.

In a distributed pipeline:

- messages can be retried
- workers can crash
- acknowledgements can be lost
- databases and queues have separate transactions

Many robust systems instead achieve the desired final state through:

```text
at-least-once delivery
+
idempotent processing
+
deduplication
+
transactional boundaries
```

Do not assume that a framework's "exactly once" phrase eliminates the need to understand its precise failure semantics.
"""))


cells.append(md(r"""
# SQL and Orchestration

SQL transformations are often executed by an orchestration system.

An orchestrator coordinates:

- dependencies
- schedules
- retries
- parameters
- backfills
- logging
- alerts

Conceptually:

```text
ingest
   |
validate
   |
clean
   |
aggregate
   |
build features
   |
train
```

SQL is one layer of the pipeline. Workflow state and dependencies belong to broader data engineering.
"""))


cells.append(md(r"""
# Do Not Hide Pipeline State in Random Files

A production pipeline may need durable state such as:

```text
last successful watermark
batch ID
run status
source snapshot
row counts
```

Scattering this state across ad-hoc local text files can make distributed execution unreliable.

Operational metadata should have a deliberate persistence strategy.

Relational databases are often well suited for this type of transactional pipeline metadata.
"""))


cells.append(md(r"""
# Reusable Analytical Query Design

Complex SQL becomes easier to reason about when built as stages.

For example:

```text
eligible_population
        |
filtered_events
        |
entity_level_features
        |
labels
        |
final_training_dataset
```

For every stage, document:

```text
grain
keys
filters
time semantics
```

This creates a transformation DAG in relational form.
"""))


cells.append(md(r"""
# Avoid Accidental Many-to-Many Joins

A common pipeline bug occurs when two intermediate relations both contain multiple rows per entity.

Suppose:

```text
customer_features:
3 rows per customer

customer_labels:
2 rows per customer
```

Joining only on `customer_id` can create:

```text
3 × 2 = 6 rows
```

per customer.

Before joining, verify that join keys represent the intended grain on both sides.

Many "mysterious duplicate" problems are actually grain mismatches.
"""))


cells.append(md(r"""
# Pre-Aggregation Before Joining

Suppose we need:

```text
one row per customer
```

but transactions contain many rows per customer.

A safe pattern is:

```text
transactions
-> aggregate to customer grain
-> join customers
```

rather than joining several detail tables first and aggregating afterward.

Pre-aggregation can prevent row multiplication and often improves performance.
"""))


cells.append(md(r"""
# Reconciliation After Joins

Useful join checks include:

```text
row count before
row count after
distinct entity count before
distinct entity count after
unmatched entities
duplicate key count
```

If a supposedly one-to-one enrichment doubles row count, investigate before continuing.

Data pipeline correctness should be checked at transformation boundaries, not only at the final output.
"""))


cells.append(md(r"""
# Null Semantics in Pipelines

Pipelines often incorrectly convert `NULL` to zero.

But:

```text
NULL
```

may mean:

```text
unknown / unavailable / not applicable
```

while:

```text
0
```

means a known numeric zero.

For ML features, this distinction can matter significantly.

Imputation policy should be deliberate and often belongs to the feature/model pipeline rather than being silently applied by every SQL transformation.
"""))


cells.append(md(r"""
# Time Zones

Production event pipelines frequently contain multiple time zones.

Questions include:

- Are timestamps stored in UTC?
- Is the source timestamp timezone-aware?
- Which timezone defines a business day?
- What happens at daylight-saving transitions?
- Does a cohort use user-local date or UTC date?

SQLite's date/time facilities are limited compared with richer server databases, so production temporal logic should use the capabilities of the chosen platform carefully.

A date boundary is not meaningful until its timezone semantics are known.
"""))


cells.append(md(r"""
# Deterministic Transformations

A reproducible transformation should avoid unspecified order and unstable choices.

Examples of nondeterminism include:

- `LIMIT` without `ORDER BY`
- selecting a row from tied values without a tiebreaker
- using changing current timestamps in historical rebuilds without deliberate semantics
- depending on mutable external state

Determinism makes:

- testing
- backfills
- debugging
- reproducibility

substantially easier.
"""))


cells.append(md(r"""
# SQL Review Checklist

For an important transformation, review:

- What does one output row represent?
- What is the output key?
- Are joins one-to-one, one-to-many, or many-to-many?
- Can joins multiply rows?
- Are `NULL` semantics correct?
- Are time boundaries explicit?
- Is ordering deterministic?
- Are future values excluded where required?
- Are duplicates handled using business semantics?
- Is the query idempotent when materialized?
- Can late data change the result?
- What tests verify the output?
- Is performance acceptable?
- Is lineage documented?
"""))


cells.append(md(r"""
# Data Pipeline Review Checklist

For an incremental pipeline, additionally ask:

- What is the source of truth?
- What defines a new row?
- What defines an updated row?
- How are deletes represented?
- What is the watermark?
- Can several rows share the watermark value?
- Can data arrive late?
- Is there a lookback strategy?
- Can the batch be safely retried?
- When does the watermark advance?
- Are writes atomic?
- Is batch metadata recorded?
- Can the pipeline be backfilled?
- How is a failed batch recovered?
- How are quality failures handled?
"""))


cells.append(md(r"""
# AI Training Dataset Review Checklist

Before trusting a SQL-built training dataset, ask:

- What does one training row represent?
- What is prediction time?
- What is the feature cutoff?
- What is the label window?
- Are current-state tables leaking future information?
- Are features computed only from allowed history?
- Are labels mature?
- Are multiple source rows multiplying examples?
- Are duplicate entities intentional?
- Are missing values meaningful?
- Can the dataset be reproduced later?
- Is the source snapshot/version recorded?
- Is the feature transformation version recorded?
- Is class distribution plausible?
- Are train/validation/test time boundaries correct?
"""))


cells.append(md(r"""
# Common Advanced SQL Mistakes

Common mistakes include:

- counting events instead of distinct entities in retention
- using the wrong cohort anchor
- computing funnel stages without enforcing required order
- using `DISTINCT` as generic deduplication
- choosing latest rows without deterministic tie-breaking
- joining current state into historical examples
- using event-time watermarks without handling late data
- advancing watermarks before successful publication
- ignoring source deletions
- making incremental pipelines non-idempotent
- using dynamic SQL without structural allowlists
- storing important relational fields only inside JSON
- treating `LIKE '%term%'` as scalable full-text search
- ignoring overlapping temporal intervals
- checking only whether a pipeline ran, not whether data is valid
- averaging averages without weights
- joining several detail tables before establishing grain
- building ML features with future information
"""))


cells.append(md(r"""
# End-to-End SQL Data Pipeline Architecture

A robust SQL-centered pipeline can conceptually look like:

```text
Operational Sources
        |
        v
Ingestion
        |
        v
Raw / Staging Data
        |
        +---- Data Quality Checks
        |
        v
Cleaned / Standardized Data
        |
        +---- Deduplication
        +---- Schema Validation
        +---- Referential Validation
        |
        v
Modeled Relational Data
        |
        +---- Analytical Facts/Dimensions
        +---- Historical State
        |
        v
Feature / Reporting Models
        |
        +---- Point-in-Time Validation
        +---- Metric Tests
        |
        v
Published Dataset
        |
        +---- Version
        +---- Batch Metadata
        +---- Lineage
        +---- Quality Results
```

Each boundary should have an explicit grain and data contract.
"""))


cells.append(md(r"""
# End-to-End AI Feature Pipeline Example

Imagine building a churn model.

Operational data contains:

```text
customers
subscriptions
payments
logins
support tickets
```

A robust SQL workflow might:

1. define prediction dates
2. identify eligible customers
3. construct historical payment features before prediction time
4. construct historical login features
5. construct support-interaction features
6. join each feature table at one-row-per-prediction grain
7. define churn outcome in a future label window
8. exclude examples whose label window has not matured
9. run uniqueness and leakage checks
10. publish a versioned training dataset
11. record source snapshots and transformation version

The difficult part is not `SELECT`.

The difficult part is keeping time, grain, identity, and provenance correct across the entire workflow.
"""))


cells.append(md(r"""
# Advanced SQL Patterns and Data Pipeline Engineering Summary

Advanced SQL combines relational reasoning with temporal, analytical, and operational correctness.

Cohort analysis groups entities around a defined anchor. Retention then measures subsequent activity against a clearly defined denominator.

Funnels measure progression through actions, but event membership and ordered event progression are different problems.

Deduplication requires a business key and deterministic survivor rule. Window functions make latest-version and ranking patterns expressive.

Gaps-and-islands techniques identify consecutive sequences by combining `LAG`, boundary detection, cumulative windows, and grouping.

Relational division solves "all required items" questions. Conditional aggregation provides portable pivot-like transformations.

JSON adds useful flexibility but should not replace important relational structure. Full-text search requires specialized indexing and differs from vector similarity search.

Temporal databases distinguish current state from historical state. Effective-dated records and point-in-time joins prevent historical data from being incorrectly enriched with future/current information.

ETL and ELT describe different transformation locations. Staging layers, raw preservation, batch metadata, and lineage improve reproducibility.

Incremental pipelines reduce processing cost but introduce difficult problems involving watermarks, ties, late-arriving data, deletes, retries, and idempotency.

CDC provides richer change streams than ordinary timestamp filtering but introduces distributed delivery semantics.

Data quality must be tested explicitly for completeness, uniqueness, validity, integrity, freshness, and volume.

SQL transformations should be tested like code.

For AI engineering, SQL is especially powerful for feature computation, historical reconstruction, labeling, and dataset generation—but point-in-time correctness is mandatory to prevent leakage.

The central principle is:

> Every transformation should have explicit grain, identity, time semantics, quality expectations, and reproducible lineage.
"""))


cells.append(md(r"""
# What Comes Next

The next SQL part should serve as the final consolidation and professional SQL engineering section.

It can cover:

- SQL dialect portability
- SQLite versus PostgreSQL versus MySQL syntax differences
- database drivers and Python DB-API patterns
- SQLAlchemy awareness
- ORM trade-offs
- repository/service architecture
- secure configuration
- realistic end-to-end relational application design
- database code review
- debugging incorrect SQL results
- debugging slow SQL
- production incident reasoning
- SQL interview foundations
- complete SQL revision map
- final AI-engineering relational case study

After that, the comprehensive SQL notebook can receive a dedicated end-of-unit practice notebook and separate solutions if desired, while keeping practice outside this theory notebook.
"""))


nb.cells.extend(cells)

if len(nb.cells) <= start_count:
    raise RuntimeError(
        "Part 11 construction failed: no cells were appended."
    )

part11_locations = heading_locations(nb, PART11)

if len(part11_locations) != 1:
    raise RuntimeError(
        f"Expected exactly one Part 11 marker, "
        f"found {part11_locations}."
    )

for marker in required_markers:
    locations = heading_locations(nb, marker)

    if len(locations) != 1:
        raise RuntimeError(
            f"Prior section changed unexpectedly: "
            f"{marker!r} -> {locations}"
        )

nbf.validate(nb)

# Direct write only. No temporary notebook is created.
nbf.write(nb, NOTEBOOK_PATH)

# Read back the persisted notebook and validate it.
saved_nb = nbf.read(
    NOTEBOOK_PATH,
    as_version=4
)

nbf.validate(saved_nb)

all_markers = required_markers + [PART11]

for marker in all_markers:
    locations = heading_locations(
        saved_nb,
        marker
    )

    if len(locations) != 1:
        raise RuntimeError(
            f"Post-write marker validation failed for "
            f"{marker!r}: {locations}"
        )

part11_start = heading_locations(
    saved_nb,
    PART11
)[0]

part11_text = "\n".join(
    cell.source
    for cell in saved_nb.cells[part11_start:]
    if cell.cell_type == "markdown"
)

required_concepts = [
    "Cohort Analysis",
    "Monthly Retention",
    "Funnel Analysis",
    "Basic Funnel Versus Ordered Funnel",
    "Deduplication",
    "Latest Row per Business Key",
    "Gaps and Islands",
    "Streak Analysis",
    "Relational Division Awareness",
    "Pivoting with Conditional Aggregation",
    "Dynamic SQL",
    "JSON in Relational Databases",
    "Full-Text Search",
    "Temporal Data",
    "Effective-Dated Records",
    "Temporal Join Correctness",
    "ETL",
    "ELT",
    "Incremental Processing",
    "High-Water Marks",
    "Compound Watermarks",
    "Event Time Versus Ingestion Time",
    "Late-Arriving Data",
    "Idempotent Pipelines",
    "Change Data Capture",
    "Data Quality",
    "Testing SQL",
    "Point-in-Time Correct Features",
    "Label Construction",
    "Feature Backfills",
    "Data Contracts",
    "Schema Drift",
    "Lineage",
    "Provenance",
    "End-to-End AI Feature Pipeline Example",
]

missing = [
    concept
    for concept in required_concepts
    if concept not in part11_text
]

if missing:
    raise RuntimeError(
        "Part 11 content validation failed. "
        f"Missing: {missing}"
    )

file_size = NOTEBOOK_PATH.stat().st_size

print("SQL Part 11 appended successfully.")
print(f"Notebook: {NOTEBOOK_PATH}")
print(f"Previous cell count: {start_count}")
print(
    f"Appended cells: "
    f"{len(saved_nb.cells) - start_count}"
)
print(
    f"Final cell count: "
    f"{len(saved_nb.cells)}"
)
print(
    f"File size: "
    f"{file_size / (1024 * 1024):.2f} MB"
)
print(
    "Part 11 marker location:",
    heading_locations(saved_nb, PART11)
)
print("nbformat validation: PASSED")
print("Post-write validation: PASSED")
print("Direct-write mode: PASSED")
print("Temporary notebook created: NO")