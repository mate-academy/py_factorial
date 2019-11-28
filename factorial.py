"""Calculate factorial without using loops and functions from standard library."""


def fact(num: int) -> int:
    """General func"""
    if num > 0:
        num = num * fact(num-1)
        return num
    num = 1
    return num
