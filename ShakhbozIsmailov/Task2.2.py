"""
    There is a convenient way to count the number of characters in string.

    from collections import Counter
    print(dict(Counter(toLower)))
"""

dummyText = "Oh, it is python"
toLower = dummyText.lower()
characterDict = dict()
iterator = 0

for i in toLower:
    for j in range(len(toLower)):
        if i == toLower[j]:
            iterator = iterator + 1
    characterDict[i] = iterator
    iterator = 0
print(characterDict)

