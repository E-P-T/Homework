from collections import defaultdict


def group_by(it, key=lambda x: x):
    """
    Group an iterable by key
    """
    d = defaultdict(list)
    for item in it:
        d[key(item)].append(item)
    return d.items()


def merge_by_key(it, key=lambda x: x):
    """
    Merge an iterable by key. If the key is the same for multiple items, only the latest stays
    """
    d = {}
    for item in it:
        d[key(item)] = item
    return list(d.values())
