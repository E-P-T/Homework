"""Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed,
then the cipher alphabet is generated with the keyword matching to A, B, C etc.
until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order,
excluding those already used in the key."""
from string import ascii_lowercase as low_chars


class Cipher:
    def __init__(self, code_word):
        self.codes = list(code_word)
        self.char_lst = list(low_chars)
        self.coded_alph = self.codes + [i for i in self.char_lst if i not in self.codes]

    def encode_word(self, string):
        coded_str = ''
        for char in string:
            if char.isupper():
                coded_str += self.coded_alph[self.char_lst.index(char.lower())].upper()
            else:
                coded_str += self.coded_alph[self.char_lst.index(char)]
        return coded_str

    def decode_word(self, string):
        decoded_str = ''
        for char in string:
            if char.isupper():
                decoded_str += self.char_lst[self.coded_alph.index(char.lower())].upper()
            else:
                decoded_str += self.char_lst[self.coded_alph.index(char)]
        return decoded_str

    def encode(self, frase):
        frase_lst = frase.split()
        encoded_lst = [self.encode_word(word) for word in frase_lst]
        return " ".join(encoded_lst)

    def decode(self, frase):
        frase_lst = frase.split()
        decoded_lst = [self.decode_word(word) for word in frase_lst]
        return " ".join(decoded_lst)


if __name__ == "__main__":
    cipher = Cipher("crypto")
    print(cipher.encode("Hello world"))
    print(cipher.decode("Fjedhc dn atidsn"))

