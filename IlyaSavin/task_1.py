# TASK2.1 FROM LECTION 2
"""
This module contains several functions to calculate the length of a string.
Also it contains speed tests for these functions.
"""


import timeit
from numpy import average as avg


def get_length_genexpr(string):
    """
    This function can work with any of iterable. Not only with a string.
    """
    return sum(1 for i in string)


def get_length_listcmp(string):
    """
    This function can work with any of iterable. Not only with a string.
    """
    return sum([1 for i in string])


def get_length_loopfor(string):
    """
    This function can work with any of iterable. Not only with a string.
    """
    length = 0
    for i in string:
        length += 1
    return length


def get_length_loopwhile(string):
    """
    This function can work with any of sequence. Not only with a string.
    """
    length = 0
    while string:
        length += 1
        string = string[:-1]
    return length


if __name__ == '__main__':
    print(get_length_genexpr("Hello world!"))  # Result: 12
    print(get_length_listcmp("Hello world!"))  # Result: 12
    print(get_length_loopfor("Hello world!"))  # Result: 12
    print(get_length_loopwhile("Hello world!"))  # Result: 12

    result = timeit.repeat(
        stmt='get_length_genexpr("Hello world!")',
        setup='import task_1',
        number=10000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00510776

    result = timeit.repeat(
        stmt='get_length_listcmp("Hello world!")',
        setup='import task_1',
        number=10000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00439206

    result = timeit.repeat(
        stmt='get_length_loopfor("Hello world!")',
        setup='import task_1',
        number=10000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00311908

    result = timeit.repeat(
        stmt='get_length_loopwhile("Hello world!")',
        setup='import task_1',
        number=10000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00720439

    # ------------------------Results----------------------------------------
    # Since all functions are easy to read and if consider performance...
    # The best way to calculate len of a string without len() is
    # to use loop for.
    # The worst way to calculate len of a string without len() is
    # to use loop while.
    # Note: time of len('Hello world') - 0.00029599 > any of funcs by 10 times
