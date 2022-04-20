### Task 2.7
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# ```
# Input:
# a = 2
# b = 4
# c = 3
# d = 7

# Output:
# 	3	4	5	6	7	
# 2	6	8	10	12	14	
# 3	9	12	15	18	21	
# 4	12	16	20	24	28
# ```

a, b, c, d = int(input('a = ')), int(input('b = ')), int(input('c = ')), int(input('d = '))
print(end = '\t')
for x in range(c, d + 1):
        print(x, end = ' \t')
print()
for y in range(a, b + 1):
    print(y, end = '\t')
    for x in range(c, d + 1):
        print(x * y, end = '\t')
    print()