"""
Task 2.6
Write a Python program to print all unique values of all dictionaries in a list.
Examples:
Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

"""

input_data = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

list_of_values = []
for data in input_data:
    for value in data.values():
        list_of_values.append(value)
print(set(list_of_values))



