# Task 6.3
# Implement The Keyword encoding and decoding for latin alphabet. The Keyword Cipher uses a Keyword to rearrange the
# letters in the alphabet. Add the provided keyword at the begining of the alphabet. A keyword is used as the key,
# and it determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the word
# are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is
# used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used
# in the key.

from string import ascii_lowercase, ascii_uppercase


class Cipher(object):
    """
    The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.  The keyword is used as the key,
    and it determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the word
    are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is
    used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used
    in the key.
    """


    def __init__(self, keyword: str):
        self._keyword = Cipher.process_keyword(keyword)
        self._alphabet = ascii_lowercase + ascii_uppercase
        shift = self._keyword + ''.join(sorted(set(ascii_lowercase) - set(self._keyword)))
        self._shifted_alphabet = shift + shift.upper()
        self._encode_dict = {key: value for key, value in zip(self._alphabet, self._shifted_alphabet)}
        self._decode_dict = {key: value for key, value in zip(self._shifted_alphabet, self._alphabet)}

    @staticmethod
    def process_keyword(keyword):
        """
        processes the input keyword, removing repeating letters and returns a new string
        :param keyword: string
        :return: processed string
        """
        result = []
        for letter in keyword:
            if letter.lower() not in result:
                result.append(letter.lower())
        return ''.join(result)

    def encode(self, sentence: str):
        """
        encodes input string using _encode_dict as reference
        :param sentence: input string
        :return: encoded string
        """
        result = []
        for letter in sentence:
            result.append(self._encode_dict[letter] if letter in self._encode_dict else letter)
        return ''.join(result)

    def decode(self, sentence: str):
        """
        decodes input string using _decode_dict as reference
        :param sentence: input string
        :return: decoded string
        """
        result = []
        for letter in sentence:
            result.append(self._decode_dict[letter] if letter in self._decode_dict else letter)
        return ''.join(result)




cipher = Cipher("Crypto")
print(cipher.encode("Hello world"))
# "Btggj vjmgp"
print(cipher.decode("Fjedhc dn atidsn!"))
# "Kojima is genius"