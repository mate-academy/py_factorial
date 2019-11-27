"""Calculate factorial without using loops and functions from standard library."""


def fact(number: int) -> int:
    """Factorial calculation with recursive approach"""
    if number <= 1:
        return 1
    return number * fact(number - 1)
