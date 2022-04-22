def combine_dicts(*args):
    l = [(key, value) for el in args for key, value in el.items()]
    final_list = []
    for i in range(len(l)):
        k = l[i][0]
        lis = list(map(lambda el: el[1] if k in el else 0, l))
        element = {k: sum(lis)}
        if element not in final_list:
            final_list.append(element)
    final_dict = {key:value for x in final_list for key, value in x.items()}
    return final_dict





dict_1 = {"a": 100,
          "b": 200}

dict_2 = {"a": 200,
          "c": 300}

dict_3 = {"a": 300,
          "d": 100}
print(combine_dicts(dict_1, dict_2, dict_3))
