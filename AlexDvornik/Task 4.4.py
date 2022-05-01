'''
Task 4.4
Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

split_by_index("no luck", [42])
["no luck"]
'''
from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    start = 0
    list_of_words = []
    for end in sorted(indexes):
        try:
            if s[end]:
                list_of_words.append(s[start:end])
                start = end
        except:
            print("Index not found")
            return [s]
    list_of_words.append(s[end:])
    return list_of_words


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
