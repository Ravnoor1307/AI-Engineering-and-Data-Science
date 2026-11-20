# AI Engineering and Data Science Roadmap

A structured study workspace for Python, data science, machine learning, and AI engineering. The repository is organized into numbered folders, with an expanded AI Engineering track under `18_AI_Engineering/`.

## Folder structure

- `01_Python/` through `19_DSA/`: ordered study areas
- `18_AI_Engineering/`: software fundamentals through AI system design, LLMOps, fine-tuning, projects, and interview preparation
- `Projects/`: standalone portfolio and practice projects

Each AI Engineering level includes folders for notes, session work, code, tests and evaluations, the level project, and resources.

## Setup

Python 3.10 or newer is recommended.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

To start JupyterLab:

```powershell
jupyter lab
```

## Recommended workflow

1. Read the relevant level `README.md`.
2. Store session work using the level's session naming convention.
3. Keep reusable implementation in the level `03_Code/` folder.
4. Record checks and evaluations in `04_Tests_and_Evaluations/`.
5. Keep the level capstone or outcome in `05_Level_Project/`.

## Environment variables

Do not commit API keys or credentials. Store local values in a `.env` file. Example variables include:

```text
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
HUGGINGFACE_API_KEY=
```
