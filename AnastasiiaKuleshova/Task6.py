# Task 2.6
# Write a Python program to convert a given tuple of positive integers into an integer. Examples:
#
# Input: (1, 2, 3, 4)
# Output: 1234

def tupleToInt(inputTuple):
    tempString = ""
    for item in inputTuple:
        tempString += str(item)
    return int(tempString)


print(tupleToInt(eval("(1,20,4)")))
