d = {'c': 10, 'b': 2, 'a': 2}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[0]))
print(sorted_dict)