def get_pairs(lst):
    if len(lst) == 1:
        return

    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]


print(
    get_pairs([1, 2, 3, 8, 9])
)

print(
    get_pairs(['need', 'to', 'sleep', 'more'])
)

print(
    get_pairs([1])
)
