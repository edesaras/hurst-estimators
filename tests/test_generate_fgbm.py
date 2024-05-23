import numpy as np
from hurst_estimators.simulators import generate_fgbm


def test_generate_fgbm():
    length = 1000
    hurst = 0.7
    sigma = 1
    s0 = 1.0
    mu = 0.05
    seed = 42

    fgbm = generate_fgbm(length, hurst, sigma=sigma, s0=s0, mu=mu, seed=seed)

    assert isinstance(fgbm, np.ndarray)
    assert len(fgbm) == length
    assert fgbm[0] == s0


def test_generate_fgbm_no_drift():
    length = 1000
    hurst = 0.7
    sigma = 1
    s0 = 1.0
    seed = 42

    fgbm = generate_fgbm(length, hurst, sigma=sigma, s0=s0, seed=seed)

    assert isinstance(fgbm, np.ndarray)
    assert len(fgbm) == length
    assert fgbm[0] == s0


def test_generate_fgbm_invalid_hurst():
    try:
        generate_fgbm(1000, 1.1)
        assert False, "Expected ValueError for invalid Hurst exponent"
    except ValueError:
        pass


if __name__ == "__main__":
    test_generate_fgbm()
    test_generate_fgbm_no_drift()
    test_generate_fgbm_invalid_hurst()
