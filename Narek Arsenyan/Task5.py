num = input("set number: ")

def createTuple(a = num):
    word = str(a)
    digits = ()
    for n in word:
        digits += (int(n),)
    return digits
print(createTuple())
