"""
Implement The Keyword encoding and decoding for latin alphabet. The Keyword Cipher uses a Keyword to rearrange
the letters in the alphabet. Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching
to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical
order, excluding those already used in the key.

Encryption: Keyword is "Crypto"
"""
import string

class Cipher:


    def __init__(self, crypt_keyt):
        self.main_alphabet = string.ascii_lowercase + string.ascii_uppercase
        kw = crypt_keyt + self.main_alphabet
        self.new_alpha = "".join(sorted(set(kw), key=kw.index))
        print(self.main_alphabet)
        print(self.new_alpha)


    def encode(self, word):
        cr = ""
        for i in range(len(word)):
            position = self.main_alphabet.find(word[i])
            if position == -1:
                cr += word[i]
            else:
                cr += self.new_alpha[position]
        return cr

    def decode(self, word):
        cr = ""
        for i in range(len(word)):
            position = self.new_alpha.find(word[i])
            if position == -1:
                cr += word[i]
            else:
                cr += self.main_alphabet[position]
        return cr

c = Cipher("Crypto")
print(c.decode("Norayr"))
print(c.decode("Htffi Wilfp"))



