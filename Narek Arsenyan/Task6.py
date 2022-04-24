str = input("set string: ")

def getLongestWord(stri = str):
    words = stri.split()
    longWord = words[0]
    for n in words:
        if len(n) > len(longWord):
            longWord = n
    return longWord
print(getLongestWord())
