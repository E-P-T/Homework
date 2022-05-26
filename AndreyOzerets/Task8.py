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


if __name__ == '__main__':

    s = [1, 2, 3, 8, 9]
    # s=[1]
    # s = ['need', 'to', 'sleep', 'more']
    # s = ['need']

    print()
    print('{:*^30}'.format('Task 4.8'), end='\n\n')
    print(f'Function result: {get_pairs(s)}', end='\n\n')
