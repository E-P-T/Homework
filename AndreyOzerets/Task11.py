# Task 4.11


def combine_dicts(*args):
    '''Merge a variable number of dictionaries

    In case of identical keys, the values are summed up.
    '''

    result = {}
    for i in args:
        for j in i:
            if j not in result:
                result[j] = i[j]
            else:
                result[j] += i[j]
    return result
