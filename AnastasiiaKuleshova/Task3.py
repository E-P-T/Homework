# Task 6.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the beginning of the alphabet. A keyword is used as
# a key, and it determines the letter matching of the cipher alphabet
# to the plain alphabet. Repeats of letters in the word are removed,
# then the cipher alphabet is generated with the keyword matching to A, B, C etc.
# until the keyword is used up, whereupon the rest of the ciphertext letters are
# used in alphabetical order, excluding those already used in the key.
#
# Encryption: Keyword is "Crypto"
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# Example:
#
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"
#
# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
import string


class Cipher:
    _alphabet = list(string.ascii_lowercase)
    _coding_dict = {}
    _decoding_dict = {}

    def __init__(self, key_word: str):
        self._get_coding_dict(key_word)

    def _get_coding_dict(self, key_word):
        temp_string = ""
        for letter in key_word:
            if not temp_string.__contains__(letter):
                temp_string += letter
        for letter in self._alphabet:
            if not temp_string.__contains__(letter):
                temp_string += letter
        for i in range(0, len(self._alphabet)):
            self._coding_dict[self._alphabet[i].lower()] = temp_string[i].lower()
            self._decoding_dict[temp_string[i].lower()] = self._alphabet[i].lower()

    def encode(self, encodeable_word: str):
        result = ""
        for letter in encodeable_word:
            letter_lower = letter.lower()
            if not self._coding_dict.__contains__(letter_lower):
                result += letter_lower
            elif letter.isupper():
                result += self._coding_dict[letter.lower()].upper()
            else:
                result += self._coding_dict[letter.lower()]
        print(result)

    def decode(self, decodable_word: str):
        result = ""
        for letter in decodable_word:
            letter_lower = letter.lower()
            if not self._decoding_dict.__contains__(letter_lower):
                result += letter_lower
            elif letter.isupper():
                result += self._decoding_dict[letter.lower()].upper()
            else:
                result += self._decoding_dict[letter.lower()]
        print(result)


cipher = Cipher("crypto")
cipher.encode("Hello world")
cipher.decode("Btggj vjmgp")

cipher1 = Cipher("babenastya")
cipher1.encode("Hello world")
cipher1.decode('Cshhk vkohn')
