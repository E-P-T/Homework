# Task 2.7

from typing import Callable, Iterable


def indent_length(a: int, b: int, c: int, d: int) -> int:

    max_ab = max(a, b)
    max_cd = max(c, d)
    indent_length = len(str(max_ab*max_cd))+1

    return indent_length


def data_gen(a: int, b: int, c: int, d: int) -> Iterable[int]:
    return (i*j for i in range(a, b+1) for j in range(c, d+1))


def print_tab(a: int,
              b: int,
              c: int,
              d: int,
              indent: int,
              gen: Callable[[int, int, int, int], Iterable[int]]) -> None:

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


if __name__ == '__main__':

    a = int(input("Enter initial vertical value: "))
    b = int(input("Enter vertical end value: "))
    c = int(input("Enter initial horizontal value: "))
    d = int(input("Enter horizontal end value: "))

    indent = indent_length(a, b, c, d)

    print_tab(a, b, c, d, indent, data_gen)
