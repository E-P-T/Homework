number = input("Set number: ")

def generateSquares(num = number):
    finalDict = dict()
    for i in range(1,num + 1):
        finalDict[i] = i**2
    print(finalDict)
generateSquares()
