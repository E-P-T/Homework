# TASK2.4 FROM LECTION 2
"""
This module contains several functions that return all divisors of a
number. It also contains some speed tests for these functions.
"""


import timeit
from numpy import average as avg


def get_divisors(number: int) -> set:
    divisors = {1, }
    for x in range(2, number + 1):
        if number % x == 0:
            divisors.add(x)
    return divisors


def get_divisors_setcmp(number: int) -> set:
    return {x for x in range(1, number + 1) if number % x == 0}


def get_divisors_listcmp(number: int) -> list:
    return [x for x in range(1, number + 1) if number % x == 0]


if __name__ == '__main__':
    is_integer = False
    while not is_integer:
        try:
            number = int(input('Enter number: '))  # for example 60
            is_integer = True
        except ValueError:
            print('Cannot convert to integer.')

    print(get_divisors(number))
    # Result: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 60, 30}
    print(get_divisors_setcmp(number))
    # Result: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 60, 30}
    print(get_divisors_listcmp(number))
    # Result: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]

    result = timeit.repeat(
        stmt='get_divisors(number)',
        setup='import task_4',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00263927

    result = timeit.repeat(
        stmt='get_divisors_setcmp(number)',
        setup='import task_4',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00217567

    result = timeit.repeat(
        stmt='get_divisors_listcmp(number)',
        setup='import task_4',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00208785

    # ------------------------Results----------------------------------------
    # The best way to do this task is to use list comprehension
