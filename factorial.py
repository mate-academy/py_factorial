"""factorial module."""


def fact(number: int) -> int:
    """returns number's factorial."""
    if number == 0:
        return 1
    return number * fact(number-1)
