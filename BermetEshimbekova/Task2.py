# Task 4.2

import re
strings = [
    "Palindromes often consist of a sentence or phrase, e.g.,",
    "Mr. Owl ate my metal worm",
    "Do geese see God?",
    "Was it a car or a cat I saw?"
    "Punctuation, capitalization, and spaces are usually ignored."
    "Rats live on no evil star",
    "Live on time, emit no evil",
    "Step on no pets"
    ]


def is_palindrome(s):
    s = re.sub('\W', '', s).lower()
    result = True
    for i in range(1, len(s)//2+1):
        if s[i-1] != s[-i]:
            result = False
            break
    return result


for string in strings:
    if is_palindrome(string):
        print('"' + string + '"', 'is a palindrome')
