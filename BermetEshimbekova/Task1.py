print(r'''Task 2.1
Write a Python program to calculate the length of a string without using the `len` function.
Input: 'Write a Python program to calculate the length of a string without using the `len` function.' ''')
string = 'Write a Python program to calculate the length of a string without using the `len` function.'
length = 0
for i in string: length += 1
print('Output:', length)