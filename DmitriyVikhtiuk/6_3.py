class Cipher:
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z", " ", ",", ".", "!", "?", ":", ";", "'", '"']

    def __init__(self, keyword):
        self.word = keyword.upper()
        self.word_to_list = [char for char in self.word]
        self.second_part_of_new_alpha = [elem for elem in self.alpha if elem not in self.word_to_list]
        self.new_alpha = self.word_to_list + self.second_part_of_new_alpha

    def encode(self, s):
        result = ""
        up = s.upper()
        for char in up:
            i = self.alpha.index(char)
            result += self.new_alpha[i]
        print(result.lower().capitalize())

    def decode(self, s):
        result = ""
        up = s.upper()
        for char in up:
            i = self.new_alpha.index(char)
            result += self.alpha[i]
        print(result.lower().capitalize())

cipher = Cipher("crypto")
cipher.encode("Hello world")
cipher.decode("Fjedhc dn atidsn")

