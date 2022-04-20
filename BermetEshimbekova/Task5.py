### Task 2.4
# Write a Python program to sort a dictionary by key.

dictionary = {5:'abc', 2:'def', 9:'ghi', 1:'jkl'}
for key in sorted(dictionary):
    dictionary[key] = dictionary.pop(key)
print(dictionary)