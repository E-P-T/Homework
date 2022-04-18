"""Write a Python program to print all unique values of all dictionaries in a list."""


lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
       {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]  # example list of dicts

unique_values = set()  # empty set for unique values

# add all values from dicts to make them unique
for i in lst:
    unique_values.update(set(i.values()))

print(unique_values)
