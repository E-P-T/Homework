"""
Task 6.3
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc.
Until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order,
excluding those already used in the key.

Encryption:
Keyword is "Crypto"

* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z


Example:
cipher = Cipher("crypto")
cipher.encode("Hello world")
"Btggj vjmgp"
cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"

"""
import string


class Cipher:
    def __init__(self, cipher):
        self.cipher = list(cipher)
        self.alpha = list(string.ascii_lowercase)
        for char in cipher:
            self.alpha.pop(self.alpha.index(char))
        self.cipher.extend(self.alpha)

    def encode(self, message: str):
        encoded = str()
        alphabet = list(string.ascii_lowercase)
        for m in message.lower():
            if m in alphabet:
                encoded += self.cipher[alphabet.index(m)]
            else:
                encoded += ' '
        return encoded

    def decode(self, message: str):
        decoded = str()
        for m in message.lower():
            if m in self.cipher:
                decoded += list(string.ascii_lowercase)[self.cipher.index(m)]
            else:
                decoded += ' '
        return decoded


c = Cipher("crypto")
print(c.encode('Hello world'))
print(c.decode("Fjedhc dn atidsn"))

