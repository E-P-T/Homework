#!/usr/bin/python3
print('Python Practice - Session 2')
print('Task 2.5 Write a Python program to print all unique values of all dictionaries in a list.')

list_with_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# First version
unique_values = set()

for a_dict in list_with_dicts:
    for value in a_dict.values():
        if value not in unique_values:
            unique_values.add(value)

# Second version
unique_values = set(value for a_dict in list_with_dicts for value in a_dict.values())
print(f'Here are the unique values: {unique_values}')
