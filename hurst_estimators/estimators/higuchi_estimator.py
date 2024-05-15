import numpy as np
from scipy.stats import linregress
from typing import Tuple

def higuchi_estimator(
    X: np.ndarray, 
    min_window_size: int, 
    max_window_size: int, 
    *, 
    num_windows: int = 20
) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    """
    Estimates the Hurst exponent of a time series using the Higuchi method.

    Parameters:
        X (np.ndarray): Time series data.
        min_window_size (int): Minimum window size for calculating normalized lengths.
        max_window_size (int): Maximum window size for calculating normalized lengths.
        num_windows (int): Number of window sizes to compute.

    Returns:
        Tuple containing:
            hurst (float): Estimated Hurst exponent.
            slope (float): The slope of the regression line.
            intercept (float): The intercept of the regression line.
            log_window_sizes (np.ndarray): Logarithm of window sizes used in the estimation.
            log_mean_normalized_lengths (np.ndarray): Logarithm of mean normalized lengths corresponding to each window size.
    """
    N = len(X)
    if N < min_window_size:
        raise ValueError("The time series is too short for the specified minimum window size.")
    if min_window_size < 1 or max_window_size < 1:
        raise ValueError("Window sizes must be positive integers.")
    if min_window_size >= max_window_size:
        raise ValueError("min_window_size must be less than max_window_size.")
    if N < max_window_size:
        raise ValueError("The length of the time series must be greater than max_window_size.")
    if num_windows < 2:
        raise ValueError("Number of windows must be at least 2.")

    cumulative_bias = np.cumsum(X - np.mean(X))
    window_sizes = np.unique(np.geomspace(min_window_size, max_window_size, num=num_windows).astype(int))
    log_window_sizes = np.log(window_sizes)

    mean_normalized_lengths = []
    for m in window_sizes:
        normalized_lengths = []
        for k in range(1, m + 1):
            coeff = (N - 1) / ((N - k) // m) / m / m
            if k + m < N:  # Ensure that k+m does not exceed N
                L_k = coeff * np.sum(np.abs(cumulative_bias[k + m::m] - cumulative_bias[k:-m:m]))
                normalized_lengths.append(L_k)
        if normalized_lengths:
            mean_normalized_lengths.append(np.mean(normalized_lengths))
        else:
            mean_normalized_lengths.append(0)  # Add a zero if there are no lengths to average

    log_mean_normalized_lengths = np.log(mean_normalized_lengths)
    slope, intercept, _, _, _ = linregress(log_window_sizes, log_mean_normalized_lengths)
    hurst = slope + 2

    return hurst, slope, intercept, log_window_sizes, log_mean_normalized_lengths
