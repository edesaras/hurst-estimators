from ._gen_sbpf import _gen_sbpf
from math import ceil


def search_opt_seq_len(N: int, w: int, alpha: float = 0.99) -> int:
    """
    Search the optimal sequence length.

    Parameters:
        N (int): Original sequence length.
        w (int): Lower bound for factors.
        alpha (float): Percentage for the starting point of the search.

    Returns:
        int: Optimal sequence length.
    """
    n0 = int(ceil(alpha * N))
    Lfactors = []

    for i in range(n0, N + 1):
        sbpf = _gen_sbpf(i, w)
        Lfactors.append(len(sbpf))

    vmax = max(Lfactors)
    imax = Lfactors.index(vmax)
    Nopt = n0 + imax

    return Nopt
