"""Curriculum unit registry.

Each entry defines one *meaningful* study unit. A unit combines every theory
notebook underneath it into a single comprehensive notes document.

Design rules
------------
* ``sources`` are path globs relative to the repository root. When omitted the
  unit uses ``root`` recursively.
* ``exclude`` patterns (regex, matched against the notebook path relative to
  ``root``) drop practice/task/solution/interview material.
* Metadata (title, lede, prerequisites, outcomes, focus) is authored per unit so
  the generated document reads as a designed study guide rather than a dump.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

DEFAULT_EXCLUDE = re.compile(
    r"(^|[/\\])(tasks?|solutions?|practice|assignment|exercise|interview|"
    r"questions?|homework|mock|revision_test)",
    re.IGNORECASE,
)

NAME_EXCLUDE = re.compile(
    r"(^|[_ .-])(task|tasks|solution|solutions|practice|assignment|exercise|"
    r"challenge|interview|question|questions|homework|mock)([_ .-]|$)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Unit:
    key: str
    root: str
    out_stem: str
    title: str
    eyebrow: str
    lede: str
    prerequisites: tuple[str, ...] = ()
    outcomes: tuple[str, ...] = ()
    focus: tuple[str, ...] = ()
    sources: tuple[str, ...] = ()
    exclude: re.Pattern = field(default=DEFAULT_EXCLUDE)
    exclude_name: re.Pattern = field(default=NAME_EXCLUDE)
    order: int = 0

    def is_excluded(self, rel_path: str, name: str) -> bool:
        rel_path = rel_path.replace("\\", "/")
        if self.exclude.search(rel_path):
            return True
        return bool(self.exclude_name.search(name))


UNITS: tuple[Unit, ...] = (
    Unit(
        key="jupyter",
        root="00_Jupyter_Demo",
        out_stem="Jupyter_Demo",
        title="Jupyter Demo: Working Effectively in Notebooks",
        eyebrow="Unit 00 · Tooling",
        lede=(
            "Jupyter is the working surface for this entire course. This unit covers the "
            "execution model, keyboard workflow, cell state, output inspection and the "
            "hygiene rules that keep a notebook reproducible six months later."
        ),
        prerequisites=("A Python 3 installation",),
        outcomes=(
            "Understand the kernel/client split and why cell execution order matters",
            "Navigate and edit cells with confidence in command and edit mode",
            "Inspect and suppress output deliberately instead of by accident",
            "Keep notebooks readable: named cells, markdown structure, reproducible runs",
        ),
        focus=(
            "kernel state and re-execution order",
            "command mode versus edit mode",
            "output and display control",
            "notebook hygiene and reviewability",
        ),
        order=0,
    ),
    Unit(
        key="python-core",
        root="01_Python/01_Python_Core_Fundamentals",
        out_stem="Python_Core_Fundamentals",
        title="Python Core Fundamentals",
        eyebrow="Unit 01 · Python",
        lede=(
            "The syntactic and semantic foundation everything else assumes: how Python "
            "evaluates expressions and statements, how values are printed and read, how "
            "control flow is expressed, and how text is represented and manipulated."
        ),
        prerequisites=("Jupyter familiarity from Unit 00",),
        outcomes=(
            "Use print, input and f-strings with an accurate model of evaluation",
            "Apply every operator category with correct precedence and truthiness",
            "Write reliable if/elif/else and loop logic, including break/continue/pass",
            "Manipulate strings using slicing, methods and formatting rather than ad-hoc code",
        ),
        focus=(
            "expression evaluation and printing",
            "operators, precedence and truthiness",
            "control flow and loop control",
            "string methods, slicing and formatting",
        ),
        order=1,
    ),
    Unit(
        key="python-ds",
        root="01_Python/02_Built_in_Data_Structures",
        out_stem="Python_Built_in_Data_Structures",
        title="Built-in Data Structures and Functions",
        eyebrow="Unit 02 · Python",
        lede=(
            "Lists, tuples, sets and dictionaries are the containers you will use in "
            "essentially every line of data work. This unit covers their semantics, the "
            "cost of their operations, and how function definitions scope and pass data."
        ),
        prerequisites=("Python Core Fundamentals",),
        outcomes=(
            "Choose between list, tuple, set and dict from the access pattern you need",
            "Reason about mutability and aliasing when passing data around",
            "Write functions with clear parameters, defaults and return contracts",
            "Avoid the classic list/tuple aliasing and mutable-default bugs",
        ),
        focus=(
            "container semantics and selection",
            "mutability, aliasing and copying",
            "comprehensions and iteration",
            "function signatures, scope and return values",
        ),
        order=2,
    ),
    Unit(
        key="pythonic",
        root="01_Python/03_Pythonic_Thinking",
        out_stem="Pythonic_Thinking",
        title="Pythonic Thinking: Iterators, Copying and Identity",
        eyebrow="Unit 03 · Python",
        lede=(
            "Idiomatic Python is less about clever syntax and more about the object "
            "model underneath it. This unit covers the iterator protocol, the functional "
            "builtins, shallow versus deep copying, mutability versus immutability, and "
            "how arguments are actually bound."
        ),
        prerequisites=("Built-in Data Structures and Functions",),
        outcomes=(
            "Explain the iterator protocol and write generators that are lazy, not eager",
            "Compose map, filter, zip and reduce for readable data transformations",
            "Distinguish shallow, deep and structural copies and use copy/deepcopy correctly",
            "Bind arguments correctly with *args, **kwargs and keyword-only parameters",
        ),
        focus=(
            "iterator and generator protocol",
            "functional builtins and lazy evaluation",
            "shallow vs deep copy",
            "mutability, immutability and identity",
            "argument binding with *args and **kwargs",
        ),
        order=3,
    ),
    Unit(
        key="python-advanced",
        root="01_Python/04_Python_Advanced",
        out_stem="Python_Advanced",
        title="Advanced Python: OOP, Files, Errors and Decorators",
        eyebrow="Unit 04 · Python",
        lede=(
            "The patterns that turn scripts into maintainable software: object-oriented "
            "design, file handling, structured error handling, and the decorator and "
            "generator mechanisms that underpin most Python frameworks."
        ),
        prerequisites=("Pythonic Thinking", "Functions and scope"),
        outcomes=(
            "Model a domain with classes, encapsulation, inheritance and polymorphism",
            "Read and write files with correct context management and encoding",
            "Design exception hierarchies that fail loudly and fail usefully",
            "Understand and write decorators and generator-based pipelines",
        ),
        focus=(
            "class design, dunder methods and inheritance",
            "file I/O and context managers",
            "exception hierarchies and error strategy",
            "decorators and generators",
        ),
        order=4,
    ),
    Unit(
        key="python-modules",
        root="01_Python/05_Modules_Packages_Environments",
        out_stem="Modules_Packages_Environments",
        title="Modules, Packages and Environments",
        eyebrow="Unit 05 · Python",
        lede=(
            "How code becomes an importable project and how dependencies stay "
            "reproducible across machines. Covers the import system, package layout, "
            "and virtual environment isolation."
        ),
        prerequisites=("Advanced Python",),
        outcomes=(
            "Trace how the import system resolves a module to a file",
            "Lay out a package that others can install and import",
            "Create and use isolated virtual environments",
            "Keep dependencies declared and reproducible",
        ),
        focus=(
            "import machinery and module resolution",
            "package structure and entry points",
            "virtual environments and dependency isolation",
        ),
        order=5,
    ),
    Unit(
        key="numpy",
        root="01_Python/06_Numerical_Computing_NumPy",
        out_stem="NumPy",
        title="Numerical Computing with NumPy",
        eyebrow="Unit 06 · Python",
        lede=(
            "NumPy is the substrate under pandas, scikit-learn and every tensor "
            "operation you will perform. This unit covers the ndarray, dtype and shape "
            "model, vectorisation, indexing, broadcasting and the performance reasoning "
            "that decides whether code scales."
        ),
        prerequisites=("Pythonic Thinking", "Lists and indexing"),
        outcomes=(
            "Create and reshape ndarrays and reason explicitly about shape and dtype",
            "Replace Python loops with vectorised array expressions",
            "Apply broadcasting correctly and debug silent shape bugs",
            "Choose reductions, indexing and memory layouts for large arrays",
        ),
        focus=(
            "ndarray, dtype, shape and strides",
            "array construction and manipulation",
            "vectorisation and broadcasting",
            "indexing, slicing and boolean masks",
            "reductions, performance and memory",
        ),
        order=6,
    ),
    Unit(
        key="pandas",
        root="01_Python/07_Pandas",
        out_stem="Pandas",
        title="Data Analysis with Pandas",
        eyebrow="Unit 07 · Python",
        lede=(
            "Pandas turns a table into something you can interrogate. This unit covers "
            "Series and DataFrame construction, selection and alignment, missing data, "
            "grouping and aggregation, reshaping, merges and joins, and time-aware "
            "indexes."
        ),
        prerequisites=("NumPy",),
        outcomes=(
            "Build and inspect a DataFrame with correct dtypes",
            "Select data with loc, iloc and boolean masks",
            "Handle missing data deliberately rather than silently",
            "Group, aggregate, pivot and reshape with confidence",
            "Join datasets without corrupting row counts",
        ),
        focus=(
            "Series and DataFrame internals",
            "selection, indexing and alignment",
            "missing data and type handling",
            "groupby, aggregation and reshaping",
            "merges, joins and time series indexes",
        ),
        order=7,
    ),
    Unit(
        key="dataviz",
        root="01_Python/08_Data_Visualization",
        out_stem="Data_Visualization",
        title="Data Visualization: Matplotlib, Seaborn and Plotly",
        eyebrow="Unit 08 · Python",
        lede=(
            "A chart is an argument, not decoration. This unit covers building figures "
            "with Matplotlib, statistical graphics with Seaborn, and interactive output "
            "with Plotly, along with the design decisions that make a plot readable."
        ),
        prerequisites=("Pandas",),
        outcomes=(
            "Build and annotate figures directly in Matplotlib",
            "Use Seaborn for distributions, categories and relationships",
            "Add interactivity with Plotly where it earns its keep",
            "Choose encodings that do not mislead",
        ),
        focus=(
            "figure, axes and artist model",
            "plot types and annotations",
            "statistical and categorical plots",
            "interactive charts and design principles",
        ),
        order=8,
    ),
    Unit(
        key="data-analysis",
        root="01_Python/09_Data_Analysis_Process",
        out_stem="Data_Analysis_Process",
        title="The Data Analysis Process",
        eyebrow="Unit 09 · Python",
        lede=(
            "Analysis is a process, not a library call. This unit covers acquiring data, "
            "assessing and cleaning it, running exploratory analysis, and the ETL habits "
            "that make results defensible and repeatable."
        ),
        prerequisites=("Pandas", "Data Visualization"),
        outcomes=(
            "Acquire data from files and sources with provenance in mind",
            "Profile a dataset for quality issues before analysing it",
            "Run exploratory analysis that answers a stated question",
            "Structure ETL steps so results are reproducible",
        ),
        focus=(
            "data acquisition and provenance",
            "data assessment, profiling and cleaning",
            "exploratory analysis workflow",
            "ETL structure and reproducibility",
        ),
        order=9,
    ),
    Unit(
        key="async",
        root="01_Python/11_Async_Parallel_Python",
        out_stem="Async_Parallel_Python",
        title="Async and Parallel Python",
        eyebrow="Unit 11 · Concurrency",
        lede=(
            "When a program waits on I/O, concurrency is the fix; when it waits on the "
            "CPU, parallelism is. This unit covers threads, processes, asyncio and the "
            "decision framework for choosing between them."
        ),
        prerequisites=("Advanced Python", "Functions and callbacks"),
        outcomes=(
            "Distinguish CPU-bound from I/O-bound work",
            "Use threading, multiprocessing and asyncio in the right cases",
            "Explain the GIL and why it constrains Python parallelism",
            "Detect and avoid concurrency hazards such as races and blocking the loop",
        ),
        focus=(
            "CPU-bound vs I/O-bound reasoning",
            "threads and the GIL",
            "multiprocessing and process pools",
            "asyncio, await and event loops",
            "choosing the right concurrency model",
        ),
        order=10,
    ),
    Unit(
        key="production",
        root="01_Python/13_Production_Ready_Mindset",
        out_stem="Production_Ready_Mindset",
        title="Production-Ready Python Mindset",
        eyebrow="Unit 13 · Engineering",
        lede=(
            "Code that only works on the author's machine is not finished. This unit "
            "covers clean readable code, modular design, logging and monitoring habits, "
            "and how to read unfamiliar code deliberately."
        ),
        prerequisites=("Modules, Packages and Environments",),
        outcomes=(
            "Write code that a reviewer can follow without you in the room",
            "Structure projects into modules with clear boundaries",
            "Instrument code with logging instead of print debugging",
            "Approach an unfamiliar codebase systematically",
        ),
        focus=(
            "readability and naming",
            "modularity and project structure",
            "logging, monitoring and observability",
            "reading other people's code",
        ),
        order=11,
    ),
    Unit(
        key="sql",
        root="02-SQL-Databases",
        out_stem="SQL_Databases",
        title="SQL and Relational Databases",
        eyebrow="Unit 02 · Databases",
        lede=(
            "SQL is the interface between your analysis and durable, concurrent, "
            "correctly stored data. This unit covers relational modelling, DDL and "
            "constraints, the full DML/DQL surface, joins, aggregation, subqueries and "
            "window functions, plus transaction and index fundamentals."
        ),
        prerequisites=("Python Core Fundamentals",),
        outcomes=(
            "Design a normalised schema with appropriate keys and constraints",
            "Write correct DDL and DML, including safe ALTER and DELETE patterns",
            "Join tables across keys without dropping or duplicating rows",
            "Aggregate, group and pivot results for reporting",
            "Use subqueries, CTEs and window functions for analytical queries",
            "Reason about transactions, isolation and index usage",
        ),
        focus=(
            "relational modelling, keys and normalisation",
            "DDL, constraints and data types",
            "DML, DQL and filtering",
            "joins and set operations",
            "aggregation, grouping and subqueries",
            "window functions and CTEs",
            "transactions, indexes and query performance",
        ),
        sources=("02-SQL-Databases/SQL_Databases_Complete.ipynb",),
        order=12,
    ),
    Unit(
        key="dsa-intro",
        root="05-DSA-for-AI/01. Introduction to DSA and Python Basics",
        out_stem="DSA_01_Introduction",
        title="Introduction to DSA and Python Basics",
        eyebrow="Unit 05 · DSA",
        lede=(
            "The complexity vocabulary and Python building blocks every later data "
            "structure and algorithm depends on: asymptotic notation, array versus list "
            "behaviour, and the Python primitives used to implement the structures."
        ),
        prerequisites=("Built-in Data Structures and Functions",),
        outcomes=(
            "State time and space complexity in Big-O terms",
            "Explain why Python list append is amortised O(1)",
            "Implement the primitives that later structures build on",
        ),
        focus=("asymptotic analysis", "complexity classes", "Python primitives"),
        order=20,
    ),
    Unit(
        key="dsa-arrays",
        root="05-DSA-for-AI/02. Arrays & Lists",
        out_stem="DSA_02_Arrays_and_Lists",
        title="Arrays and Lists",
        eyebrow="Unit 05 · DSA",
        lede=(
            "The contiguous-memory structure behind almost every other structure. Covers "
            "static versus dynamic arrays, resizing cost, insertion and deletion, and the "
            "trade-offs of Python lists versus fixed-size arrays."
        ),
        prerequisites=("DSA Introduction",),
        outcomes=(
            "Explain amortised cost of append and resize",
            "Implement insert, delete and search on an array",
            "Choose between a Python list and a fixed-size array deliberately",
        ),
        focus=("dynamic array resizing", "insertion and deletion", "array vs list"),
        order=21,
    ),
    Unit(
        key="dsa-strings",
        root="05-DSA-for-AI/03. Strings",
        out_stem="DSA_03_Strings",
        title="Strings",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Strings are immutable sequences, which changes the algorithmic options "
            "available. Covers character storage, pattern matching primitives, anagram "
            "detection and the sliding-window technique."
        ),
        prerequisites=("DSA Introduction", "Python Core Fundamentals"),
        outcomes=(
            "Use character frequency counting for anagrams and duplicates",
            "Apply the sliding-window pattern",
            "Implement common string scanning algorithms",
        ),
        focus=("string internals", "sliding window", "frequency counting", "pattern matching"),
        order=22,
    ),
    Unit(
        key="dsa-linked-lists",
        root="05-DSA-for-AI/04. Linked Lists",
        out_stem="DSA_04_Linked_Lists",
        title="Linked Lists",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Node-based structures trade random access for cheap insertion. Covers singly "
            "and doubly linked lists, insertion and deletion, cycle detection and the "
            "fast/slow pointer technique."
        ),
        prerequisites=("DSA Introduction",),
        outcomes=(
            "Implement singly and doubly linked lists",
            "Insert and delete in O(1) given a reference to the node",
            "Detect cycles and find the middle node with two pointers",
        ),
        focus=("node structure", "insertion and deletion", "cycle detection", "two pointers"),
        order=23,
    ),
    Unit(
        key="dsa-stacks",
        root="05-DSA-for-AI/05. Stacks",
        out_stem="DSA_05_Stacks",
        title="Stacks",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Last-in, first-out access underpins recursion, expression parsing, undo and "
            "monotonic-window algorithms. Covers stack operations, balanced-bracket "
            "validation and monotonic stack patterns."
        ),
        prerequisites=("DSA Introduction", "Linked Lists"),
        outcomes=(
            "Implement a stack and use it for bracket validation",
            "Recognise when a monotonic stack removes a nested loop",
            "Apply stacks to parsing, undo and traversal problems",
        ),
        focus=("stack operations", "balanced brackets", "monotonic stack", "applications"),
        order=24,
    ),
    Unit(
        key="dsa-queues",
        root="05-DSA-for-AI/06. Queues",
        out_stem="DSA_06_Queues",
        title="Queues",
        eyebrow="Unit 05 · DSA",
        lede=(
            "First-in, first-out buffering, including the circular queue and deque "
            "variants that make sliding-window problems linear."
        ),
        prerequisites=("DSA Introduction", "Stacks"),
        outcomes=(
            "Implement a queue, deque and circular queue",
            "Use deque for O(1) sliding-window maximum",
            "Understand when FIFO buffering is the right abstraction",
        ),
        focus=("queue and deque", "circular queue", "sliding window", "applications"),
        order=25,
    ),
    Unit(
        key="dsa-searching",
        root="05-DSA-for-AI/07. Searching",
        out_stem="DSA_07_Searching",
        title="Searching",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Finding a target efficiently: linear and binary search, the conditions that "
            "make binary search valid, and lower-bound variants."
        ),
        prerequisites=("DSA Introduction", "Sorting basics"),
        outcomes=(
            "Implement binary search and state its precondition",
            "Implement lower-bound and insertion-position variants",
            "Choose linear vs binary search from the data's properties",
        ),
        focus=("linear search", "binary search", "lower bound", "search preconditions"),
        order=26,
    ),
    Unit(
        key="dsa-sorting",
        root="05-DSA-for-AI/08. Sorting",
        out_stem="DSA_08_Sorting",
        title="Sorting",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Ordering as a tool for faster downstream work. Covers bubble, selection, "
            "insertion, merge and quicksort, plus stability, in-place behaviour and "
            "Python's built-in sort."
        ),
        prerequisites=("DSA Introduction", "Searching"),
        outcomes=(
            "Implement the core sorts and state their complexities",
            "Explain stability and why it matters for multi-key sorting",
            "Choose a sort from stability, memory and time requirements",
        ),
        focus=("elementary sorts", "merge sort", "quicksort", "stability", "selection"),
        order=27,
    ),
    Unit(
        key="dsa-recursion",
        root="05-DSA-for-AI/09. Recursion",
        out_stem="DSA_09_Recursion",
        title="Recursion",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Solving a problem by decomposing it. Covers base cases, the call stack, "
            "tail recursion, memoisation and the recursion-to-iteration conversion that "
            "avoids stack limits."
        ),
        prerequisites=("Functions", "Stacks"),
        outcomes=(
            "Structure a recursive solution with a correct base case",
            "Explain stack growth and identify when it will overflow",
            "Apply memoisation and convert deep recursion to iteration",
        ),
        focus=("base cases", "call stack", "tail recursion", "memoisation"),
        order=28,
    ),
    Unit(
        key="dsa-hashing",
        root="05-DSA-for-AI/10. Hashing",
        out_stem="DSA_10_Hashing",
        title="Hashing",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Constant-time lookup by trading memory for speed. Covers hash functions, "
            "hash tables, collision strategies, load factor, and how Python's dict and "
            "set are actually built."
        ),
        prerequisites=("DSA Introduction",),
        outcomes=(
            "Explain how a hash table converts a key into an index",
            "Describe separate chaining vs open addressing and the load-factor trade-off",
            "Explain Python dict insertion order and resizing behaviour",
        ),
        focus=("hash functions", "hash tables", "collisions", "load factor", "python dict internals"),
        order=29,
    ),
    Unit(
        key="dsa-problem-solving",
        root="05-DSA-for-AI/11. Problem Solving",
        out_stem="DSA_11_Problem_Solving",
        title="Problem Solving Frameworks",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Knowing algorithms is not the same as being able to select one. This unit "
            "covers pattern recognition, a repeatable approach to unfamiliar problems, "
            "and complexity budgeting."
        ),
        prerequisites=("Arrays", "Hashing", "Recursion", "Sorting"),
        outcomes=(
            "Follow a repeatable process from statement to working code",
            "Recognise common patterns and map them to known algorithms",
            "Estimate complexity before writing an implementation",
        ),
        focus=("pattern recognition", "problem decomposition", "complexity budgeting"),
        order=30,
    ),
    Unit(
        key="dsa-trees",
        root="05-DSA-for-AI/12. Trees",
        out_stem="DSA_12_Trees",
        title="Trees",
        eyebrow="Unit 05 · DSA",
        lede=(
            "Hierarchical structure with logarithmic depth. Covers binary trees, binary "
            "search trees, traversal orders, tree recursion and the invariants that keep "
            "a BST balanced."
        ),
        prerequisites=("Recursion", "Stacks and Queues"),
        outcomes=(
            "Implement tree insertion, search and deletion in a BST",
            "Run preorder, inorder, postorder and level-order traversals",
            "Use recursion naturally for tree problems",
        ),
        focus=("binary trees", "BST invariants", "traversals", "tree recursion", "height"),
        order=31,
    ),
    Unit(
        key="dsa-graphs",
        root="05-DSA-for-AI/13. Graphs",
        out_stem="DSA_13_Graphs",
        title="Graphs",
        eyebrow="Unit 05 · DSA",
        lede=(
            "The generalisation of trees to arbitrary connectivity. Covers adjacency "
            "representations, BFS and DFS, topological sort, connected components, cycle "
            "detection and shortest-path foundations."
        ),
        prerequisites=("Trees", "Queues", "Hashing"),
        outcomes=(
            "Choose between adjacency list and matrix from graph density",
            "Implement BFS and DFS for traversal and shortest unweighted paths",
            "Apply topological sorting to dependency graphs",
            "Detect cycles and find connected components",
        ),
        focus=(
            "graph representations",
            "BFS and DFS",
            "topological sort",
            "connected components and cycle detection",
            "shortest paths",
        ),
        order=32,
    ),
)


UNITS_BY_KEY = {u.key: u for u in UNITS}


def unit_for_path(rel_path: str, name: str) -> Unit | None:
    """Return the most specific unit that owns a notebook."""
    rel = rel_path.replace("\\", "/")
    best: Unit | None = None
    for unit in UNITS:
        root = unit.root.strip("/")
        if rel == root or rel.startswith(root + "/"):
            if best is None or len(unit.root) > len(best.root):
                best = unit
    if best and best.is_excluded(rel, name):
        return None
    return best