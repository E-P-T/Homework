import string;


class Cipher:
    alphabet = list(string.ascii_lowercase)
    cipher = list(string.ascii_lowercase)

    def init(self, keyword):
        self.keyword = keyword

        for k in keyword[::-1]:
            self.cipher.remove(k)
            self.cipher.insert(0, k)

    def encode(self, text):
        lowerText = text.lower()
        encodedText = ''
        for i in text:
            if i.lower() in self.alphabet:
                char = self.cipher[self.alphabet.index(i.lower())]
                if i.isupper():
                    char = char.upper()
                encodedText += char
            else:
                encodedText += i
        return encodedText

    def decode(self, text):
        decodedText = ''
        for i in text:
            if i.lower() in self.alphabet:
                char = self.alphabet[self.cipher.index(i.lower())]
                if i.isupper():
                    char = char.upper()
                decodedText += char
            else:
                decodedText += i
        return decodedText


c = Cipher('xyz')
text = 'Barev aper'
e = c.encode(text)
d = c.decode(e)
print(text)
print(e)
print(d)
