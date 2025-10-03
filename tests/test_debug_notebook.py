from testbook import testbook


def test_debug_notebook_runs():
    # Executes all cells in the notebook to ensure it runs without errors
    with testbook('debug_notebook.ipynb', execute=True):
        pass
