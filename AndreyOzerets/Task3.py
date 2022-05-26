# The Task 4.3

from typing import List


def new_split(str_: str, sep: str = ' ', maxsplit: int = -1) -> List[str]:
    '''Return the given number of words from a string.'''

    out: List[str] = []
    out_append = out.append

    start = 0

    while maxsplit:
        stop = str_.find(sep, start)
        if stop == -1:
            out_append(str_[start:])
            break
        else:
            out_append(str_[start:stop])
            start = stop + 1
            maxsplit -= 1
    return out


if __name__ == '__main__':

    s = "Implement a function which works the same as `str.split` method"

    print()
    print('{:*^30}'.format('Task 4.3'), end='\n\n')

    print(new_split(s, maxsplit=4))
    print()
