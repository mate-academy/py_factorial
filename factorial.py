"""
docstring
"""


def fact(n: int) -> int:
    """

    :param n:
    :return:
    """
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)
