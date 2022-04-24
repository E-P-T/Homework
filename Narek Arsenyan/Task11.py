dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

def combineDicts(*args):
    finalDict = dict()
    for i in args:
        for n in i.keys():
            if n in finalDict:
                finalDict[n] += i[n]
            else:
                finalDict[n] = i[n]
    print(finalDict)
combineDicts(dict_1, dict_3, dict_2)
