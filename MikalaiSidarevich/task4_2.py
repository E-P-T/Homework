# Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

from string import punctuation, whitespace


def is_palindrome(s: str) -> bool:
    """
    Check whether a `s` is a palindrome or not.
    """
    garbage = punctuation + whitespace
    s = ''.join(filter(lambda ch: ch not in garbage, s))
    s = s.lower()
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True


def main():
    """
    Entry point function.
    """
    s = "Redivider"
    print(f"'{s}' is{' ' if is_palindrome(s) else ' not '}a palindrome")
    s = "Hello"
    print(f"'{s}' is{' ' if is_palindrome(s) else ' not '}a palindrome")
    s = "Mr. Owl ate my metal worm"
    print(f"'{s}' is{' ' if is_palindrome(s) else ' not '}a palindrome")


if __name__ == '__main__':
    main()
