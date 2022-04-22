"""Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`."""

def num_product(pos: int, lst: list):
    copied_lst = lst.copy()
    copied_lst.pop(pos)
    prod = 1
    for num in copied_lst:
        prod *= num
    return prod


def foo(nums: list):
    out_lst = []
    for i in range(len(nums)):
        out_lst.append(num_product(i, nums))
    return out_lst


if __name__ == '__main__':
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))



