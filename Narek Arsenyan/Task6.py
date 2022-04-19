listTwo = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
listOne = []
for n in listTwo:
    value = list(n.values())[0]
    if value not in listOne:
        listOne.append(value)
print(listOne)