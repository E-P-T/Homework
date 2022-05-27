class MySquareIterator:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.numbers = self.squares()
        self.__i = 0

    def squares(self):
        square_numbers = list()
        try:
            for e in self.iterable:
                if not isinstance(e, int):
                    raise TypeError
        except TypeError:
            print("Only integers are allowed in this iterable!")
        else:
            for n in self.iterable:
                square_numbers.append(n**2)

        finally: 
            return square_numbers

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__i < len(self.numbers):
            self.__i += 1
            return self.numbers[self.__i - 1]

        self.__i = 0
        raise StopIteration


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    for i in MySquareIterator(lst):
        print(i)