# ### Task 4.4
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
def split_index(string: str, ind_s: list) -> list:
    ret = []
    word = ""
    for _ in range(len(string)):
        word += string[_]
        if _ + 1 in ind_s:
            ret.append(word)
            word = ""
    ret.append(word)
    return ret