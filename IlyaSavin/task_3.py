#! /usr/bin/env python
# TODO: Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings
# of the cipher alphabet to the plain alphabet. Repeats of letters in the word
# are removed, then the cipher alphabet is generated with the keyword matching
# to A, B, C etc. until the keyword is used up, whereupon the rest of the
# ciphertext letters are used in alphabetical order, excluding those already
# used in the key.
#  Encryption: Keyword is "Crypto"
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# C R Y P T O A B D E F G H I J K L M N Q S U V W X Z


"""
task_3.py: implemented class Cipher, which can encode string or decode it and
some test stetement for this class.
"""


class Cipher:
    """
    Cipher: class which allow client encode or decode string.
    To encode or decode string it requires creating Cipher instance and
    call necessary method.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

    def __init__(self, cipher):
        self.cipher = self._remove_repeated_letters(cipher)
        self.alphabet = self._change_alphabet(Cipher.alphabet, self.cipher)

    def _remove_repeated_letters(self, string):
        result = ''
        for letter in string:
            if letter not in result:
                result += letter
        return result

    def _change_alphabet(self, alphabet, cipher):
        for letter in cipher:
            alphabet = alphabet.replace(letter.upper(), '')
        return cipher.upper() + alphabet

    def encode(self, string):
        is_upper = tuple(1 if x.isupper() else 0 for x in string)
        string = ''.join(self.alphabet[Cipher.alphabet.index(x.upper())] for x in string)
        return ''.join(x.lower() if i == 0 else x for i, x in zip(is_upper, string))

    def decode(self, string):
        is_upper = tuple(1 if x.isupper() else 0 for x in string)
        string = ''.join(Cipher.alphabet[self.alphabet.index(x.upper())] for x in string)
        return ''.join(x.lower() if i == 0 else x for i, x in zip(is_upper, string))


if __name__ == '__main__':
    cipher = Cipher('crypto')
    print(cipher.encode("Hello world"))  # Result: Btggj vjmgp
    print(cipher.decode("Fjedhc dn atidsn"))  # Result: Kojima is genius
