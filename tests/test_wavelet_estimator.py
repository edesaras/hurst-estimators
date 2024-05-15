
import numpy as np
from hurst_estimators import wavelet_estimator

def test_wavelet_estimator():
    data = [1, 2, 3, 4, 5]
    result = wavelet_estimator(data)
    assert result is not None
