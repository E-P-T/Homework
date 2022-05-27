### Task 4.3
'''Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.
<em> Encryption:
Keyword is "Crypto"
* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
</em>
Example:
```python
cipher = Cipher("crypto")
cipher.encode("Hello world")
"Btggj vjmgp"
cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
'''


class Cipher:
    __ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, keyword):
        self.__build_mappings(keyword)

    def __build_mappings(self, keyword):
        prepared_key = ''.join(list(dict.fromkeys(list(keyword)))).lower()
        without_duplicates = ''.join([c for c in Cipher.__ALPHABET if c not in prepared_key])

        lower_mapping = prepared_key + without_duplicates

        self.__from_alphabet = Cipher.__ALPHABET + Cipher.__ALPHABET.upper()
        self.__to_alphabet = lower_mapping + lower_mapping.upper()

        print(self.__from_alphabet)
        print(self.__to_alphabet)

    def __change(self, sentence, old_alphabet, new_alphabet):
        return ''.join([new_alphabet[old_alphabet.index(c)] if c in old_alphabet else c for c in sentence])

    def encode(self, sentence):
        return self.__change(sentence, self.__from_alphabet, self.__to_alphabet)

    def decode(self, sentence):
        return self.__change(sentence, self.__to_alphabet, self.__from_alphabet)


cipher = Cipher("Crypto")
encoded = cipher.encode("Hello, my name is Альгис")
print(encoded)
decoded = cipher.decode(encoded)
print(decoded)

print(cipher.encode("Hello world"))  # "Btggj vjmgp"
print(cipher.decode("Fjedhc dn atidsn"))  # "Kojima is genius"
