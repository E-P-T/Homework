number = 1
list = []
for n in range(1, number // 2 + 1):
    if number % n == 0:
        list.append(n)
list.append(number)
print(list)