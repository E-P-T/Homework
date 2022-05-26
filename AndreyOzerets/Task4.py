# Task 2.4

def data_dict(source_dict):
    '''Return a dictionary with data grouped by key type.'''
    out_dict = {}
    for i in source_dict:
        key_type = type(i)
        if key_type not in out_dict:
            out_dict[key_type] = {}
        out_dict[key_type].update({i: source_dict[i]})
    print(out_dict)
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
