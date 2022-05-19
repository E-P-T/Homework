import string

class Cipher:
    letters_alphabet = list(string.ascii_lowercase)
    unique_ciphers = list()
    ciphers_alphabet = list()
    letters_of_ciphers = dict() # cipher: original_letter pairs
    ciphers_of_letters = dict() # original_letter: cipher pairs
    
    def __init__(self, keyword) -> None:
        self.keyword = keyword
        for c in self.keyword:
            if c not in self.unique_ciphers:
                self.unique_ciphers.append(c)

        for i in range(len(self.unique_ciphers)):
                self.ciphers_alphabet.append(self.unique_ciphers[i])
        for i in range(len(self.letters_alphabet)):        
            if self.letters_alphabet[i] not in self.unique_ciphers:
                self.ciphers_alphabet.append(self.letters_alphabet[i])

        self.letters_of_ciphers = {
            cipher: original_letter
            for cipher, original_letter in zip(self.ciphers_alphabet, self.letters_alphabet)
        }
        self.ciphers_of_letters = {
            original_letter: cipher
            for cipher, original_letter in zip(self.ciphers_alphabet, self.letters_alphabet)
        }

    def encode(self, original_str: str):
        ciphered_str = ""
        for character in original_str:
            if character.lower() not in self.ciphers_of_letters.keys():
                ciphered_str += character
                continue
            ciphered_str += self.ciphers_of_letters[character.lower()].upper() if character.isupper() else self.ciphers_of_letters[character]
        return ciphered_str
    
    def decode(self, ciphered_str):
        original_str = ""
        for character in ciphered_str:
            if character.lower() not in self.letters_of_ciphers.keys():
                original_str += character
                continue
            original_str += self.letters_of_ciphers[character.lower()].upper() if character.isupper() else self.letters_of_ciphers[character]
        return original_str    
