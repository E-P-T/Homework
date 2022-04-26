# Task 4.8
'''Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
of tuples containing pairs of elements. Pairs should be formed as in the
example. If there is only one element in the list return `None` instead.
Example:
```python
get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

get_pairs([1])
None
'''


def get_pairs(lis):
    if len(lis) <= 1:
        return None
    res = [v1 for v1 in zip(lis[0:-1], lis[1:])]
    # res = [(lis[i],lis[i+1]) for i in range(0,len(lis)-1)]
    return res


print(get_pairs([1, 2, 3, 8, 9]))
