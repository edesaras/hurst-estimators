import numpy as np
import pytest
from hurst_estimators import generate_fgn


def test_generate_fgn_length():
    length = 1000
    hurst = 0.7
    fgn = generate_fgn(length, hurst)
    assert len(fgn) == length


def test_generate_fgn_type():
    length = 1000
    hurst = 0.7
    fgn = generate_fgn(length, hurst)
    assert isinstance(fgn, np.ndarray)


def test_generate_fgn_invalid_hurst():
    length = 1000
    with pytest.raises(ValueError):
        generate_fgn(length, -0.1)
    with pytest.raises(ValueError):
        generate_fgn(length, 1.1)


def test_generate_fgn_mean_variance():
    length = 10000
    hurst = 0.5
    fgn = generate_fgn(length, hurst)
    mean = np.mean(fgn)
    variance = np.var(fgn)
    print(mean, variance)
    assert np.isclose(mean, 0, atol=0.1)
    assert np.isclose(variance, 1, atol=0.1)


if __name__ == "__main__":
    pytest.main([__file__])
