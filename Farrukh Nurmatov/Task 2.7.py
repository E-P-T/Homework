"""Write a program which makes a pretty print of a part of the multiplication table."""

# input parameters
a = 2
b = 4
c = 3
d = 7


# calculating multiplication table
matrix = []
for i in range(a, b + 1):
    lst = []
    for j in range(c, d + 1):
        lst.append(i * j)
    matrix.append(lst)

# calculating parameters for .ljust() function
max_num_len = len(str(matrix[-1][-1]))  # length of the one cell in the table
max_str_len = len("0 " + " ".join(str(i).ljust(len(str(i))) for i in matrix[-1]))  # length of the one row in the table

"""pretty printing"""
# top row of multipliers printing
print(" ".join(str(i).ljust(max_num_len) for i in range(c, d + 1)).rjust(max_str_len))

for i in range(a, b + 1):
    print(i, end=" ")  # colon multiplier printing
    print(" ".join(str(i).ljust(max_num_len) for i in matrix[i - 2]).ljust(max_str_len))  # print row of the table

