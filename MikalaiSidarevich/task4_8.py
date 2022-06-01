# Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# ```python
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]

# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

# >>> get_pairs([1])
# None
# ```

def get_pairs(lst: list) -> list[tuple]:
    """
    Return a list of tuples containing pairs of adjacent elements.
    If there is only one element in the list return `None` instead.
    """
    result = []
    if len(lst) > 1:
        for i in range(1, len(lst)):
            result.append((lst[i-1], lst[i]))
        return result


def main():
    """
    Entry point function.
    """
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))
    print(get_pairs([]))


if __name__ == '__main__':
    main()
