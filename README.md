# Expense Calculator

Small Python project that keeps a list of expenses, calculates the total with a tax rate per category, and saves/loads the list as JSON. It is a learning project for Software Engineering Assignment #05 (AI-assisted repository customization and risk review).

## Features
- `add_expense(expenses, name, amount, category)` adds one expense. The amount must be a positive number, otherwise `ValueError` is raised.
- `total_with_tax(expenses)` returns the total with tax. Tax is chosen by category (names are case-insensitive):

| Category | Tax |
|---|---|
| food | 5% |
| transport | 10% |
| entertainment | 20% |
| any other | 0% |

- `save_to_file(expenses, path)` and `load_from_file(path)` write and read a JSON file (default `expenses.json`).

## Project structure
```
expense_calc.py        - the only module, entry point is main()
test_expense_calc.py   - pytest tests
AGENTS.md              - rules for AI coding agents (safe/forbidden actions)
requirements.txt       - pinned dev dependencies (pytest, ruff, mypy)
.gitignore             - ignores .venv, caches and expenses.json
```

## Setup (Windows PowerShell)
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
On macOS/Linux activate with `source .venv/bin/activate`. Tested with Python 3.11.

## Run
```
python expense_calc.py
```
Runs a small demo and writes `expenses.json`.

## Test and checks
```
pytest -v
ruff check .
mypy expense_calc.py
```

## Known limitations
- Loading a corrupted JSON file raises `JSONDecodeError` (not handled).
- Unknown categories are taxed at 0% without a warning.
- No CI pipeline.

## Working with AI agents
Read `AGENTS.md` before using a coding agent: it lists safe commands, forbidden actions and review gates.
