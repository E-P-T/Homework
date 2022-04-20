### Task 2.6
# Write a Python program to convert a given tuple of positive integers into an integer. 
# Examples:
# ```
# Input: (1, 2, 3, 4)
# Output: 1234
# ```

number = ''
tuple = (1, 2, 3, 4)
for i in tuple:
    number += str(i)
print(int(number))