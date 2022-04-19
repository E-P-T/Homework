a = 2
b = 4
c = 4
d = 7
for j in range(c - 1, d + 1):
    if j == c - 1:
        print(" " * 4, end='')
    else:
        print(("{:4d}".format(j, )), end='')
print()
for i in range(a, b + 1):
    for j in range(c - 1, d + 1):
        if j == c - 1:
            print(("{:4d}".format(i, )), end='')
        else:
            print(("{:4d}".format(j * i, )), end='')
    print()