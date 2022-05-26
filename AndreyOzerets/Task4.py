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
