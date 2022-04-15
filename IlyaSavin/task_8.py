# TASK2.8 FROM LECTION 2
"""
This module contains 1 function aimed at printing multiplication table.
"""


def print_multiplication_table(bvb, tvb, bhb, thb):
    """
    This function can print multiplication table from any to any numbers.
    It will print correctly.
    Arguments:
        1) bvb - botton vertical border
        2) tvb - top vertical border
        3) bhb - bottom horizontal border
        4) thb - top horizontal border
    """
    vertical_numbers = list(range(bvb, tvb + 1))
    horizontal_numbers = list(range(bhb, thb + 1))
    indent = '  '

    # add space to print vertical_numbers and horizontal_numbers on their spots
    horizontal_numbers.insert(0, ' ')

    # max_number contains width parameter for formatting
    max_number = tvb * thb

    # max_digits is max width
    max_digits = len(str(max_number))

    # barlen - horizontal length of a multiplication table
    barlen = (max_digits + len(indent)) * len(horizontal_numbers) + len(indent)

    print('-' * barlen)
    print('|', end='')
    for i in horizontal_numbers:
        print('%*s' % (max_digits, i), end=indent)
    print('|')
    # after this loop we can see top border of a table and first string

    # deleting space to ease calculate values of a table
    horizontal_numbers.pop(0)

    # printing the rest part of a table except for bottom border
    for i in vertical_numbers:
        print('|%*s' % (max_digits, i), end=indent)
        for j in horizontal_numbers:
            print('%*s' % (max_digits, j * i), end=indent)
        print('|')

    # printing bottom border of a table
    print('-' * barlen)


if __name__ == '__main__':
    is_right = False
    while not is_right:
        try:
            bvb = int(input("Input bottom vertical border: "))
            tvb = int(input("Input top vertical border: "))
            bhb = int(input("Input bottom horizontal border: "))
            thb = int(input("Input top horizontal border: "))
            is_right = True
        except ValueError:
            print('Cannot convert to integer.')

    print_multiplication_table(bvb, tvb, bhb, thb)

    # ------------------------Results----------------------------------------

    # for 2-4, 3-7
    # --------------------------
    # |     3   4   5   6   7  |
    # | 2   6   8  10  12  14  |
    # | 3   9  12  15  18  21  |
    # | 4  12  16  20  24  28  |
    # --------------------------

    # for 2-15, 3-13
    # --------------------------------------------------------------
    # |       3    4    5    6    7    8    9   10   11   12   13  |
    # |  2    6    8   10   12   14   16   18   20   22   24   26  |
    # |  3    9   12   15   18   21   24   27   30   33   36   39  |
    # |  4   12   16   20   24   28   32   36   40   44   48   52  |
    # |  5   15   20   25   30   35   40   45   50   55   60   65  |
    # |  6   18   24   30   36   42   48   54   60   66   72   78  |
    # |  7   21   28   35   42   49   56   63   70   77   84   91  |
    # |  8   24   32   40   48   56   64   72   80   88   96  104  |
    # |  9   27   36   45   54   63   72   81   90   99  108  117  |
    # | 10   30   40   50   60   70   80   90  100  110  120  130  |
    # | 11   33   44   55   66   77   88   99  110  121  132  143  |
    # | 12   36   48   60   72   84   96  108  120  132  144  156  |
    # | 13   39   52   65   78   91  104  117  130  143  156  169  |
    # | 14   42   56   70   84   98  112  126  140  154  168  182  |
    # | 15   45   60   75   90  105  120  135  150  165  180  195  |
    # --------------------------------------------------------------

    # for 30-40, 25-30
    # --------------------------------------------
    # |        25    26    27    28    29    30  |
    # |  30   750   780   810   840   870   900  |
    # |  31   775   806   837   868   899   930  |
    # |  32   800   832   864   896   928   960  |
    # |  33   825   858   891   924   957   990  |
    # |  34   850   884   918   952   986  1020  |
    # |  35   875   910   945   980  1015  1050  |
    # |  36   900   936   972  1008  1044  1080  |
    # |  37   925   962   999  1036  1073  1110  |
    # |  38   950   988  1026  1064  1102  1140  |
    # |  39   975  1014  1053  1092  1131  1170  |
    # |  40  1000  1040  1080  1120  1160  1200  |
    # --------------------------------------------

    # Note: Code doesn't contain speed tests bcse I don't get the point of it.
    # It also doesn't contain unit-tests bcse I don't save output in a string.
    # If you want to see output just run it.
