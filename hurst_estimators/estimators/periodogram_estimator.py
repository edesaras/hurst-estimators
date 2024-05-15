import numpy as np
from scipy.fft import fft
from scipy.stats import linregress
from typing import Tuple


def periodogram_estimator(X: np.ndarray) -> Tuple[float, np.ndarray, np.ndarray]:
    """
    Estimates the Hurst exponent of a time series using the periodogram method.

    Parameters:
        X (np.ndarray): Time series data.

    Returns:
        Tuple containing:
            hurst_exponent (float): Estimated Hurst exponent.
            log_frequencies (np.ndarray): Logarithm of frequencies used for regression.
            log_periodogram (np.ndarray): Logarithm of power spectrum values corresponding to the frequencies.
    """
    if len(X) < 2:
        raise ValueError("The time series must have at least 2 data points.")

    # Compute the power spectrum (periodogram) via FFT
    periodogram = np.abs(fft(X)) ** 2
    upperbound = len(periodogram) // 2
    periodogram = periodogram[:upperbound]
    log_periodogram = np.log(periodogram)

    # Calculate the frequency vector suitable for log-log regression
    frequencies = np.arange(1, upperbound + 1)
    log_frequencies = np.log(4 * np.sin(frequencies * np.pi / len(X)) ** 2)

    # Perform linear regression on the log-log plot of the periodogram
    slope, intercept, _, _, _ = linregress(log_frequencies, log_periodogram)

    # Calculate the Hurst exponent from the slope
    hurst = (1 - slope) / 2

    return hurst, slope, intercept, log_frequencies, log_periodogram
