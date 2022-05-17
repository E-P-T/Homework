# Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
# >>> get_pairs([1])
# None


def get_pairs(list_of_is):
    if len(list_of_is) < 2:
        return None
    result = []
    for i in range(len(list_of_is)):
        if i == 0:
            continue
        else:
            my_list = [list_of_is[i - 1], list_of_is[i]]
            result.append(tuple(my_list))
    return result


print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))
