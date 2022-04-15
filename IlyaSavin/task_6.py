# TASK2.6 FROM LECTION 2
"""
This module contains 2 functions aimed at creating list of unique dicts values.
Also it contains some speed tests to measure performance of these functions.
"""


import timeit
from numpy import average as avg


def get_list_of_unique_values(list_of_dicts) -> list:
    unique_values = []
    for dict in list_of_dicts:
        for key in dict:
            if dict[key] not in unique_values:
                unique_values.append(dict[key])
    unique_values.sort()
    return unique_values


def get_list_of_unique_values_cmp(list_of_dicts) -> list:
    return sorted({dict[key] for dict in list_of_dicts for key in dict})


if __name__ == '__main__':
    list_of_dicts = [
        {"V": "S001"}, {"V": "S002"},
        {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"},
        {"VIII": "S007"}
    ]

    print(list1 := get_list_of_unique_values(list_of_dicts))
    # Result: ['S001', 'S002', 'S005', 'S009', 'S007']
    print(list2 := get_list_of_unique_values_cmp(list_of_dicts))
    # Result: ['S002', 'S005', 'S007', 'S009', 'S001']
    print(sorted(list1) == sorted(list2))
    # Result: True

    result = timeit.repeat(
        stmt='get_list_of_unique_values(list_of_dicts)',
        setup='import task_6',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00085894

    result = timeit.repeat(
        stmt='get_list_of_unique_values_cmp(list_of_dicts)',
        setup='import task_6',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00081363

    # ------------------------Results----------------------------------------
    # As usual the best way to do this task is to use built-in tools
