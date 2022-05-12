"""
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of
the cipher alphabet to the plain alphabet. 
Repeats of letters in the word are removed, then the cipher alphabet
is generated with the keyword matching to A, B, C etc. until the keyword is used up,
whereupon the rest of the ciphertext letters are used in alphabetical order,
excluding those already used in the key.
"""

import string

class Cipher:
    def __init__(self, word):
        self.dict = {} # crypto dictionary
        init_list = list(string.ascii_lowercase) # variable of list of alphabet
        cryp_list = list(string.ascii_lowercase)  # variable of list of alphabet without crypto string
        # fill letters of crypto word
        for i in range(len(word)):
            flag = 0
            for val in self.dict.values():
                if word[i] == val: flag = 1
            if flag == 1: break
            self.dict[string.ascii_lowercase[i]] = word[i]
            init_list.remove(string.ascii_lowercase[i])
            cryp_list.remove(word[i])
        # fill tha rest letters
        for i in range(len(init_list)):
            self.dict[init_list[i]] = cryp_list[i]
        # fill letters of the uppercase
        for i in string.ascii_uppercase:
            self.dict[i] = self.dict[i.lower()].upper()
        self.dict[' '] = ' '

    def encode(self, encode_str):
        res = []
        for i in encode_str:
            res.append(self.dict[i])
        print(''.join(res))

    def decode(self, decode_str):
        res = []
        for letter in decode_str:
            for k, v in self.dict.items():
                if v == letter:
                    res.append(k)       
        print(''.join(res))