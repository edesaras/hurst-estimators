import numpy as np
from .generate_fbm import generate_fbm


def generate_fgbm(
    length: int,
    hurst: float,
    sigma: float = 1,
    s0: float = 1.0,
    mu: float = None,
    seed: int | None = None,
) -> np.ndarray:
    """
    Generate a Fractional Geometric Brownian Motion (fGBM) sequence.

    Parameters:
        length (int): Length of the sequence.
        hurst (float): Hurst exponent, H (0 < H < 1).
        sigma (float): Volatility term. Default is 1.
        s0 (float): Initial value of the process. Default is 1.0.
        mu (float | None): Drift term. Default is None (no drift).
        seed (int | None): Seed for the random number generator. Default is None.

    Returns:
        np.ndarray: Generated fGBM sequence.
    """
    # Step 1: Generate fBM sequence
    fbm = generate_fbm(length - 1, hurst, seed=seed)

    # Step 2: Apply the exponential transformation to obtain fGBM
    t = np.arange(1, length)
    if mu is None:
        drift = 0.0
    else:
        drift = (mu - 0.5 * sigma**2) * t
    fgbm = s0 * np.exp(drift + sigma * fbm)
    fgbm = np.concatenate([[s0], fgbm])

    return fgbm
