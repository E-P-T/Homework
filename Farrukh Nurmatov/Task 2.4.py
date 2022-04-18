"""Write a Python program to sort a dictionary by key."""

example_dict = {1: "stas", 3: "misha", 4: "fara", 5: "dima", 2: "serega"}  # initial dict
dict_keys = list(example_dict.keys())  # create list of keys
dict_keys.sort()  # sorting list of keys

sorted_dict = dict() #  create new dict

# add key: value pair to dict, taking key from sorted list and getting value from initial dict by key
for key in dict_keys:
    sorted_dict[key] = example_dict.get(key)


print(example_dict)  # initial dict
print(sorted_dict)  # sorted dict