# Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

def find_palindromes_no_reverse(string: str) -> bool:
    """
    The function takes a string as an argument and returns True if it is a palindrome and False if it is not
    :param string: input string
    :return: boolean
    :raises AssertionError if input is not string type
    """
    assert isinstance(string, str), 'Incorrect input. Input must be a string'
    ignore_set = set("""\t\n !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
    letters_sequence = ''.join([i for i in string if i not in ignore_set])
    for i in range(len(letters_sequence) // 2):
        if letters_sequence[i].lower() != letters_sequence[len(letters_sequence) - 1 - i].lower():
            return False
    return True


# s = 'а роза упала на лапу азора'
# s = "Mr. Owl ate my metal worm"
# s = '11/11/11 11:11'
# s = ''
# print(find_palindromes_no_reverse(s))
