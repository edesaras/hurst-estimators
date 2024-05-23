import numpy as np
from hurst_estimators.simulators import generate_fbm


def test_generate_fbm():
    length = 1000
    hurst = 0.7
    seed = 42

    fbm = generate_fbm(length, hurst, seed=seed)

    assert isinstance(fbm, np.ndarray)
    assert len(fbm) == length
    assert np.isclose(fbm[0], 0, atol=1e-2)


def test_generate_fbm_invalid_hurst():
    try:
        generate_fbm(1000, 1.1)
        assert False, "Expected ValueError for invalid Hurst exponent"
    except ValueError:
        pass


if __name__ == "__main__":
    test_generate_fbm()
    test_generate_fbm_invalid_hurst()
