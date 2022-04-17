# Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# ```python
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]


def get_pairs(lst: list) -> list:
    new_lst = list()
    if len(lst) < 2:
        return None
    for i in range(len(lst) - 1):
        new_lst.append((lst[i], lst[i+1]))
    return new_lst
