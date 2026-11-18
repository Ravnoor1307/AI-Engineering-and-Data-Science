# Python Curriculum Folder Structure

This document proposes a repository layout for organizing the Python curriculum, learning notes, exercises, datasets, case studies, and projects. It is a recommended structure; it does not move or rename the existing folders.

## Recommended Folder Tree

```text
01_Python/
|-- README.md
|-- Python_Topics.md
|-- Python_Curriculum_Folder_Structure.md
|-- pyproject.toml
|-- requirements.txt
|-- .gitignore
|
|-- 00_Setup_and_Guides/
|   |-- environment_setup.md
|   |-- python_style_guide.md
|   `-- learning_sequence.md
|
|-- 01_Python_Fundamentals/
|   |-- 01_Introduction_and_Syntax/
|   |   |-- notes/
|   |   |-- notebooks/
|   |   `-- exercises/
|   |-- 02_Operators_and_Control_Flow/
|   |-- 03_Strings_and_Text_Processing/
|   |-- 04_Core_Data_Types/
|   |-- 05_Data_Structures_and_Collections/
|   |-- 06_Functions_and_Functional_Programming/
|   |-- 07_Object_Oriented_Programming/
|   |-- 08_Advanced_Python/
|   |-- 09_Modules_Packages_and_Imports/
|   |-- 10_File_Handling_and_Serialization/
|   `-- 11_Standard_Library/
|
|-- 02_Data_Analysis_with_Python/
|   |-- 01_Data_Analysis_Fundamentals/
|   |   |-- notes/
|   |   |-- notebooks/
|   |   |-- exercises/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 02_NumPy/
|   |   |-- 01_Array_Creation_and_Inspection/
|   |   |-- 02_Indexing_and_Broadcasting/
|   |   |-- 03_Vectorization_and_Aggregation/
|   |   |-- datasets/
|   |   |   `-- README.md          # References central dataset IDs and paths
|   |   `-- notebooks/
|   |-- 03_Pandas/
|   |   |-- 01_Series_and_DataFrames/
|   |   |-- 02_Selection_Filtering_and_Sorting/
|   |   |-- 03_GroupBy_and_Aggregation/
|   |   |-- 04_Merge_Join_and_Concatenate/
|   |   |-- 05_Time_Series_and_Text/
|   |   |-- datasets/
|   |   |   `-- README.md
|   |   `-- notebooks/
|   |-- 04_Data_Import_and_Export/
|   |   |-- csv/
|   |   |-- json/
|   |   |-- excel_and_other_formats/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 05_Data_Cleaning_and_Wrangling/
|   |   |-- missing_values/
|   |   |-- duplicates_and_outliers/
|   |   |-- type_conversion_and_validation/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 06_Exploratory_Data_Analysis/
|   |   |-- univariate_analysis/
|   |   |-- bivariate_analysis/
|   |   |-- multivariate_analysis/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 07_Grouping_and_Aggregation/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 08_Time_Series_Analysis/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 09_SQL_for_Data_Analysis/
|   |   |-- 01_SQL_Fundamentals/
|   |   |-- 02_Filtering_and_Sorting/
|   |   |-- 03_Aggregation_and_Grouping/
|   |   |-- 04_Joins_and_Subqueries/
|   |   |-- 05_CTEs_and_Window_Functions/
|   |   |-- 06_SQLite_with_Python/
|   |   |-- 07_SQLAlchemy_Basics/
|   |   |-- datasets/
|   |   |   `-- README.md
|   |   `-- practice_queries/
|   |-- 10_Data_Visualization/
|   |   |-- matplotlib/
|   |   |-- seaborn/
|   |   |-- chart_selection_and_interpretation/
|   |   |-- datasets/
|   |   |   `-- README.md
|   |   `-- dashboard_summaries/
|   |-- 11_Analysis_Reports/
|   |   `-- datasets/
|   |       `-- README.md
|   `-- 12_Analysis_Workflows/
|       |-- notebooks/
|       |-- scripts/
|       |-- reports/
|       `-- datasets/
|           `-- README.md
|
|-- 03_Math_for_Data_Analysis/
|   |-- 01_Algebra_and_Numerical_Foundations/
|   |   |-- notes/
|   |   |-- worked_examples/
|   |   `-- exercises/
|   |-- 02_Probability/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 03_Descriptive_Statistics/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 04_Inferential_Statistics/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 05_Linear_Algebra/
|   |-- 06_Calculus_and_Optimization/
|   `-- 07_Python_Math_Libraries/
|       |-- math_and_statistics/
|       |-- numpy/
|       `-- scipy/
|
|-- 04_Python_Applications/
|   |-- 01_APIs_and_HTTP/
|   |-- 02_Flask/
|   |-- 03_FastAPI/
|   |-- 04_Databases_and_SQLAlchemy/
|   |   |-- 01_SQL_Fundamentals/
|   |   |-- 02_SQLite_and_sqlite3/
|   |   |-- 03_SQLAlchemy_Models_and_Sessions/
|   |   `-- 04_Migrations_and_Repository_Pattern/
|   |-- 05_Async_and_Concurrency/
|   |-- 06_Testing_and_Code_Quality/
|   |-- 07_Security_and_Reliability/
|   |-- 08_Performance_and_Optimization/
|   `-- 09_Development_Tools_and_Workflows/
|
|-- 05_AI_Python_Overview/
|   |-- README.md
|   `-- library_overviews/
|       |-- scikit_learn.md
|       |-- pytorch.md
|       |-- tensorflow_keras.md
|       |-- nlp_and_transformers.md
|       `-- llm_python_tools.md
|
|-- 06_Practice_Questions/
|   |-- 01_Fundamentals/
|   |   |-- questions/
|   |   `-- solutions/
|   |-- 02_Collections_and_Functions/
|   |-- 03_OOP_and_Advanced_Python/
|   |-- 04_Pandas_and_Data_Cleaning/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 05_Analysis_and_Visualization/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 06_SQL_for_Analysis/
|   |   |-- query_challenges/
|   |   |-- datasets/
|   |   |   `-- README.md
|   |   `-- solutions/
|   |-- 07_Math_and_Statistics/
|   |-- 08_APIs_and_Applications/
|   `-- 09_Review_and_Mixed_Problems/
|
|-- 07_Case_Studies/
|   |-- README.md
|   |-- 01_Sales_Analysis/
|   |   |-- brief.md
|   |   |-- dataset_info.md
|   |   |-- datasets/
|   |   |   `-- README.md
|   |   |-- notebooks/
|   |   `-- findings/
|   |-- 02_Student_Performance/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 03_Ecommerce_and_Customers/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 04_Employee_and_HR/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 05_Finance_and_Expenses/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 06_Healthcare/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 07_Inventory_and_Supply/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 08_Website_and_Social_Analytics/
|   |   `-- datasets/
|   |       `-- README.md
|   |-- 09_Weather_and_Time_Series/
|   |   `-- datasets/
|   |       `-- README.md
|   `-- 10_Transportation_and_Travel/
|       `-- datasets/
|           `-- README.md
|
|-- 08_Projects/
|   |-- README.md
|   |-- 01_Intermediate/
|   |   |-- data_analysis/
|   |   |   `-- sales_dashboard/
|   |   |       `-- datasets/
|   |   |           `-- README.md
|   |   |-- automation/
|   |   |   `-- file_organizer/
|   |   `-- applications_and_apis/
|   |       `-- task_manager_api/
|   |-- 02_Advanced/
|   |   |-- analytics_applications/
|   |   |   `-- ecommerce_analytics/
|   |   |       `-- datasets/
|   |   |           `-- README.md
|   |   |-- data_pipelines/
|   |   |   `-- automated_etl/
|   |   |       `-- datasets/
|   |   |           `-- README.md
|   |   `-- AI_and_API_integrations/
|   |       `-- document_assistant/
|   `-- 03_Expert/
|       |-- scalable_data_systems/
|       |   `-- distributed_data_processing/
|       |       `-- datasets/
|       |           `-- README.md
|       |-- production_python_services/
|       |   `-- monitored_inference_service/
|       `-- advanced_AI_applications/
|           `-- evaluated_rag_platform/
|
|-- 09_Datasets/
|   |-- 
|   |-- pandas/README.md
|   |-- visualization/README.md
|   |-- sql/README.md
|   |-- statistics/README.md
|   |-- processed/README.md
|       
|-- 10_References/
|   |-- official_documentation.md
|   `-- useful_resources.md
|
`-- tests/
    |-- fundamentals/
    |-- data_analysis/
    `-- applications/
```

