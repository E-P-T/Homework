# The Task 4.6

def get_longest_word(s: str) -> str:
    '''Return the longest word from a string'''

    words = s.split()
    best = words[0]
    len_best = len(best)
    for v in words:
        if len_best < len(v):
            best = v
            len_best = len(best)
    return best


if __name__ == '__main__':

    s = 'Python is simple and effective!'
    # s = 'Any pythonista like namespaces a lot.'

    print()
    print('{:*^30}'.format('Task 4.6'), end='\n\n')
    print(f'A long word: {get_longest_word(s)}')
    print()
