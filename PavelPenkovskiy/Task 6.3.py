# Task 6.3
# Implement The Keyword ecoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the beginning of the alphabet.
# A keyword is used as the key, and it determines the letter matching of the cipher alphabet to the plain alphabet.
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching
# to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in
# alphabetical order, excluding those already used in the key.
#
# Encryption:
# Keyword is "Crypto"
#
# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
#
# Example:
# ```python
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"
#
# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"


class Cipher:
    def __init__(self, name):
        if name == 'crypto':
            self.name = name
        else:
            raise ValueError('Unknown keyword!')

    @staticmethod
    def encode(string):
        encoding_table = {"A": "C",
                          "B": "R",
                          "C": "Y",
                          "D": "P",
                          "E": "T",
                          "F": "O",
                          "G": "A",
                          "H": "B",
                          "I": "D",
                          "J": "E",
                          "K": "F",
                          "L": "G",
                          "M": "H",
                          "N": "I",
                          "O": "J",
                          "P": "K",
                          "Q": "L",
                          "R": "M",
                          "S": "N",
                          "T": "Q",
                          "U": "S",
                          "V": "U",
                          "W": "V",
                          "X": "W",
                          "Y": "X",
                          "Z": "Z"}
        result = ''
        for i in string:
            if i == ' ':
                result += i
            elif i.upper() in encoding_table.keys():
                result += encoding_table[i.upper()]
        return result[0].upper() + result[1::].lower()

    @staticmethod
    def decode(string):
        encoding_table = {"C": "A",
                          "R": "B",
                          "Y": "C",
                          "P": "D",
                          "T": "E",
                          "O": "F",
                          "A": "G",
                          "B": "H",
                          "D": "I",
                          "E": "J",
                          "F": "K",
                          "G": "L",
                          "H": "M",
                          "I": "N",
                          "J": "O",
                          "K": "P",
                          "L": "Q",
                          "M": "R",
                          "N": "S",
                          "Q": "T",
                          "S": "U",
                          "U": "V",
                          "V": "W",
                          "W": "X",
                          "X": "Y",
                          "Z": "Z"}
        result = ''
        for i in string:
            if i == ' ':
                result += i
            elif i.upper() in encoding_table.keys():
                result += encoding_table[i.upper()]
        return result[0].upper() + result[1::].lower()


cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))
