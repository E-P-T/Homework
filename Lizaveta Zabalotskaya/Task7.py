a = 2
b = 4
c = 3
d = 7

ab = ["flag"]
for element in range(a, b + 1):
    ab.append(element)

cd = list(range(c, d + 1))

for x in ab:
    s = ""
    if x == "flag":
        s += "".ljust(4)
        for y in cd:
            s += str(1 * y).ljust(4)
    else:
        s += str(x).ljust(4)
        for y in cd:
            s += str(x * y).ljust(4)
    print(s)