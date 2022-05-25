# Task 2.1

def get_str(greeting: str) -> str:
    '''Return the entered string
    '''
    seq = input(greeting)
    return seq


def len_str(string: str) -> int:
    '''Count the number of characters.'''
    return sum(1 for _ in string)
