# Task 4.8


from typing import List, Tuple, Optional


def get_pairs(lst: List) -> Optional[List[Tuple]]:
    '''Return a list of tuples containing pairs of elements'''

    result: Optional[List[Tuple]] = []

    len_ = len(lst)

    if len_ > 1:
        result = [(lst[i], lst[i+1]) for i in range(len_-1)]
    else:
        result = None

    return result
