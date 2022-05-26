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


if __name__ == '__main__':
    print()
    print('{:*^30}'.format('Task 4.10'), end='\n\n')
    print(f'Result: {generate_squares(5)}')
