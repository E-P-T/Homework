# TASK2.7 FROM LECTION 2
"""
This module contains 2 functions aimed at
generating integer from tuple of digits.
Also it contains some speed tests to
measure performance of these functions.
"""


import timeit
from numpy import average as avg


def tuple_to_number_cmp(tuple_) -> int:
    """
    This function also works with any iterable of digits
    """
    return int(''.join(str(x) for x in tuple_))


def tuple_to_number(tuple_) -> int:
    """
    This function also works with any iterable of digits
    """
    tmp = ''
    for number in tuple_:
        tmp += str(number)
    return int(tmp)


if __name__ == '__main__':
    tuple_ = (1, 2, 3, 4)
    print(tuple_to_number_cmp(tuple_))  # Result: 1234
    print(tuple_to_number(tuple_))  # Result: 1234

    result = timeit.repeat(
        stmt='tuple_to_number_cmp(tuple_)',
        setup='import task_7',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00066522

    result = timeit.repeat(
        stmt='tuple_to_number(tuple_)',
        setup='import task_7',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00052808

    # ------------------------Results----------------------------------------
    # As we can see the best way to do this task is to use
    # simple instruments instead of str methods and genexp.
    # I think that's because it's rather heavy instruments.
