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
# ```

def foo(lst: list[int]) -> list[int]:
    """
    Take a list of integers and return a new list: 
    each element is the product of all the original integers except the one at current position.
    """
    result = []

    # Calc total product
    total = 1
    for el in lst:
        total *= el

    # Fill result list
    for el in lst:
        result.append(total // el)

    return result


def main():
    """
    Entry point function.
    """
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))
    print(foo([]))


if __name__ == '__main__':
    main()
