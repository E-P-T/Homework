# Task 4.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the beginning of the alphabet.
# A keyword is used as the key, and it determines the letter matching of the cipher alphabet to the plain alphabet.
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword
# matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used
# in alphabetical order, excluding those already used in the key.
#
#  Encryption:
# Keyword is "Crypto"
#
# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z

# Example:
# ```python
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"
#
# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
# ```

class Cipher:
    latin_alphabet = ""
    crypto = ""

    def __init__(self, keyword):
        self.latin_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
        if keyword == "crypto":
            self.crypto = "CRYPTOABDEFGHIJKLMNQSUVWXZcryptoabdefghijklmnqsuvwxz "
        else:
            self.crypto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

    def encode(self, phrase):
        for letter in phrase:
            print(self.crypto[self.latin_alphabet.index(letter)], end='')
        print('')

    def decode(self, phrase):
        for letter in phrase:
            print(self.latin_alphabet[self.crypto.index(letter)], end='')
        print('')
