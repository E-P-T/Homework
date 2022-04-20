# Task 2.3
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. Examples:
#
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}


def findAllDividers(inputNumber: int):
    if inputNumber == 0:
        raise Exception
    resultList = []
    for counter in range(1, inputNumber + 1):
        if inputNumber % counter == 0:
            resultList.append(counter)
    return resultList

print("enter number")
try:
    enteredNumber = int(input())
    print(findAllDividers(enteredNumber))
except ValueError:
    print("it's not number")
except Exception:
    print (":(")

