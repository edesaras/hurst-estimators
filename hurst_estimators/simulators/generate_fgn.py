import numpy as np
from scipy.fft import ifft


def generate_fgn(length: int, hurst: float, seed: int | None = None) -> np.ndarray:
    """
    Generate a Fractal Gaussian Noise (FGN) sequence of a specified length and Hurst exponent.

    Parameters:
        length (int): Length of the sequence.
        hurst (float): Hurst exponent, H (0 < H < 1).
        seed (int | None): Seed for the random number generator. Default is None.

    Returns:
        np.ndarray: Generated FGN sequence.
    """
    if not (0 < hurst < 1):
        raise ValueError("Hurst exponent must be between 0 and 1")

    if seed is None:
        seed = np.random.randint(np.iinfo(int).max)
    rng = np.random.RandomState(seed)

    # Step 1: Define the autocorrelation sequence
    k = np.arange(0, length)
    exponent = 2 * hurst
    rho = 0.5 * (
        np.abs(k - 1) ** exponent
        - 2 * np.abs(k) ** exponent
        + np.abs(k + 1) ** exponent
    )

    # Step 2: Extend the autocorrelation sequence and compute FFT
    rho = np.concatenate([rho, [0], rho[:0:-1]])
    g = np.fft.fft(rho)

    # Step 3: Calculate eigenvalues (square root of FFT results)
    eigs = np.sqrt(np.maximum(np.real(g), 0))  # Ensure non-negative values

    # Step 4: Generate two independent Gaussian sequences
    m = rng.randn(length)
    n = rng.randn(length)

    # Step 5: Construct the FGN sequence
    w = np.zeros(2 * length, dtype=complex)
    w[0] = eigs[0] * m[0] / np.sqrt(2 * length)
    indices = np.arange(1, length)
    w[indices] = eigs[indices] * (m[indices] + 1j * n[indices]) / np.sqrt(4 * length)
    w[2 * length - indices] = np.conj(w[indices])
    w[length] = eigs[length] * n[0] / np.sqrt(2 * length)

    # Step 6: Perform inverse FFT and take the real part
    fgn = np.real(ifft(w)[:length])
    fgn *= np.sqrt(length) / np.linalg.norm(fgn)  # std normalized to 1
    return fgn
