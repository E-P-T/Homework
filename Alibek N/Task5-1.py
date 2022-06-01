import os

print(os.getcwd())
path_input = os.getcwd().rstrip('\Alibek N') + '\data' +  '\\' + 'unsorted_names.txt'
path_output = os.getcwd().rstrip('\Alibek N') + '\data' +  '\\' + 'sorted_names.txt'


names = []
with open(path_input) as file:
    for x in file:
        if x != '\n':
            names.append(x.strip('\n'))
names = sorted(names)
file.close()

with open(path_output, 'w') as result:
    for i in names:
        result.write(i)
        result.write('\n')
result.close()

