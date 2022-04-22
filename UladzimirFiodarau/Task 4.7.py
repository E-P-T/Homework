# Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.

from functools import reduce


def foo(integers: list[int]) -> list[int]:
    """
    The function takes a list of integers and returns a new list such that each element at index `i` of the new list
    is the product of all the numbers in the original array except the one at `i`.
    :param integers: a list of integers
    :return: a list of integers
    :raises AssertionError if argument is not a list of integers
    """
    if not integers:
        return []
    assert isinstance(integers, list) and all(map(lambda x: isinstance(x, int), integers)), 'Incorrect input. ' \
                                                                                            'Argument must be a list of integers'
    multiplication = reduce(lambda x, y: x * y, integers)
    return [int(multiplication / i) for i in integers]

# print(foo([1, 2, 3, 4, 5]))
# # [120, 60, 40, 30, 24]
#
# print(foo([3, 2, 1]))
# # [2, 3, 6]
#
# print(foo([]))
# # []
