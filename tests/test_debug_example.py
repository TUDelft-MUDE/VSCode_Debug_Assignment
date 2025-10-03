import pytest

import debug_example as de


def test_compute_ratio_basic():
    assert de.compute_ratio(10, 2) == 5
    assert de.compute_ratio(9, 3) == 3


def test_compute_ratio_zero_division():
    with pytest.raises(ZeroDivisionError):
        de.compute_ratio(1, 0)
