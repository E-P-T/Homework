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


if __name__ == '__main__':
    print()
    print('{:*^30}'.format('Task 4.11'), end='\n\n')

    a = {'a': 100, 'b': 200}
    b = {'a': 200, 'c': 300}
    c = {'a': 300, 'd': 100}
    d = {'a': 100, 'f': 300}

    print(f'Result 1: {combine_dicts(a, b, c, d)}', end='\n\n')
    print(f'Result 2: {combine_dicts(a, b, d)}', end='\n\n')
