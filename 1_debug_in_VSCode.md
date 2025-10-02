Debugging lets you pause execution, inspect variables, and step through your code to find and fix issues faster. In this assignment you'll set up VS Code for Python debugging, practice with a small script, and learn how to debug Jupyter Notebooks.

## Task 1.1 Install VS Code and extensions

1. Install VS Code: https://code.visualstudio.com/
2. Install the VS Code extensions:
   - `Python` by Microsoft (`ms-python.python`)
   - `Jupyter` by Microsoft (`ms-toolsai.jupyter`)

## Task 1.2 Open the folder and select the Python interpreter

1. Open this assignment in VS Code: 'File' → 'Open Folder...' and select `VSCode_Debug_Assignment/` (e.g., `c:\Users\lkdmc\Desktop\PA1.4\VSCode_Debug_Assignment\`).
2. Press Ctrl+Shift+P → 'Python: Select Interpreter' → choose a Python 3.12 environment that has the packages from `requirements.txt`.
   - If needed, create a virtual environment and install the requirements.

## Task 1.3 Use the included debug script

This repository already contains a tiny example with a bug so you can practice stepping through code.

% Open the existing file `debug_example.py` in this folder (the code is shown below for reference)

```python
# debug_example.py

def compute_ratio(a, b):
    return a / b  # Potential ZeroDivisionError when b == 0


def main():
    values = [1, 2, 3, 0, 4]
    total = 0
    for v in values:
        total += compute_ratio(10, v)
    print("Total:", total)


if __name__ == "__main__":
    main()
```

## Task 1.4 Create a debug configuration (launch.json)

1. Open the 'Run and Debug' view (left sidebar) → 'create a launch.json file' → choose 'Python Debugger (Suggested)' → choose 'Python File' → choose 'Python: Current File'.
2. VS Code creates `.vscode/launch.json`. A minimal configuration will look like:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

## Task 1.5 Set breakpoints and start debugging

1. Open `debug_example.py` and click left of a line number to add a red breakpoint (e.g., on `return a / b`).
2. Start debugging: press F5 or click the green 'Run and Debug' button while `debug_example.py` is active.
3. When execution pauses:
   - Inspect variables in the 'Variables' view.
   - Use the 'Debug Console' to evaluate expressions (e.g., `v`).
   - Use the 'Call Stack' to see how you got here.

## Task 1.6 Step through code

- Use the toolbar:
  - 'Continue' (F5)
  - 'Step Over' (F10): Runs the current line; if it calls a function, executes it without entering and stops at the next line in the same function.
  - 'Step Into' (F11): Enters the called function and pauses at its first line so you can debug inside it.
  - 'Step Out' (Shift+F11)
- Observe how `v` changes and where the exception occurs.

## Task 1.7 Break on exceptions and conditional breakpoints

1. In the 'Breakpoints' view, enable breaking on exceptions ('Raised Exceptions' / 'Uncaught Exceptions').
2. Right-click the breakpoint (in the gutter or in the Breakpoints view) → 'Edit Breakpoint...' → enable 'Expression' and enter a condition:
    - If the breakpoint is inside `compute_ratio()`, use `b == 0` (local parameter in that function).
    - If the breakpoint is on the call line in `main()`, use `v == 0`.
- Common mistakes:
  - Using the wrong variable for the scope: `v` exists in `main()`, `b` exists in `compute_ratio()`.
  - Using `=` instead of `==` in the condition.
  - Writing a condition that never becomes true (then execution never pauses).

 3. Note: If there is no breakpoint yet, right‑click the gutter and some VS Code versions show 'Add Conditional Breakpoint...' to create one directly; otherwise create a breakpoint first, then use 'Edit Breakpoint...'.

 ### Step-by-step (recommended)

1. Open `VSCode_Debug_Assignment/debug_example.py`.
2. Add a breakpoint on `return a / b` inside `compute_ratio()`.
3. Right-click that breakpoint → Edit Breakpoint… → Expression → type `b == 0` → Enter.
4. Press F5. Execution pauses when `b` is 0.
5. In Variables, confirm `a == 10`, `b == 0`. In Debug Console, try `a / (b or 1)` to probe safely.
6. If you prefer to stop at the call site, place a breakpoint on `total += compute_ratio(10, v)` and set condition `v == 0`, then use F11 (Step Into).

### Verify it works

- With exception breakpoints enabled, it also pauses on `ZeroDivisionError` even without a conditional.
- If it never pauses: ensure the breakpoint is enabled, the condition uses the correct variable for that scope, and you started debugging the active file.

## Task 1.8 Debugging a Jupyter Notebook cell

Debug a cell in `debug_notebook.ipynb` using 'Debug Cell' or 'Run by Line'.
1. Open `debug_notebook.ipynb` in this folder.
2. Ensure the Python and Jupyter extensions are installed and the correct kernel (Python 3.12) is selected.
3. Set a breakpoint by clicking in the gutter to the left of a code cell.
4. Use 'Debug Cell' (from the cell toolbar) or 'Run by Line' to step through the cell.
5. Inspect variables and outputs as you go; you can also use the 'Variables' panel and 'Debug Console' during a notebook debug session.

## Task 1.9 Optional: Debug tests (pytest/unittest)

Discover and debug tests from the 'Testing' view.
If you use a test framework:
1. Open the 'Testing' view in VS Code.
2. Configure tests (`pytest` or `unittest`). VS Code will discover tests.
3. Use the gutter actions next to a test ('Run', 'Debug') to debug a single test.

## Task 1.10 Wrap up

Clean up breakpoints and ensure the interpreter matches `requirements.txt`.
- Remove or disable breakpoints when done.
- Keep your interpreter consistent with `requirements.txt`.
- Use conditional breakpoints and exception breakpoints to quickly narrow down issues.
