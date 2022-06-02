# Task 6.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

# Encryption:
# Keyword is "Crypto"

# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z

# Example:
# ```python
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"

# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
# ```

from collections import deque
import string


class Cipher:
    """The Keyword encoding and decoding for latin alphabet class."""

    base_alphabet = deque(string.ascii_uppercase)

    def __init__(self, keyword: str):
        """
        Initialize encryption alphabet using `keyword`.
        """
        self._alphabet = deque(keyword.upper())
        rest_alphabet = deque(filter(lambda ch: ch not in keyword.upper(), self.base_alphabet))
        self._alphabet.extend(rest_alphabet)

    def encode(self, string: str) -> str:
        """
        Encode target `string` with keyword specified in constructor. Print the result.
        """
        encoded_str = ""
        for ch in string:
            if ch.isalpha():
                encoded_ch = self._alphabet[self.base_alphabet.index(ch.upper())]
                encoded_str += encoded_ch if ch.isupper() else encoded_ch.lower()
            else:
                encoded_str += ch

        print(encoded_str)
        return encoded_str

    def decode(self, string: str) -> str:
        """
        Decode `string` encoded with keyword specified in constructor. Print the result.
        """
        decoded_str = ""
        for ch in string:
            if ch.isalpha():
                encoded_ch = self.base_alphabet[self._alphabet.index(ch.upper())]
                decoded_str += encoded_ch if ch.isupper() else encoded_ch.lower()
            else:
                decoded_str += ch

        print(decoded_str)
        return decoded_str


def main():
    """
    Entry point function.
    """
    cipher = Cipher("crypto")
    cipher.encode("Hello world")
    cipher.decode("Fjedhc dn atidsn")


if __name__ == '__main__':
    main()
