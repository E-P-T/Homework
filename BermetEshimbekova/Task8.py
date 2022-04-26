# Task 4.8

def get_pairs(lst):
    result = None
    if len(lst) > 1:
        result = []
        for i in range(0, len(lst)-1):
            result.append((lst[i], lst[i+1]))
    print(result)


get_pairs([1, 2, 3, 8, 9])
get_pairs(['need', 'to', 'sleep', 'more'])
get_pairs([1])
