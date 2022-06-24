def get_pairs_zip(lst: list) -> list[tuple]:
    if len(lst) < 2:
        return None

    first = lst[:-1]
    second = lst[1:]

    return [ el for el in zip(first, second)]

def get_pairs_while(lst: list) -> list[tuple]:
    if len(lst) < 2:
        return None

    length = len(lst) - 1
    res = []

    for i in range(length):
        res.append( (lst[i], lst[i+1]) )

    return res

tmp_zip = get_pairs_zip(['need', 'to', 'sleep', 'more'])
tmp_while = get_pairs_while(['need', 'to', 'sleep', 'more'])

print(tmp_zip)
print(tmp_while)