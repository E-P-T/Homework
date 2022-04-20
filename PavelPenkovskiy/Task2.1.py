### Task 2.1
### Write a Python program to calculate the length of a string without using the `len` function.

def string_length(string):
    result = 0
    for _ in string:
        result += 1
    return result


print(string_length('123456789'))
