import numpy as np
from hurst_estimators.estimators import periodogram_estimator

def test_periodogram_estimator():
    # Generate synthetic data for testing
    X = np.random.randn(1000)
    
    # Test with valid inputs
    hurst, slope, intercept, log_frequencies, log_periodogram = periodogram_estimator(X)
    
    assert isinstance(hurst, float)
    assert isinstance(log_frequencies, np.ndarray)
    assert isinstance(log_periodogram, np.ndarray)
    assert len(log_frequencies) == len(log_periodogram)
    
    # Check for statistical correctness
    hursts = []
    for _ in range(100):
        X = np.random.randn(1000)
        hurst, slope, intercept, _, _ = periodogram_estimator(X)
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

if __name__ == "__main__":
    test_periodogram_estimator()
    test_periodogram_estimator_edge_cases()
