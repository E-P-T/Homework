### Task 4.5
'''
Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
of a given integer's digits.
Example:
```python
split_by_index(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
'''


def get_digits(number):
    lis = [int(i) for i in str(abs(number))]
    number = tuple(lis)
    return number


print(get_digits(87178291199))
