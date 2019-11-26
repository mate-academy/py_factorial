"""
module factorial
"""


def fact(num: int) -> int:
    """
    Calculate factorial without using loops and functions from standard library.
    Recursive factorial function.
    :param num: int
    :return: int
    """
    return 1 if (num < 1) else num * fact(num - 1)
