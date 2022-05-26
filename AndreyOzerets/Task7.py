# Task 2.7


def indent_length(a: int, b: int, c: int, d: int) -> int:
    '''Return the length of the indent between columns.'''

    max_ab = max(a, b)
    max_cd = max(c, d)
    indent_length = len(str(max_ab*max_cd)) + 1

    return indent_length
