# Task 2.6

from typing import Tuple


def with_join(numbers: Tuple[int]) -> int:
    '''Convert a tuple of positive integers to a number

    Implemented via join and generator comprehension.
    '''
    gen_numbers = (str(i) for i in numbers)
    str_number = int(''.join(gen_numbers))
    return str_number


def with_concat(numbers: Tuple[int]) -> int:
    '''Convert a tuple of positive integers to a number

    Implemented via concatenation.
    '''
    str_out = ""
    for i in numbers:
        str_out = str_out + str(i)
    out_int = int(str_out)
    return out_int


def with_map(numbers: Tuple[int]) -> int:
    '''Convert a tuple of positive integers to a number

    Implemented via join and map.
    '''
    return int(''.join(map(str, numbers)))


if __name__ == '__main__':
    print()
    print('{:*^30}'.format('The task 2.6'), end='\n\n')

    original_tuple = (1, 2, 3, 4, 2, 223, 13, 3, 4, 556, 7, 78)

    print(f'Original tuple: {original_tuple}', end='\n\n')

    print(
        f'Function result "with_join": {with_join(original_tuple)}',
        end='\n\n')
    print(
        f'Function result "with_concat": {with_concat(original_tuple)}',
        end='\n\n')
    print(
        f'Function result "with_map": {with_map(original_tuple)}',
        end='\n\n')
