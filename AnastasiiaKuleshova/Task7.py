# Implement a function foo(List[int]) -> List[int] which, given a list of integers,
# return a new list such that each element at index i of the new list is the product
# of all the numbers in the original array except the one at i. Example:
#
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]
#
# >>> foo([3, 2, 1])
# [2, 3, 6]


def foo(list_of_integers: [int]) -> [int]:
    result_list = []
    multiplication_result = 1
    for i in range(0, len(list_of_integers)):
        multiplication_result *= list_of_integers[i]
    for i in list_of_integers:
        result_list.append(int(multiplication_result/i))
    return result_list


print(foo([3,2,1]))