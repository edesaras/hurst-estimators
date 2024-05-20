import numpy as np
from scipy.stats import linregress
from typing import Tuple


def ghe_estimator(
    X: np.ndarray, max_tau: int = 20, *, q: float = 2.0
) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    """
    Estimates the Generalized Hurst exponent of a time series using the q-th order moments.

    Parameters:
        X (np.ndarray): Time series data.
        q (float): Order of the moments.
        max_tau (int): Maximum time lag.

    Returns:
        float: Estimated Hurst exponent.
        List[float]: Logarithm of time lags.
        List[float]: Logarithm of q-th order moments.
    """
    N = len(X)
    taus = np.arange(1, max_tau + 1)
    moments = []

    for tau in taus:
        diffs = np.abs(X[tau:] - X[:-tau])  # Differences for lag tau
        moments.append(np.mean(diffs**q))  # q-th order moment

    log_taus = np.log(taus)
    log_moments = np.log(moments)

    # Perform linear regression
    slope, intercept, _, _, _ = linregress(log_taus, log_moments)
    hurst_exponent = slope / q

    return hurst_exponent, slope, intercept, log_taus, log_moments
