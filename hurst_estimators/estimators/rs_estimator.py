import numpy as np
from scipy.stats import linregress
from typing import Tuple
from hurst_estimators.utils import search_opt_seq_len, _gen_sbpf


def rs_estimator(
    X: np.ndarray,
    w: int,
    *,
    alpha: float = 0.99,
) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    """
    Estimate the Hurst exponent using Rescaled Range Analysis (R/S Analysis).

    Parameters:
        X (np.ndarray): The time series data.
        w (int): The window size for calculating the rescaled range.
        alpha (float): The percentage for the starting point of the search (default is 0.99).

    Returns:
        Tuple containing:
            hurst (float): Estimated Hurst exponent.
            slope (float): The slope of the regression line.
            intercept (float): The intercept of the regression line.
            log_window_sizes (np.ndarray): Logarithm of window sizes used in the estimation.
            log_rs_values (np.ndarray): Logarithm of rescaled range values corresponding to each window size.
    """
    N = len(X)
    Nopt = search_opt_seq_len(N, w, alpha=alpha)
    T = sorted(_gen_sbpf(Nopt, w))
    n = len(T)

    RS = np.zeros(n)

    for idx, m in enumerate(T):
        k = Nopt // m
        segments = np.array([X[j * m : (j + 1) * m] for j in range(k)])
        means = np.mean(segments, axis=1, keepdims=True)
        Z = np.cumsum(segments - means, axis=1)
        R = np.ptp(Z, axis=1)
        S = np.std(segments, axis=1, ddof=1)
        RS[idx] = np.mean(R / S)

    log_window_sizes = np.log(T)
    log_rs_values = np.log(RS)
    slope, intercept, _, _, _ = linregress(log_window_sizes, log_rs_values)
    hurst = slope

    return hurst, slope, intercept, log_window_sizes, log_rs_values
