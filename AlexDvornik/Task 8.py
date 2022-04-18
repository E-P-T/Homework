"""
Task 2.8
Write a program which makes a pretty print of a part of the multiplication table.
Examples:
Input:
a = 2
b = 4
c = 3
d = 7
Output:
	3	4	5	6	7
2	6	8	10	12	14
3	9	12	15	18	21
4	12	16	20	24	28
"""

print('Enter your numbers in the following format "a=1"...')
rows_ = sorted([int(input()[-1]) for i in range(3)])
columns_ = [j for j in range(min(rows_) + 1, int(input()[-1]) + 1)]

for item in columns_:
    print('\t ' + str(item), end=' ')
print()

for i in rows_:
    print(str(i).rjust(2), end=' ')
    for j in columns_:
        print(str(i * j).rjust(3), end=' ')
    print()
