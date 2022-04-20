a, b, c, d = int(input()), int(input()), int(input()), int(input())
mul = [[0 for i in range(c, d + 2)] for j in range(a, b + 2)]
i1 = a
j1 = c
for i in range(1, len(mul)):
    mul[i][0] = i1
    i1 += 1
for j in range(1, len(mul[1])):
    mul[0][j] = j1
    j1 += 1
for i in range(1, len(mul)):
    for j in range(1, len(mul[1])):
        mul[i][j] = mul[i][0] * mul[0][j]
mul[0][0] = ' '

for i in range(len(mul)):
    for j in range(len(mul[0])):
        print(str(mul[i][j]).ljust(4), end='')
    print()
