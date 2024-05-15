import numpy as np
from hurst_estimators.estimators import higuchi_estimator

def test_higuchi_estimator():
    # Generate synthetic data for testing
    X = np.random.randn(1000)
    
    # Test with valid inputs
    hurst, slope, intercept, log_window_sizes, log_mean_normalized_lengths = higuchi_estimator(X, min_window_size=10, max_window_size=100)
    
    assert isinstance(hurst, float)
    assert isinstance(slope, float)
    assert isinstance(intercept, float)
    assert isinstance(log_window_sizes, np.ndarray)
    assert isinstance(log_mean_normalized_lengths, np.ndarray)
    assert len(log_window_sizes) == len(log_mean_normalized_lengths)
    
    # Check for correctness
    # Statistically speaking this might evaluate false eventhough the implementation is correct
    hursts = []
    for _ in range(100):
        X = np.random.randn(1000)
        hurst, _, _, _, _ = higuchi_estimator(X, min_window_size=10, max_window_size=100)
        hursts.append(hurst)
    assert np.abs(np.mean(hursts) - 0.5) < 0.1

def test_higuchi_estimator_edge_cases():
    # Very short time series
    X = np.random.randn(5)
    try:
        higuchi_estimator(X, min_window_size=7, max_window_size=12)
        assert False, "Expected ValueError for very short time series"
    except ValueError:
        pass

    # Invalid window sizes
    try:
        higuchi_estimator(X, min_window_size=-1, max_window_size=5)
        assert False, "Expected ValueError for invalid min_window_size"
    except ValueError:
        pass

    try:
        higuchi_estimator(X, min_window_size=5, max_window_size=-1)
        assert False, "Expected ValueError for invalid max_window_size"
    except ValueError:
        pass

if __name__ == "__main__":
    test_higuchi_estimator()
    test_higuchi_estimator_edge_cases()
