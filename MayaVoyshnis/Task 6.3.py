ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

class Cipher:
    def __init__(self, key):
        self._key = key
        self._new_alphabet = self._make_alphabet()

    def _make_alphabet(self):
        key = list(self._key.upper())
        key.extend(ALPHABET)
        return list(dict.fromkeys(key))

    def encode(self, text):
        final = []
        for el in text:
            if el.isalpha():
                if el in ALPHABET:
                    final.append(self._new_alphabet[ALPHABET.index(el)])
                else:
                    final.append(self._new_alphabet[ALPHABET.index(el.upper())].lower())
            else:
                final.append(el)
        return ''.join(final)

    def decode(self, text):
        final = []
        for el in text:
            if el.isalpha():
                if el in ALPHABET:
                    final.append(ALPHABET[self._new_alphabet.index(el)])
                else:
                    final.append(ALPHABET[self._new_alphabet.index(el.upper())].lower())
            else:
                final.append(el)
        return ''.join(final)

cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))
