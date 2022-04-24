str = input("Please set string: ")

def firstFunction(a = str):
    designedStr = ''
    for char in range(0, len(a)):
        if(a[char] == '"'):
            designedStr += "'"
        elif(a[char] == "'"):
            designedStr += '"'
        else:
            designedStr += a[char]
    return designedStr

print("New design: ")
print(firstFunction(str))
