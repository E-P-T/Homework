# Task 2.4
# Write a Python program to sort a dictionary by key.


def sortDictByKey():
    try:
        sortableDict = {}
        print("enter dictionary")
        sortableDict = eval(input())
    except SyntaxError:
        print("syntax error")
    except NameError:
        print("Name error")
    sortedDict = {}
    for key in sorted(sortableDict.keys()):
        sortedDict[key] = sortableDict[key]
    return sortedDict


print(sortDictByKey())
