from collections.abc import Iterable


class MyNumberCollection:
    def __init__(self, start = [], end=None, step=None):
        self.start = start
        self.end = end
        self.step = 1 if isinstance(self.start, int) and not step else step        
        self.numbers = self.input_validity()
        self.__i = 0

    def input_validity(self):
        numbers = list()

        try:
            if isinstance(self.start, Iterable):
                if  (isinstance(self.start, Iterable) and (any((self.end, self.step)) or 0 in (self.end, self.step))):
                    raise AttributeError("You shouldn't provide `end` and `step` with Iterable!")
                for el in self.start:
                    if not isinstance(el, int):
                        raise TypeError

            elif isinstance(self.start, int):            
                if (self.start < self.end and self.step < 0) or (self.start > self.end and self.step > 0):
                    raise AttributeError("Provided `step` should not be against logic with respect to `start` and `end`!")
                elif (isinstance(self.start, int) and not self.end):
                    raise AttributeError("You should provide `end` with non-iterable `start`!")
                elif (not isinstance(self.end, int) or not isinstance(self.step, int)):
                    raise TypeError

            elif not isinstance(self.start, Iterable) and not isinstance(self.start, int):
                raise TypeError
        
        except (TypeError) as exc:
            print(f"MyNumberCollection supports only integers!")
            return None
        except AttributeError as exc:
            print(exc)
            return None
        except Exception as exc:
            print("Unknown exception has raised...")
            return None

        else:
            if isinstance(self.start, int):
                if self.start == self.end:
                    numbers.append(self.start)
                else:
                    for n in range(self.start, self.end + 1, self.step):
                        numbers.append(n)
                    if numbers[-1] != self.end:
                        numbers.append(self.end)
            else:
                for n in self.start:
                    numbers.append(n)

            return numbers

    def append(self, number: int) -> None:
        self.numbers.append(number)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__i < len(self.numbers):
            self.__i += 1
            return self.numbers[self.__i-1]
        self.__i = 0
        raise StopIteration
    
    def __str__(self):
        return f"{self.numbers}"
    
    def __add__(self, other):
        return self.numbers + other.numbers
    
    def __getitem__(self, index):
        try:
            return self.numbers[index] ** 2
        except IndexError:
            print(f"Index out of range. You can use from 0 till {len(self.numbers) - 1}")


if __name__ == "__main__":
    a = MyNumberCollection(1, 10, 4)
    b = MyNumberCollection(28, 1, -5)
    c = MyNumberCollection()
    print(a + b)
    print(a)
    print(b)
    print(c)
    print(a[2])

    for i in a:
        print(i)