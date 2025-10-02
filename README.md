# VS Code Debugging Assignment

This repository contains a small Python project to learn and practice debugging in Visual Studio Code (VS Code) for both scripts and Jupyter Notebooks.

- Main guide: see `1_debug_in_VSCode.md` for detailed, step‑by‑step instructions.
- Practice files: `debug_example.py` and `debug_notebook.ipynb`.

## Prerequisites

- VS Code installed: https://code.visualstudio.com/
- Extensions:
  - Python (ms-python.python)
  - Jupyter (ms-toolsai.jupyter)
- Python 3.12 with the packages from `requirements.txt`.

## Setup

1. Open this folder in VS Code: `File` → `Open Folder...` → select `VSCode_Debug_Assignment/`.
2. Select interpreter: `Ctrl+Shift+P` → `Python: Select Interpreter` → choose a Python 3.12 environment.
3. Install dependencies (if needed):
   ```bash
   pip install -r requirements.txt
   ```

## Quick start: debug the script

1. Open `debug_example.py`.
2. Create a launch config: `Run and Debug` → `create a launch.json` → Python.
3. Set a breakpoint (e.g., on `return a / b`).
4. Start debugging with F5, step through, inspect variables, and observe the `ZeroDivisionError` case.

## Debugging a Notebook

1. Open `debug_notebook.ipynb`.
2. Select the correct kernel (Python 3.12).
3. Use `Debug Cell` or `Run by Line`, set breakpoints in the gutter, and inspect variables.

## Tasks (summary)

Use `1_debug_in_VSCode.md` for the full walkthrough of each task.

- Install VS Code and extensions.
- Open the folder and select the Python interpreter.
- Use and debug `debug_example.py` (breakpoints, step into/over/out, exception/conditional breakpoints).
- Create a `launch.json` for Python debugging.
- Debug a cell in `debug_notebook.ipynb`.
- Optional: discover and debug tests from the Testing view.

## Repository contents

- `debug_example.py`: small script with a deliberate bug for practice.
- `debug_notebook.ipynb`: notebook to practice cell debugging.
- `1_debug_in_VSCode.md`: detailed instructions for all steps.
- `requirements.txt`: Python dependencies.
- `LICENSE`, `CITATION.cff`: licensing and citation info.

## Tips

- Use exception breakpoints to stop on errors automatically.
- Prefer conditional breakpoints to pause only on interesting cases (e.g., `b == 0`).
- Keep your interpreter consistent with `requirements.txt`.

---

For details, follow `1_debug_in_VSCode.md`.
