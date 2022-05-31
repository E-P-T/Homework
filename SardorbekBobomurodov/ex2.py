def ex2(text):
    dictTxt = {}
    for x in text:
        keys = dictTxt.keys()
        if x in keys:
            dictTxt[x] += 1
        else:
            dictTxt[x] = 1
    print(dictTxt)


if __name__ == '__main__':
    while True:
        text = input("Enter a text: ")
        ex2(text)