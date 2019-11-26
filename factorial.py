"""
Calculate factorial without using loops and functions from standard library
"""


def fact(value: int) -> int:
    """Factorial"""
    if value == 0:
        return 1
    return fact(value - 1) * value
