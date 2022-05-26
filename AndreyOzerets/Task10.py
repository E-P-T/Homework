# Task 4.10

from typing import Dict


def generate_squares(n: int) -> Dict[int, int]:
    '''Return dictionary.
    The key is a number, the value is the square of that number.
    '''

    result = {}
    for i in range(1, n + 1):
        result[i] = i ** 2
    return result
