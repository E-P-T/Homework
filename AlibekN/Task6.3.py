from string import ascii_letters

class Cipher:
    def __init__(self, ciph=""):
        #initialize alphabet and decode alphabet
        self.alph = ascii_letters
        self.decode_alph = ciph
        for ch in self.alph[:26]:
            if ch not in ciph:
                self.decode_alph += ch
        self.decode_alph += self.decode_alph.upper()
    
    def encode(self, word):
        result = ""
        for ch in word:
            if ch not in self.alph:
                result += ch
                continue
            char_index = self.alph.find(ch)
            result += self.decode_alph[char_index]
        print(result)

    def decode(self, word):
        result = ""
        for ch in word:
            if ch not in self.alph:
                result += ch
                continue
            char_index = self.decode_alph.find(ch)
            result += self.alph[char_index]
        print(result)

    def print_alph(self):
        print(self.alph)
        print(self.decode_alph)

ch = Cipher("crypto")
ch.encode("Hello world")
ch.decode("Fjedhc dn atidsn")