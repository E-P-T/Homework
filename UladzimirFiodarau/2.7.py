# Task 2.7
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# Input:
# a = 2
# b = 4,
# c = 3
# d = 7
# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28


def compute_multiplication_table(a, b, c, d):
    """
    The function takes four integers and computes the multiplication table, with rows numbers from a to b,
    columns numbers from c to d, and items in intersections equal to the result of multiplication of corresponding
    row number and column number
    :param a: starting number in the rows
    :param b: ending number in the rows, b >= a
    :param c: starting number in the columns
    :param d: ending number in the columns d >= c
    :return: a filled matrix (list of lists)
    """
    assert all(map(lambda x: isinstance(x, int), [a, b, c, d])), 'Incorrect input. All attributes must be integer type'
    assert b >= a and d >= c, "Incorrect input, ending numbers of rows and columns must be greater then " \
                              "starting numbers or equal to them"
    assert a >= 0 and b >= 0 and c >= 0 and d >= 0, "Incorrect input, the starting and ending numbers of " \
                                                    "rows and columns must be greater then zero or equal to it"
    rows = b - a + 2
    columns = d - c + 2
    matrix = [[None] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if i == 0 and j != 0:
                matrix[i][j] = 1 * (j + c - 1)
            elif i != 0 and j == 0:
                matrix[i][j] = 1 * (i + a - 1)
            elif i != 0 and j != 0:
                matrix[i][j] = (j + c - 1) * (i + a - 1)

    return matrix


def pretty_print(matrix: list, ljust=4, rjust=0):
    """
    The function takes a matrix (list of lists) as argument and makes a print of its items in a form of a table
    with an option of tweaking of sizes of left and right aligns of the printed item
    :param matrix: the input matrix (list of lists)
    :param ljust: the size of left align of the printed matrix item, the default size is 4 symbols
    :param rjust: the size of right align of the printed matrix item, the default size is 0 symbols
    :return: None
    """

    assert isinstance(matrix, list) and all(
        map(lambda x: isinstance(x, list), matrix)), 'Incorrect input. Must be a list of lists'
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if not isinstance(matrix[i][j], int):
                print(''.ljust(ljust).rjust(rjust), end='')
            else:
                print(str(matrix[i][j]).ljust(ljust).rjust(rjust), end='')
        print()



