# The Task 4.4

from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """Splits the `s` string by indexes specified in `indexes`

    Indices are in ascending order.
    """

    list_out: List[str] = []
    k = 0

    len_ = len(s)
    list_out_append = list_out.append

    if not indexes:
        list_out_append(s)
        return list_out

    for i in indexes:
        if i <= 0:
            list_out.clear()
            list_out_append(s)
            return list_out

        elif k < len_ and i > k:
            list_out_append(s[k:i])
            k = i
        else:
            break

    if k < len_:
        list_out_append(s[k:])

    return list_out
