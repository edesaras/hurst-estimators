import numpy as np
import pywt
from scipy.stats import linregress
from typing import Tuple


def wavelet_estimator(
    X: np.ndarray, method: str = "awc", wavelet: str = "db1"
) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    """
    Estimates the Hurst exponent using specified methods: 'awc' (Average Wavelet Coefficients)
    or 'vvl' (Variance Versus Level).

    Parameters:
        X (np.ndarray): Time series data.
        method (str): Estimation method, either 'awc' for average wavelet coefficients
                      or 'vvl' for variance versus level.
        wavelet (str): Type of wavelet to use, default 'db1'.

    Returns:
        Tuple containing:
            hurst (float): Estimated Hurst exponent.
            slope (float): The slope of the regression line.
            intercept (float): The intercept of the regression line.
            log_scales (np.ndarray): Logarithm of scales or levels.
            log_values (np.ndarray): Logarithm of mean or variance of wavelet coefficients.

    Raises:
        ValueError: If the method is not 'awc' or 'vvl'.
    """
    if len(X) < 2:
        raise ValueError("The time series must have at least 2 data points.")

    coeffs = pywt.wavedec(X, wavelet)
    if method == "awc":
        values = [np.mean(np.abs(c)) for c in coeffs]
    elif method == "vvl":
        values = [np.var(np.abs(c)) for c in coeffs]
    else:
        raise ValueError("Method must be either 'awc' or 'vvl'.")

    log_values = np.log(values)
    log_scales = np.arange(len(log_values))

    slope, intercept, _, _, _ = linregress(log_scales, log_values)
    if method == "awc":
        hurst = slope + 0.5  # diverged from the paper in the sign
    elif method == "vvl":
        hurst = (slope + 1) / 2  # diverged from the paper in the sign

    return hurst, slope, intercept, log_scales, log_values
