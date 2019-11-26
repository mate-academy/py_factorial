'''
Module
'''


def fact(number: int) -> int:
    '''

    :param n:
    :return:
    '''
    if not number or number == 1:
        return 1
    return number * fact(number - 1)
