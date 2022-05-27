class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.validate_input()
        self._numbers = range(self.start, self.end)
        self._even_numbers = [n for n in self._numbers if n % 2 == 0]
        self.__i = 0
    
    def validate_input(self):
        if not isinstance(self.start, int) or not isinstance(self.end, int) or (self.start > self.end):
            raise TypeError
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__i < len(self._even_numbers):
            self.__i += 1
            return self._even_numbers[self.__i-1]
        else:
            print("Out of numbers")
            raise StopIteration

   
if __name__ == "__main__":
    a = EvenRange(1, 10)
    for i in a:
        print(i)