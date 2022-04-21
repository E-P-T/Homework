# Task 4.7
'''Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.
Example:
```python
foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]
'''
import math

def foo(lis):
    s = math.prod(lis)
    # new_lis = []
    # for i in lis:
        # res = s // i
        # new_lis.append(res)
    new_lis = list(map(lambda i: s // i, lis))
    return new_lis


print(foo([1, 2, 3, 4, 5]))


# def multiply(lst):
#     answer = 1
#     for i in lst:
#         answer *= i
#     return answer
#
#
# print(multiply([1, 2, 3, 4, 5]))

#
#
