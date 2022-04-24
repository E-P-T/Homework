list = input("Set numbers: ")

def foo(a = list):
    finalList = []
    for n in a:
        b = 1
        for i in a:
            b *= i
        b /= n
        finalList.append(b)
    return finalList
print(foo())
