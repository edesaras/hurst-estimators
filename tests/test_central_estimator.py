import numpy as np
from hurst_estimators.estimators import central_estimator


def test_central_estimator():
    # Generate synthetic data for testing
    X = np.random.randn(1000)

    # Test with valid inputs
    hurst, slope, intercept, log_sizes, log_moments = central_estimator(
        X, max_window_size=100
    )

    assert isinstance(hurst, float)
    assert isinstance(slope, float)
    assert isinstance(intercept, float)
    assert isinstance(log_sizes, np.ndarray)
    assert isinstance(log_moments, np.ndarray)
    assert len(log_sizes) == len(log_moments)

    # Check for correctness
    # Statistically speaking this might evaluate false eventhough the implementation is correct
    hursts = []
    for _ in range(100):
        X = np.random.randn(1000)
        hurst, _, _, _, _ = central_estimator(X, max_window_size=100)
        hursts.append(hurst)
    assert np.abs(np.mean(hursts) - 0.5) < 0.1


def test_central_estimator_edge_cases():
    # Very short time series
    X = np.random.randn(5)
    try:
        central_estimator(X, max_window_size=10, min_window_size=6)
        assert False, "Expected ValueError for very short time series"
    except ValueError:
        pass

    # Invalid window sizes
    try:
        central_estimator(X, max_window_size=-1)
        assert False, "Expected ValueError for invalid max_window_size"
    except ValueError:
        pass

    try:
        central_estimator(X, max_window_size=5, min_window_size=-1)
        assert False, "Expected ValueError for invalid min_window_size"
    except ValueError:
        pass


if __name__ == "__main__":
    test_central_estimator()
    test_central_estimator_edge_cases()
