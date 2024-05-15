import numpy as np
from scipy.stats import linregress
from typing import Tuple

def central_estimator(
    X: np.ndarray, 
    max_window_size: int, 
    *, 
    min_window_size: int = 10, 
    r: int = 1, 
    num_sizes: int = 20
) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    """
    Estimate the Hurst exponent of a time series using moments of specified degree.

    Parameters:
        X (np.ndarray): The time series data.
        max_window_size (int): The maximum window size to use for computations.
        min_window_size (int): The minimum window size to use for computations.
        r (int): The degree of the moment to use in the calculation.
        num_sizes (int): The number of different window sizes to use.

    Returns:
        Tuple containing:
            hurst (float): The estimated Hurst exponent.
            slope (float): The slope of the regression line.
            intercept (float): The intercept of the regression line.
            log_sizes (np.ndarray): Logarithms of the window sizes used.
            log_moments (np.ndarray): Logarithms of the computed moments for each window size.
    """
    N = len(X)
    if N < min_window_size:
        raise ValueError("The time series is too short for the specified minimum window size.")
    if max_window_size > N:
        raise ValueError("The maximum window size is greater than the length of the time series.")
    if min_window_size >= max_window_size:
        raise ValueError("min_window_size must be less than max_window_size.")
    if min_window_size < 1 or max_window_size < 1:
        raise ValueError("Window sizes must be positive integers.")
    if num_sizes < 2:
        raise ValueError("Number of sizes must be at least 2.")

    # Create window sizes geometrically spaced
    window_sizes = np.unique(np.geomspace(min_window_size, max_window_size, num=num_sizes).astype(int))
    log_sizes = np.log(window_sizes)
    moments = []

    for window_size in window_sizes:
        n_segments = len(X) // window_size
        X_trimmed = X[:window_size * n_segments]
        X_reshaped = X_trimmed.reshape(n_segments, window_size)
        subseq_avg = X_reshaped.mean(axis=1)
        moments.append((np.abs(subseq_avg - X_trimmed.mean()) ** r).mean())

    log_moments = np.log(moments)

    # Regression to find scaling exponent
    slope, intercept, _, _, _ = linregress(log_sizes, log_moments)
    hurst = 1 + slope / r

    return hurst, slope, intercept, log_sizes, log_moments
