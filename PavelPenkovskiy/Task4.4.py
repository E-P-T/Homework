# Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# ```python
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
# >>> split_by_index("no luck", [42])
# ["no luck"]
# ```


def split_func(string, indexes):
    result_list = []
    index = 0
    for i in indexes:
        if i > len(string):
            return [string]
        if i == indexes[0]:
            result_list.append(string[index:i])
            index = i + 1
        elif i == indexes[-1]:
            result_list.append(string[index - 1:i])
            result_list.append(string[i:])
            index = i + 1
        else:
            result_list.append(string[index-1:i])
            index = i + 1
    return result_list


print(split_func("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_func("no luck", [42]))

