# ### Task 6.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. 
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C
# etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order,
# excluding those already used in the key.

# <em> Encryption:
# Keyword is "Crypto"

# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# </em>

# Example:
# ```python
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"

# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
# ```
import string


class Cipher:
    def __init__(self, word):
        alfa = list(string.ascii_uppercase)
        new_list = []
        for i in word.upper():
            if i in new_list:
                continue
            else:
                new_list.append(i)
        for i in alfa:
            if i in new_list:
                continue
            else:
                new_list.append(i)
        self.dict = {alfa[i]: new_list[i] for i in range(len(alfa))}

    def encode(self, encodeStr):
        ret = ''
        for i in encodeStr:
            if i.isalpha():
                if i.islower():
                    ret += str(self.dict[i.upper()]).lower()
                else:
                    ret += self.dict[i]
            else:
                ret += i
        print(ret)

    def decode(self, decodeStr):
        ret = ''
        for i in decodeStr:
            flag = False
            if i.isalpha():
                if i.islower():
                    flag = True
                    i = i.upper()
                for k, v in self.dict.items():
                    if v == i:
                        if flag:
                            s = str(k).lower()
                            flag = False
                        else:
                            s = k
                        ret += s
            else:
                ret += i
        print(ret)


d = Cipher("Crypto")
d.encode("Hello world")
d.decode("Btggj vjmgp")
