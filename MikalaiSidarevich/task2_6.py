# Task 2.6
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:
# ```
# Input: (1, 2, 3, 4)
# Output: 1234
# ```

src = (1, 2, 3, 4)

print(int(''.join(map(str, src))))
