# Write a Python program to print all unique values of all dictionaries in a list. Examples:

# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


my_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

output = []
for dict in my_list:
    for key in dict:
        if dict[key] not in output:
            output.append(dict[key])
            
            
print("Result {}".format(output))