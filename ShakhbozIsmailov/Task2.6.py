dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
             {"VIII": "S007"}]
dict_items = [v for i in dict_list for k, v in i.items()]
print(set(dict_items))
