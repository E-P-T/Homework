input_str = input('Enter a comma separated string values:\n')
input_list = []
for i in input_str.split(", "):
    if i not in input_list:
        input_list.append(i)
input_list.sort()
print(input_list)
