'''
Module
'''


def fact(number: int) -> int:
    '''

    :param n:
    :return:
    '''
    if number == 0:
        return 1
    return number * fact(number - 1)
