dictionary = {'Name': 'Kekus', 5:44, 'Surname': 'Cool', 'A':4, 'Phone number' : '5423142', 1: 1}
keys = list(dictionary.keys())
keys_types = {}
for key in keys:
    index = str(type(key))
    if index not in keys_types:
        keys_types[index] = []
    keys_types[index].append(key)

for types, content in keys_types.items():
    content.sort()

keys_sorted = []
for types, content in keys_types.items():
    keys_sorted.extend(content)

dict_sorted = {}
for key in keys_sorted:
    dict_sorted[key] = dictionary[key]

print(dict_sorted)
