""" Task 2.7
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


def multiplication_table(a, b, c, d):
    matrix = []
    for i in range(b - a + 2):
        matrix.append([None] * (d - c + 2))

    iterator = c
    for i in range(len(matrix[0])):
        if i == 0:
            matrix[0][i] = ' '
        else:
            matrix[0][i] = iterator
            iterator += 1

    iterator = a
    for i in range(len(matrix)):
        if i == 0:
            pass
        else:
            matrix[i][0] = iterator
            iterator += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or j == 0:
                pass
            else:
                matrix[i][j] = matrix[0][j] * matrix[i][0]

    return matrix


# input
matrix = multiplication_table(5, 9, 2, 5)

# output
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
