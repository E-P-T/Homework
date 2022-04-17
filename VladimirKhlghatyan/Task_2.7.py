# Task 2.7
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# ```
# Input:
# a = 2
# b = 4
# c = 3
# d = 7
#
# Output:
#     3   4   5   6   7
# 2   6   8  10  12  14
# 3   9  12  15  18  21
# 4  12  16  20  24  28
# ```


def multiplication_table(a, b, c, d):
    print('', end='\t')
    for n in range(c, d + 1):
        print(n, end='\t')
    print('')
    for n in range(a, b + 1):
        print(n, end='\t')
        for nb in range(c, d + 1):
            print(n * nb, end='\t')
        print('')
