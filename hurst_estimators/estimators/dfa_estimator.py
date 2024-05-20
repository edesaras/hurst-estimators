import numpy as np
from scipy.stats import linregress
from typing import Tuple
from hurst_estimators.utils import search_opt_seq_len, _gen_sbpf


def dfa_estimator(
    X: np.ndarray,
    w: int,
    *,
    alpha: float = 0.99,
) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    """
    Estimate the Hurst exponent using Detrended Fluctuation Analysis (DFA).

    Parameters:
        X (np.ndarray): The time series data.
        w (int): The window size for calculating the fluctuation function.
        alpha (float): The percentage for the starting point of the search (default is 0.99).

    Returns:
        Tuple containing:
            hurst (float): Estimated Hurst exponent.
            slope (float): The slope of the regression line.
            intercept (float): The intercept of the regression line.
            log_window_sizes (np.ndarray): Logarithm of window sizes used in the estimation.
            log_fluctuations (np.ndarray): Logarithm of fluctuations corresponding to each window size.
    """
    N = len(X)
    Nopt = search_opt_seq_len(N, w, alpha=alpha)
    T = sorted(_gen_sbpf(Nopt, w))
    n = len(T)

    S = np.zeros(n)
    X_opt_bar = np.mean(X[:Nopt])
    Z = np.cumsum(X[:Nopt] - X_opt_bar)

    for idx, m in enumerate(T):
        k = Nopt // m
        segments = Z[:Nopt].reshape(k, m)
        x = np.arange(1, m + 1)
        # Create the design matrix for linear regression
        A = np.vstack([x, np.ones(m)]).T

        # Perform linear regression for each segment
        poly_coeffs = np.linalg.lstsq(A, segments.T, rcond=None)[0]
        trends = A @ poly_coeffs
        detrended = segments - trends.T
        stdev = np.std(detrended, axis=1)

        S[idx] = np.mean(stdev)

    log_window_sizes = np.log(T)
    log_fluctuations = np.log(S)
    slope, intercept, _, _, _ = linregress(log_window_sizes, log_fluctuations)
    hurst = slope

    return hurst, slope, intercept, log_window_sizes, log_fluctuations
