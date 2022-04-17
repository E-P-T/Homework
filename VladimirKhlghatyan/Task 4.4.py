# Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# ```python
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
#
# >>> split_by_index("no luck", [42])
# ["no luck"]
# ```


def split_by_index(s: str, indexes: list) -> list:
    new_lst = list()
    for i in range(len(indexes)):
        if i == 0:
            new_lst.append(s[:indexes[i]])
        elif i == len(indexes) - 1:
            new_lst.append(s[indexes[i - 1]:indexes[i]])
            new_lst.append(s[indexes[i]:])
        else:
            new_lst.append(s[indexes[i-1]:indexes[i]])
    return new_lst
