# TASK2.5 FROM LECTION 2
"""
This module contains 2 functions aimed at sorting dictionary by key.
Also it contains some speed tests to measure performance of these functions.
"""

import timeit
from numpy import average as avg


def sort_dict_by_key(dictionary) -> None:
    """
    Function sorts source dictionary by key.
    """
    temp_dict = {key: dictionary.pop(key) for key in sorted(dictionary)}
    dictionary.update(temp_dict)


def get_sorted_by_key_dict(dictionary) -> dict:
    """
    Function returns new dictionary that is sorted by key.
    """
    return {key: dictionary.pop(key) for key in sorted(dictionary)}


if __name__ == '__main__':
    test_dict = {3: 'three', 2: 'two', 4: 'four', 1: 'one', 5: 'five'}

    sort_dict_by_key(test_dict)
    print(test_dict)

    new_dict = get_sorted_by_key_dict(test_dict)
    print(new_dict)

    result = timeit.repeat(
        stmt='sort_dict_by_key(test_dict)',
        setup='import task_5',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00033517

    result = timeit.repeat(
        stmt='get_sorted_by_key_dict(test_dict)',
        setup='import task_5',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00028617

    # ------------------------Results----------------------------------------
    # Create new sorted dictionary is faster then modify it.
