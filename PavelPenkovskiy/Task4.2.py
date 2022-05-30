# Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).


def is_palindrome(string):
    result = ''
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result == string


print(is_palindrome('abcba'))