## Organization Guidelines

### Learning order

- Follow the numbered sequence: Python fundamentals, data analysis with Python, then mathematics for data analysis.
- Learn practical analysis workflows with datasets before studying the supporting math topics in depth.
- Study SQL within the data-analysis stage, then revisit database integration when learning Python applications.
- The folder names and order match the learning sequence in `Python_Topics.md`.

### Concepts and exercises

- Keep explanations and concept notebooks beside the topic they teach.
- Use consistent numbering so folders follow the learning sequence.
- For each topic folder, use consistent subfolders such as `notes/`, `notebooks/`, `exercises/`, and `solutions/` where applicable.
- Put topic-specific exercises in the matching topic folder when they are part of learning that concept.
- Use `06_Practice_Questions/` for cumulative, mixed-topic, or revision problem sets.
- Keep SQL concepts, query exercises, and Python database integration under the data-analysis and applications folders shown above.

### Dataset organization

- Build a catalog of approximately 100–150 datasets over the full data-analysis curriculum.
- Record each dataset's name, source URL, license, subject, row count, file type, and concepts practiced in `dataset_catalog.csv`.
- Store every actual downloaded dataset file only in the main `09_Datasets/` directory, arranged by size and subject.
- In every lesson, exercise, case study, or project that uses a dataset, add a local `datasets/README.md` or `dataset_info.md` that lists the dataset ID and its path inside `09_Datasets/`.
- These local `datasets/` folders contain only references and instructions, never duplicate copies of the data files.
- Load the central file by its documented path; do not copy the same dataset into topic, practice, case-study, or project folders.
- Categorize local datasets by size:
  - Small: 100–1,000 rows
  - Medium: 30,000–100,000 rows
  - Large: 500,000–1,000,000 rows
