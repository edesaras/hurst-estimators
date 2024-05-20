def _gen_sbpf(a: int, w: int) -> set:
    """
    Generate the list of bounded proper factors of a composite number a.

    Parameters:
        a (int): Composite number.
        w (int): Lower bound of the factors.

    Returns:
        list: List of bounded proper factors.
    """
    sbpf = set()
    for i in range(w, a // w + 1):
        if a % i == 0:
            sbpf.add(i)
    return sbpf
