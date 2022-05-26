# Task 2.7

from typing import Callable, Iterable


def indent_length(a: int, b: int, c: int, d: int) -> int:
    '''Return the length of the indent between columns.'''

    max_ab = max(a, b)
    max_cd = max(c, d)
    indent_length = len(str(max_ab*max_cd)) + 1

    return indent_length


def data_gen(a: int, b: int, c: int, d: int) -> Iterable[int]:
    '''Return the product of two numbers.'''
    return (i*j for i in range(a, b+1) for j in range(c, d+1))


def print_tab(a: int,
              b: int,
              c: int,
              d: int,
              indent: int,
              gen: Callable[[int, int, int, int], Iterable[int]]) -> None:
    '''Print data in table view.'''

    data = gen(a, b, c, d)

    print('{:<{y1}}'.format('', y1=indent), end=" ")

    for i in range(c, d+1):
        print('{:<{y1}}'.format(i, y1=indent), end=" ")
    print()

    for i in range(a, b+1):
        print('{:<{y1}}'.format(i, y1=indent), end=" ")
        for _ in range(c, d+1):
            print('{:<{y1}}'.format(next(data), y1=indent), end=" ")
        print()
