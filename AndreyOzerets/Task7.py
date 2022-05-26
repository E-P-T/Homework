# Task 2.7

from typing import Iterable


def indent_length(a: int, b: int, c: int, d: int) -> int:
    '''Return the length of the indent between columns.'''

    max_ab = max(a, b)
    max_cd = max(c, d)
    indent_length = len(str(max_ab*max_cd)) + 1

    return indent_length


def data_gen(a: int, b: int, c: int, d: int) -> Iterable[int]:
    '''Return the product of two numbers.'''
    return (i*j for i in range(a, b+1) for j in range(c, d+1))
