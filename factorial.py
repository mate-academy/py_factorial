"""
fact
"""


def fact(number: int) -> int:
    """

    :param number: number
    :return: factorial of the number
    """
    if number == 0:
        return 1

    return number * fact(number - 1)
