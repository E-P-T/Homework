#!/usr/bin/python3
print('Python Practice - Session 2')
print('Task 2.4 Write a Python program to sort a dictionary by key.')

some_dict = {'a': 1, 'c': 3, 'd': 4, 'b': 2}

# First version to get sorted keys
sorted_keys = sorted(some_dict, key=lambda key: key)

# Second version to get sorted keys
sorted_keys = list(some_dict.keys())

for i in range(len(sorted_keys)):
    for j in range(1, len(sorted_keys)):
        if sorted_keys[j] < sorted_keys[j - 1]:
         sorted_keys[j], sorted_keys[j - 1] = sorted_keys[j - 1], sorted_keys[j]

# The below part is common for the First and the Second versions
sorted_dict = {}

for key in sorted_keys:
    sorted_dict[key] = some_dict[key]

print(f'Here is the dictionary with sorted keys: {sorted_dict}')