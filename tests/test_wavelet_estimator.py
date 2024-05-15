import numpy as np
from hurst_estimators.estimators import wavelet_estimator


def test_wavelet_estimator():
    # Generate synthetic data for testing
    X = np.random.randn(1000)

    # Test with valid inputs and method 'awc'
    hurst, slope, intercept, log_scales, log_values = wavelet_estimator(X, method="awc")

    assert isinstance(hurst, float)
    assert isinstance(slope, float)
    assert isinstance(intercept, float)
    assert isinstance(log_scales, np.ndarray)
    assert isinstance(log_values, np.ndarray)
    assert len(log_scales) == len(log_values)

    # Test with valid inputs and method 'vvl'
    hurst, slope, intercept, log_scales, log_values = wavelet_estimator(X, method="vvl")

    assert isinstance(hurst, float)
    assert isinstance(slope, float)
    assert isinstance(intercept, float)
    assert isinstance(log_scales, np.ndarray)
    assert isinstance(log_values, np.ndarray)
    assert len(log_scales) == len(log_values)

    # Check for statistical correctness
    hursts_awc = []
    hursts_vvl = []
    for _ in range(100):
        X = np.random.randn(10000)  # @1000 samples this test is unstable
        hurst_awc, _, _, _, _ = wavelet_estimator(X, method="awc")
        hurst_vvl, _, _, _, _ = wavelet_estimator(X, method="vvl")
        hursts_awc.append(hurst_awc)
        hursts_vvl.append(hurst_vvl)

    # Assert that the mean Hurst exponent is close to 0.5 for white noise
    assert np.abs(np.mean(hursts_awc) - 0.5) < 0.1
    assert np.abs(np.mean(hursts_vvl) - 0.5) < 0.1


def test_wavelet_estimator_edge_cases():
    # Very short time series
    X = np.random.randn(1)
    try:
        wavelet_estimator(X)
        assert False, "Expected ValueError for very short time series"
    except ValueError:
        pass

    # Invalid method
    X = np.random.randn(1000)
    try:
        wavelet_estimator(X, method="invalid")
        assert False, "Expected ValueError for invalid method"
    except ValueError:
        pass


if __name__ == "__main__":
    test_wavelet_estimator()
    test_wavelet_estimator_edge_cases()
