# Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.



def get_pairs(lst: list) -> list[tuple]:
    assert isinstance(lst, list), 'Incorrect input. Argument must be a list'
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)] if len(lst) > 2 else None


print(get_pairs(['need', 'to', 'sleep', 'more']))
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

print(get_pairs([1]))
# None

print(get_pairs([]))
# None