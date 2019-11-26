"""doc-string"""


def fact(num: int) -> int:
    """
    Returns factorial of a given number
    :param num: int
    :return: int
    """
    return fact(num - 1)*num if num else 1
