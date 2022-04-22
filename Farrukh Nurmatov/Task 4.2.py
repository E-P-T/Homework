"""Write a function that check whether a string is a palindrome or not. Usage of
any reversing functions is prohibited. To check your implementation you can use
strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes)."""


def palindrome_check(word: str):
    """This function checks word being a palindrome by comparing original word and reversed word via slicing"""
    if word == word[::-1]:
        return "This word is palindrome!"
    else:
        return "This word isn't palindrome!"


if __name__ == '__main__':
    test_word = "level"
    print(palindrome_check(test_word))
    words = ["level", "noon", "deified", "peep", "nun", "deed", "tomato"]
    for word in words:
        print(palindrome_check(word))