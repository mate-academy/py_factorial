"""Factorial module"""

def fact(number: int) -> int:
    """
    :param n: number
    :return: number factorial
    """
    if number == 0:
        return 1
    return fact(number-1) * number
