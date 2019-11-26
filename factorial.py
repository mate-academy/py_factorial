"""module docstring"""
import numpy

def fact(number):
    """function docstring"""
    res_tuple = tuple(range(1, number + 1))
    result = numpy.prod(res_tuple)
    return result
