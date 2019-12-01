"""module"""


def fact(number: int) -> int:
    """recursive factorial!"""
    if number < 1:
        return 1
    return number * fact(number - 1)
