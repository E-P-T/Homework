"""Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
of tuples containing pairs of elements. Pairs should be formed as in the
example. If there is only one element in the list return `None` instead."""


def get_pairs(nums: list):
    if len(nums) == 1:
        return None
    else:
        out_lst = [(nums[i], nums[i + 1]) for i in range(len(nums) - 1)]
        return out_lst


if __name__ == '__main__':
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))