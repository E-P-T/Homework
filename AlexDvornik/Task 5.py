"""
Task 2.5
Write a Python program to sort a dictionary by key.
"""

sample_dict = {
    'erlich': 40,
    'dinesh': 2,
    'richard': 1,
    'gilfoyle': 3,
    'bighead': 0,
}


def get_sorted_dict(unsorted_dict):
    return dict(sorted(unsorted_dict.items()))


print(get_sorted_dict(sample_dict))
