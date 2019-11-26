"""
docstring
"""


def fact(num: int) -> int:
    """

    :param num:
    :return:
    """
    return num * fact(num - 1) if num else 1
