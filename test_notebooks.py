from testbook import testbook
import numpy as np

def test_cleaning():
    with testbook('6_data_cleaning.ipynb', execute=True) as tb:
        mean_temperature = tb.value('float(mean_temperature)')
        assert np.isclose(mean_temperature, 25.157, atol=1e-3)