# Task 4.2
'''Write a function that check whether a string is a palindrome or not.
Usage of any reversing functions is prohibited. To check your implementation you can use strings from here.
'''
# вопрос! можно ли использовать слайсинг

# def is_palindrome(s):
#     return s == s[::-1]
#
#
# print(is_palindrome("шалаш"))

def is_palindrome(string):
    reversed_string = ""
    for i in range(len(string), 0, -1):
        reversed_string += string[i-1]

    return reversed_string == string


print(is_palindrome("madam"))

# def is_palindrome(s):
#     length = len(s)
#     for i in range(length // 2):
#         if s[i] != s[length - 1 - i]:
#             return False
#     return True



