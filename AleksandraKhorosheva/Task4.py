### Task 4.4
'''Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
```python
split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

split_by_index("no luck", [42])
["no luck"]'''


# [0, 6, 8, 12, 13, 18]
# [6, 8, 12, 13, 18,None]

def split_by_index(s, lis):
    li = sorted(filter(lambda i: 0 <= i < len(s), lis))
    # output = [s[v1:v2] for v1, v2 in zip([0] + li, li + [None])]
    start = 0
    output = []

    for end in li:
        output.append(s[start:end])
        start = end
    output.append(s[start:])
    return output


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
