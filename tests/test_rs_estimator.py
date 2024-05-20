import pytest
import numpy as np
from hurst_estimators import rs_estimator


def test_rs_estimator():
    X = np.random.randn(1000)  # Generate synthetic data

    hurst, slope, intercept, log_window_sizes, log_rs_values = rs_estimator(X, w=2)

    assert isinstance(hurst, float)
    assert isinstance(slope, float)
    assert isinstance(intercept, float)
    assert isinstance(log_rs_values, np.ndarray)
    assert isinstance(log_window_sizes, np.ndarray)

    # Test for known values
    known_hurst = 0.5
    X = np.random.randn(10000)  # Generate synthetic data with Hurst exponent 0.5
    hurst, _, _, _, _ = rs_estimator(X, w=20)
    assert abs(hurst - known_hurst) < 0.1


if __name__ == "__main__":
    pytest.main([__file__])
