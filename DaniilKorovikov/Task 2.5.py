list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
un_set = set()
for dict in list:
    for key in dict:
        un_set.add(dict[key])
print(un_set)