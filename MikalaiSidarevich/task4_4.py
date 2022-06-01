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

def split_by_index(s: str, indexes: list[int]) -> list[str]:
    """
    Split the `s` string by indexes specified in `indexes`.
    Wrong indexes are ignored.
    """
    result = []
    beg, end = 0, len(s)
    for i in sorted(set(indexes)):
        if beg <= i < end:
            result.append(s[beg:i])
            beg = i
    else:
        # Consider the last element
        result.append(s[beg:end])
    return result


def main():
    """
    Entry point function.
    """
    s = "pythoniscool,isn'tit?"
    print(split_by_index(s, [6, 8, 12, 13, 18]))
    print(split_by_index(s, [-1, 6, 8, -5, 13, 12, 13, 18, 28]))
    s = "no luck"
    print(split_by_index(s, [42]))


if __name__ == '__main__':
    main()
