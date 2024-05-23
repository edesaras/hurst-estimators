import numpy as np
from .generate_fgn import generate_fgn


def generate_fbm(length: int, hurst: float, seed: int | None = 42) -> np.ndarray:
    """
    Generate a Fractional Brownian Motion (fBM) sequence of a specified length and Hurst exponent.

    Parameters:
        length (int): Length of the sequence.
        hurst (float): Hurst exponent, H (0 < H < 1).
        seed (int | None): Seed for the random number generator. Default is 42.

    Returns:
        np.ndarray: Generated fBM sequence.
    """
    # Step 1: Generate fGN sequence
    fgn = generate_fgn(length, hurst, seed=seed) / np.sqrt(length)

    # Step 2: Compute the cumulative sum to obtain fBM
    fbm = np.cumsum(fgn)
    fbm -= fbm[0]  # Normalize to start at zero

    return fbm
