# ### Task 2.1
# Write a Python program to calculate the length of a string without using the `len` function.

def stringLength(line):
    counter = 0
    for symbol in line:
        counter += 1
    print(counter)


print("input line")
enteredLine = input()
stringLength(enteredLine)
