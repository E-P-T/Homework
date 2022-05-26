# Task 2.4

def data_dict(source_dict):
    '''Return a dictionary with data grouped by key type.'''
    out_dict = {}
    for i in source_dict:
        key_type = type(i)
        if key_type not in out_dict:
            out_dict[key_type] = {}
        out_dict[key_type].update({i: source_dict[i]})
    return out_dict


def sort_dict(source_dict, **kwargs):
    '''Sort dictionary.'''
    out_dict = {}
    for i in ordered_dict:
        s = sorted(source_dict[i].items(), **kwargs)
        out_dict[i] = dict(s)
    return out_dict


def data_unpacking(source_dict):
    '''Unpack the data into a dictionary.'''
    out_dict = {}
    out_dict_update = out_dict.update
    for i in source_dict:
        m = {**source_dict[i]}
        out_dict_update(m)
    return out_dict


if __name__ == '__main__':
    d = {'a': 1, 'c': 3, 'b': 2, 1: 2, 2: 3, 8: 0, 4: 5,
         (1, 2): 3, (2, 1, 4): 1, 'aa': {}, 's': {'x': 1, }}
    print()
    print('{:*^30}'.format('Task 2.4'), end='\n\n')
    print(f'Source dictionary: {d}', end='\n\n')

    ordered_dict = data_dict(d)
    sorted_dict = sort_dict(ordered_dict)
    unpacked_dict = data_unpacking(sorted_dict)

    print(f'Sorted dictionary: {unpacked_dict}', end='\n\n')
