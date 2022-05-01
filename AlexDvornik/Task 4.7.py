"""
Task 4.7
Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.
Example:
foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]
foo([3, 2, 1])
[2, 3, 6]
"""
import copy
from typing import List
import numpy as np


def foo(lst: List[int]) -> List[int]:
    result = []
    for i in range(len(lst)):
        lst_ = copy.copy(lst)
        lst_.pop(i)
        result.append(np.prod(lst_))
    return result


print(foo([3, 2, 1]))


