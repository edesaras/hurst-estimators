import numpy as np
from hurst_estimators.estimators import periodogram_estimator


def test_periodogram_estimator():
    # Generate synthetic data for testing
    X = np.random.randn(1000)

    # Test with valid inputs using periodogram method
    hurst, slope, intercept, log_frequencies, log_psd = periodogram_estimator(
        X, method="periodogram"
    )

    assert isinstance(hurst, float)
    assert isinstance(log_frequencies, np.ndarray)
    assert isinstance(log_psd, np.ndarray)
    assert len(log_frequencies) == len(log_psd)

    # Test with valid inputs using Welch's method
    hurst, slope, intercept, log_frequencies, log_psd = periodogram_estimator(
        X, method="welch", nperseg=256
    )

    assert isinstance(hurst, float)
    assert isinstance(log_frequencies, np.ndarray)
    assert isinstance(log_psd, np.ndarray)
    assert len(log_frequencies) == len(log_psd)

    # Check for statistical correctness of periodogram
    hursts = []
    for _ in range(100):
        X = np.random.randn(1000)
        hurst, slope, intercept, _, _ = periodogram_estimator(X, method="periodogram")
        hursts.append(hurst)

    # Assert that the mean Hurst exponent is close to 0.5 for white noise
    assert np.abs(np.mean(hursts) - 0.5) < 0.1

    # Check for statistical correctness of welches method
    hursts = []
    for _ in range(100):
        X = np.random.randn(1000)
        hurst, slope, intercept, _, _ = periodogram_estimator(
            X, method="welch", nperseg=64
        )
        hursts.append(hurst)

    # Assert that the mean Hurst exponent is close to 0.5 for white noise
    assert np.abs(np.mean(hursts) - 0.5) < 0.1


def test_periodogram_estimator_edge_cases():
    # Very short time series
    X = np.random.randn(1)
    try:
        periodogram_estimator(X)
        assert False, "Expected ValueError for very short time series"
    except ValueError:
        pass

    # Invalid method
    X = np.random.randn(1000)
    try:
        periodogram_estimator(X, method="invalid_method")
        assert False, "Expected ValueError for invalid method"
    except ValueError:
        pass

    # Invalid nperseg for Welch method
    try:
        periodogram_estimator(X, method="welch", nperseg=2000)
        assert False, "Expected ValueError for invalid nperseg"
    except ValueError:
        pass


if __name__ == "__main__":
    test_periodogram_estimator()
    test_periodogram_estimator_edge_cases()
