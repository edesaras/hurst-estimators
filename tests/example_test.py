import numpy as np
from hurst_estimators import example_func

def test_example():
    x = np.arange(0, 10, .5)
    assert np.allclose(example_func(x), 2 * x)
