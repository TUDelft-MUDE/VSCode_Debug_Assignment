# Testing Guide

This repository includes a Python script (`debug_example.py`) and a Jupyter notebook (`debug_notebook.ipynb`). Both have tests you can run with `pytest`. This guide shows how to set up, run, and create tests.

## 1) Requirements
- Windows + PowerShell
- Python 3.12 (per `requirements.txt`)
- VS Code (optional) + Python extension recommended

## 2) Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## 3) Run Tests
- Run all tests:
  ```powershell
  pytest -q
  ```
- Run a specific file:
  ```powershell
  # Python unit test only
  pytest tests/test_debug_example.py -q

  # Notebook test only
  pytest tests/test_debug_notebook.py -q
  ```

## 4) Included Tests
- `tests/test_debug_example.py`
  - Verifies `compute_ratio()` in `debug_example.py`
  - Ensures dividing by zero raises `ZeroDivisionError`
- `tests/test_debug_notebook.py`
  - Executes all cells in `debug_notebook.ipynb` and checks it runs without errors (via `testbook`)
- `test_notebooks.py`
  - Also executes `debug_notebook.ipynb` end-to-end using `testbook`.

## 5) Create New Tests

### A. Python file tests
1. Create a file under `tests/` named `test_<something>.py`.
2. Import your module and assert expected outputs.
3. Example (`tests/test_my_module.py`):
   ```python
   import pytest
   import my_module as mm

   def test_add():
       assert mm.add(2, 3) == 5

   def test_raises_on_zero_division():
       with pytest.raises(ZeroDivisionError):
           mm.divide(1, 0)
   ```

### B. Notebook tests (using `testbook`)
1. Create a file under `tests/` such as `test_my_notebook.py`.
2. Use `testbook` with a path relative to the repo root (where you run `pytest`).
3. To only check that the notebook executes:
   ```python
   from testbook import testbook

   def test_my_notebook_runs():
       with testbook('my_notebook.ipynb', execute=True):
           pass
   ```
4. To assert values from the notebook, expose a variable in a cell and read it with `tb.value(...)`:
   ```python
   from testbook import testbook
   import numpy as np

   def test_my_notebook_outputs_ok():
       with testbook('my_notebook.ipynb', execute=True) as tb:
           result = tb.value('float(my_result)')
           assert np.isclose(result, 42.0, atol=1e-6)
   ```

## 6) VS Code Tips
- Select your virtual environment: Command Palette → "Python: Select Interpreter" → choose `.venv`.
- Install the Python and Test Explorer extensions for easier discovery and running of tests.
- By default, `pytest` auto-discovers tests in the `tests/` folder named `test_*.py`.

## 7) Troubleshooting
- Path errors: Make sure the path in `testbook('...')` is relative to the repo root where you run `pytest`.
- External data/network: Keep notebooks deterministic (avoid randomness and internet calls) to make tests reliable.
- Missing packages: Reinstall with `pip install -r requirements.txt`.

---
Run `pytest -q` now and fix any failures by updating the tests or source code as needed.
