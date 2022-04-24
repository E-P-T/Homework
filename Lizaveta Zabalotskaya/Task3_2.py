num = int(input('Enter a number: '))
divlist = []
for number in list(range(1, int(num / 2 + 1))):
    if num % number == 0:
        divlist.append(number)

divlist.append(num)
print(divlist)