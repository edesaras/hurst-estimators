from hurst_estimators.utils import search_opt_seq_len, _gen_sbpf
import pytest


def test_gen_sbpf():
    assert _gen_sbpf(990, 20) == {22, 30, 33, 45}
    assert _gen_sbpf(30, 2) == {2, 3, 5, 6, 10, 15}
    assert _gen_sbpf(16, 2) == {2, 4, 8}
    assert _gen_sbpf(48, 2) == {2, 3, 4, 6, 8, 12, 16, 24}
    assert _gen_sbpf(48, 3) == {3, 4, 6, 8, 12, 16}
    assert _gen_sbpf(48, 4) == {4, 6, 8, 12}
    assert _gen_sbpf(48, 5) == {6, 8}
    assert _gen_sbpf(48, 6) == {6, 8}
    assert _gen_sbpf(1, 2) == set()  # No proper factors
    assert _gen_sbpf(48, 7) == set()


def test_search_opt_seq_len():
    assert search_opt_seq_len(997, 20, 0.99) == 990
    assert search_opt_seq_len(1, 2, 0.1) == 1


if __name__ == "__main__":
    pytest.main([__file__])
