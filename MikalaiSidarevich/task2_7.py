# Task 2.7
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

a, b, c, d = 2, 4, 3, 7

header = [n for n in range(c, d+1)]

# Print header
print("{z:>2s} ".format(z=' '), end='')
for i in header:
    print(f"{i:>2d} ", end='')
print()

# Print table
for i in range(a, b+1):
    print(f"{i:>2d} ", end='')
    for j in range(c, d+1):
        print(f"{i*j:>2d} ", end='')
    print()
