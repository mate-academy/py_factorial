"""doc"""


def fact(val: int) -> int:
    """fact"""
    if not val or val == 1:
        return 1
    return val * fact(val - 1)
