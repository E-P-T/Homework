#! /usr/bin/env python
# TODO: Implement a function `get_digits(num: int) -> Tuple[int]`
# which returns a tuple of a given integer's digits.
# Example:
# >>> python
# >>> get_digits(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)


"""
task_5.py: implemented two function of get_digits and some speed tests for
these functions.
"""


import timeit
from numpy import average as avg


def get_digits_genexpr(number):
    """
    get_digits_genexpr: implementation with generator expression.
    """
    return tuple(int(x) for x in str(number))


def get_digits_listcmp(number):
    """
    get_digits_listcmp: implementation with list compherension.
    """
    return tuple([int(x) for x in str(number)])


if __name__ == '__main__':
    print(get_digits_genexpr(87178291199))
    # Result: (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
    print(get_digits_listcmp(87178291199))
    # Result: (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

    result = timeit.repeat(
        stmt="get_digits_genexpr(87178291199)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0018833135996828786

    result = timeit.repeat(
        stmt="get_digits_listcmp(87178291199)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0015886089997366071

    # As usual, the function with list compherension is better than
    # function with generator expression by performance criterion
