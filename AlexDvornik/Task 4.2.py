'''
Task 4.2
Write a function that check whether a string is a palindrome or not. Usage of
any reversing functions is prohibited.
'''


def is_palindrome(string: str) -> bool:
    new_string = str()
    s = len(string)
    while s > 0:
        new_string += string[s-1]
        s -= 1
    return bool(new_string == string)


print(is_palindrome("level"))

