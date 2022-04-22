def splitee(string):
    l = []
    i = 0
    counter = string.count(" ")
    while i != counter:
        ind = string.index(" ")
        new_s = string[:ind]
        l.append(new_s)
        new_s = string[ind:]
        string = new_s.lstrip()
        i += 1
    l.append(string)
    return l


s = input("string: ")

print(splitee(s))