- Keep original downloads separate from cleaned or transformed files.
- Keep notebooks, exercises, solutions, and reports in their relevant learning folders. Save reusable processed data under `09_Datasets/processed/` and record it in the catalog.
- Do not commit large datasets or restricted data to Git. Add local data paths to `.gitignore` and document download instructions.

### Case studies and projects

- Use `07_Case_Studies/` for guided, question-led analysis that applies completed concepts.
- Give each case study its own folder containing a problem brief, dataset instructions, notebook or scripts, and findings.
- Use `08_Projects/` for larger end-to-end builds, separated into intermediate, advanced, and expert levels.
- Include a `README.md`, source code, tests, configuration example, and usage instructions in each substantial project.
- Keep secrets, private data, generated files, and environment-specific configuration out of version control.

## Suggested Contents for a Topic Folder

```text
02_Pandas/
|-- README.md
|-- notes.md
|-- notebooks/
|-- exercises/
|-- solutions/
|-- datasets/
|   `-- README.md         # References only; data files stay under 09_Datasets/
`-- tests/
```

Example `datasets/README.md` entry:

```text
Dataset ID: sales_small_001
Canonical file: 09_Datasets/raw/small_100_to_1000_rows/pandas/sales_small_001.csv
Used for: CSV loading, filtering, grouping, and summary statistics
Source and license: See the matching row in 09_Datasets/dataset_catalog.csv
```

## Suggested Contents for a Case Study or Project Folder

```text
sales_analysis/
|-- README.md             # Goal, setup, run instructions, and conclusions
|-- dataset_info.md       # References only; actual files stay under 09_Datasets/
|-- notebooks/
|-- src/
|-- tests/
|-- reports/
`-- requirements.txt      # Or use the shared pyproject.toml
```

## Naming Conventions

- Use numbered `snake_case` directory names to preserve the learning order.
- Use descriptive filenames, such as `pandas_groupby_exercises.ipynb`.
- Keep notebooks focused on one concept or task.
- Name solutions to match their exercises, for example `pandas_groupby_solutions.ipynb`.
- Prefer a shared environment and dependency file for the curriculum; add project-specific dependencies only when needed.
