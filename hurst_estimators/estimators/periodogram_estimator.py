import numpy as np
from scipy.fft import fft
from scipy.signal import welch
from scipy.stats import linregress
from typing import Tuple


def periodogram_estimator(
    X: np.ndarray, method: str = "periodogram", nperseg: int = 256
) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    """
    Estimates the Hurst exponent of a time series using the periodogram or Welch method.

    Parameters:
        X (np.ndarray): Time series data.
        method (str): Method for power spectral density estimation. Options are 'periodogram' and 'welch'.
        nperseg (int): Length of each segment for Welch's method. Default is 256.

    Returns:
        Tuple containing:
            hurst_exponent (float): Estimated Hurst exponent.
            slope (float): Slope of the regression line.
            intercept (float): Intercept of the regression line.
            log_frequencies (np.ndarray): Logarithm of frequencies used for regression.
            log_psd (np.ndarray): Logarithm of power spectrum values corresponding to the frequencies.
    """
    if len(X) < 2:
        raise ValueError("The time series must have at least 2 data points.")

    if method == "periodogram":
        # Compute the power spectrum (periodogram) via FFT
        psd = np.abs(fft(X)) ** 2
        upperbound = len(psd) // 2
        psd = psd[:upperbound]
        frequencies = np.arange(1, upperbound + 1)
    elif method == "welch":
        if nperseg > len(X):
            raise ValueError(
                "nperseg must be less than or equal to the length of the time series."
            )
        frequencies, psd = welch(X, nperseg=nperseg)
        frequencies, psd = frequencies[1:], psd[1:]
    else:
        raise ValueError("Method should be either 'periodogram' or 'welch'")

    # Calculate the frequency vector suitable for log-log regression
    log_psd = np.log(psd)
    log_frequencies = np.log(frequencies)

    # Perform linear regression on the log-log plot of the periodogram
    slope, intercept, _, _, _ = linregress(log_frequencies, log_psd)

    # Calculate the Hurst exponent from the slope
    hurst = (1 - slope) / 2

    return hurst, slope, intercept, log_frequencies, log_psd
