def combine_dicts(*args):
    keys_out=[]
    for i in range(len(args)):
        keys_in = [key for key in args[i]]
        for j in range(len(keys_in)):
            if keys_in[j] not in keys_out:
                keys_out.append(keys_in[j])
    temp_dict=dict.fromkeys(keys_out, 0)
    for i in range(len(args)):
        keys_in = [key for key in args[i]]
        working_dict=args[i]
        for j in range(len(working_dict)):
            temp_dict[keys_in[j]] = temp_dict[keys_in[j]]+working_dict[keys_in[j]]
        dict.clear(working_dict)
    return(temp_dict)
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))