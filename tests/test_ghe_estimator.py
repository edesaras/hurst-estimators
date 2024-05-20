import numpy as np
import pytest
from hurst_estimators import ghe_estimator


def test_generalized_hurst_exponent():
    np.random.seed(42)
    X = np.cumsum(np.random.randn(1000))  # Generate synthetic data

    hurst, slope, intercept, log_taus, log_moments = ghe_estimator(X, max_tau=20, q=2.0)

    assert isinstance(hurst, float)
    assert isinstance(slope, float)
    assert isinstance(intercept, float)
    assert len(log_taus) == 20
    assert len(log_moments) == 20

    # Test for known values
    known_hurst = 0.5
    np.random.seed(42)
    X = np.cumsum(
        np.random.randn(10000)
    )  # Generate synthetic data with Hurst exponent 0.5
    hurst, _, _, _, _ = ghe_estimator(X, max_tau=20, q=2.0)
    assert abs(hurst - known_hurst) < 0.1


if __name__ == "__main__":
    pytest.main([__file__])
