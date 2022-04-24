
# Sizes of table
print('a = ', end='')
a = int(input())
print('b = ', end='')
b = int(input())
print('c = ', end='')
c = int(input())
print('d = ', end='')
d = int(input())

max_w = len(str(d * b))

print('|'.ljust(max_w), end=' ')
for column in range(c, d + 1):
    print(str(column).ljust(max_w), end=' ')

print('')

for row in range(a, b + 1):
    print(str(row).ljust(max_w), end=' ')
    for column in range(c, d + 1):
        print(str(row*column).ljust(max_w), end=' ')
    print('')