# Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
# Example:
# ```python
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]
# >>> foo([3, 2, 1])
# [2, 3, 6]


def foo(list_of_integers):
    result_list = []
    for i in list_of_integers:
        product = 1
        for j in list_of_integers:
            if j == i:
                continue
            else:
                product *= j
        result_list.append(product)
    return result_list


print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))


