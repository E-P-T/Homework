from collections import defaultdict


def group_by(it, key=lambda x: x):
    d = defaultdict(list)
    for item in it:
        d[key(item)].append(item)
    return d.items()


def merge_by_key(it, key=lambda x: x):
    d = {}
    for item in it:
        d[key(item)] = item
    return list(d.values())
