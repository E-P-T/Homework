# The Task 4.2


def ispalindrome(raw_data: str) -> bool:
    '''Is the string a palindrome?'''
    line_without_spaces = ''.join(char.lower()
                                  for char in raw_data if char.isalnum())

    len_data = len(line_without_spaces)

    if len_data < 2:
        return False

    middle = round(len_data/2)
    col = middle if len_data % 2 == 0 else middle-1

    for i in range(col):
        if line_without_spaces[i] != line_without_spaces[-1*i-1]:
            return False

    return True
