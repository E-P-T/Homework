'''
### Task 2.1
Write a Python program to calculate the length of a string without using the `len` function.
'''

string = input()
i = 0
for char in string:
    i += 1

print(i)