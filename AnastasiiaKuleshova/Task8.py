# Task 4.8
# Implement a function get_pairs(lst: List) -> List[Tuple] which returns a
# list of tuples containing pairs of elements. Pairs should be formed as in the example.
# If there is only one element in the list return None instead. Example:
#
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
#
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
#
# >>> get_pairs([1])
# None

def get_pairs(lst: []) -> [tuple]:
    if len(lst) == 1:
        return None
    else:
        result_list_of_tuples = []
        for i in range(0, len(lst) - 1):
            result_list_of_tuples.append(tuple(lst[i:i + 2]))
        return result_list_of_tuples


print(get_pairs([1, 2, 3, 4]))