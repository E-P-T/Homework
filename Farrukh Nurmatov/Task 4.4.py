"""Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored."""

def split_by_index(s: str, indexes: list):
    real_indexes = [i for i in indexes if i in range(len(s))]
    out_lst = []
    start = 0
    for index in real_indexes:
        out_lst.append(s[start:index])
        start = index
    out_lst.append(s[start:])
    return out_lst


if __name__ == '__main__':
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_index("no luck", [42]))












