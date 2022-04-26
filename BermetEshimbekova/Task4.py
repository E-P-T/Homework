# Task 4.4

def split_by_index(s, index):
    result = []
    x = 0
    for i in index:
        result.append(s[x:i])
        x = i
    if s[i:]:
        result.append(s[i:])
    print(result)


split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
split_by_index("no luck", [42])
