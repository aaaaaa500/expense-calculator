# AGENTS.md

## Purpose
Small Python expense calculator. It stores a list of expenses (name, amount, category),
calculates the total with a tax rate per category, and saves/loads the list as JSON.
It is a learning project for Software Engineering Assignment #05.

## Architecture
- `expense_calc.py` - the only module. Functions: `add_expense`, `total_with_tax`,
  `save_to_file`, `load_from_file`, `main` (entry point, small demo run).
- `test_expense_calc.py` - pytest tests for the functions above.
- Data format: a list of dicts `{"name": str, "amount": number, "category": str}`.
- Tax rates: food 5%, transport 10%, entertainment 20%, any other category 0%.
- Only the standard library `json` is used. `pytest` is used for tests only.

## Setup (Windows PowerShell)
```
python -m venv .venv
.venv\Scripts\activate
pip install pytest ruff mypy
```

## Safe commands (allowed without asking)
- `pytest -v`
- `ruff check .`
- `mypy expense_calc.py`
- `python expense_calc.py` (writes `expenses.json`, which is git-ignored)
- `git status`, `git diff`, `git log --oneline`

## Ask the human first
- Installing or upgrading any dependency (`pip install ...`)
- Creating, renaming or deleting files
- `git commit` and `git push`
- Any change to the tax rates or the data format

## Forbidden actions
- Never read, write or print secrets, tokens, passwords or real personal data.
- Never deploy to production or touch any remote service.
- Never run destructive commands (`rm -rf`, `Remove-Item -Recurse`, `git reset --hard`,
  `git push --force`, `git clean`).
- Never add or change dependencies without human review.
- Never edit tests only to make them pass; never fake or invent test results.
- Never change files outside this repository folder.

## Coding conventions
- Python 3.11, 4-space indentation, small functions with one job.
- Imports sorted (`ruff check .` must be clean).
- Add a short comment in English for each new function.
- Do not use `from module import *` in project code.
- Keep changes small: one change per commit, with a clear message.

## Test expectations
- Every behavior change needs a new or updated test in `test_expense_calc.py`.
- Run `pytest -v`, `ruff check .` and `mypy expense_calc.py` before saying a task is done.
- Report the real command output (pass/fail counts). If a check was not run, say so.

## Acceptance criteria (must stay true after any change)
1. `add_expense` adds exactly one item to the list.
2. `total_with_tax` applies 5% to food, 10% to transport, 20% to entertainment, 0% to others.
3. Saving and then loading a file returns the same list.
4. All tests pass with `pytest -v`.

## Review gates
- A human reads the full diff before any commit.
- A human approves any new dependency, deleted file or changed acceptance criterion.