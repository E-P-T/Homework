#! /usr/bin/env python
# TODO: Implement a function foo(List[int]) -> List[int] which, given a list of
# integers, return a new list such that each element at index `i` of the new lt
# is the product of all the numbers in the original array except the one at i.
# Example:
# >>> python
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]
# >>> foo([3, 2, 1])
# [2, 3, 6]


"""
task_7.py: implemented function, which takes a list of integers and returns a
new list where every element is product of all number except number
with current index.
"""


import math
import timeit
from numpy import average as avg


def foo(L: list[int]) -> list[int]:
    """
    foo: implementation of foo with math.factorial.
    """
    return [math.factorial(len(L)) // i for i in L]


def foo2(L: list[int]) -> list[int]:
    """
    foo: implementation of foo with loop for.
    """
    result = []
    for x in L:
        val = 1
        for y in range(1, len(L) + 1):
            val *= y
        val //= x
        result.append(val)
    return result


def foo3(L: list[int]) -> list[int]:
    """
    foo: implementation of foo with own recursive
    function for calculating factorials.
    """
    def rec(number):
        return 1 if number == 1 else number * rec(number - 1)
    return [rec(len(L)) // i for i in L]


if __name__ == '__main__':
    print(foo([1, 2, 3, 4, 5]))  # Result: [120, 60, 40, 30, 24]
    print(foo([3, 2, 1]))  # Result: [2, 3, 6]
    print(foo2([1, 2, 3, 4, 5]))  # Result: [120, 60, 40, 30, 24]
    print(foo2([3, 2, 1]))  # Result: [2, 3, 6]
    print(foo3([1, 2, 3, 4, 5]))  # Result: [120, 60, 40, 30, 24]
    print(foo3([3, 2, 1]))  # Result: [2, 3, 6]

    result = timeit.repeat(
        stmt='foo([1, 2, 3, 4, 5])',
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0007655589999558288

    result = timeit.repeat(
        stmt='foo2([1, 2, 3, 4, 5])',
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0019342051999046816

    result = timeit.repeat(
        stmt='foo3([1, 2, 3, 4, 5])',
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.002764402200045879

    # The best way to do this task is to use math.factorial because it's
    # an instrument which works with speed of language C.
