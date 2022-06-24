
def split_by_index(s: str, indexes: list[int]) -> list[str]:
    indexes = sorted(indexes)
    indexes = [el for el in indexes if el > 0 and el < len(s)]

    res = []
    index = 0
    pairs = zip([0] + indexes, indexes + [len(s)])

    for beg, end in pairs:
        res.append(s[beg:end])

    return res

answer = ["python", "is", "cool", ",", "isn't", "it?"]
test = split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
print(answer, test)
print(answer == test)