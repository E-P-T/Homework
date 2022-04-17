# Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
# Example:
# ```python
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]
#
# >>> foo([3, 2, 1])
# [2, 3, 6]
# ```


def foo(int_lst: list) -> list:
    new_lst = list()
    for i in range(len(int_lst)):
        prod = 1
        for j in range(len(int_lst)):
            if i != j:
                prod = prod * int_lst[j]
        new_lst.append(prod)
    return new_lst
