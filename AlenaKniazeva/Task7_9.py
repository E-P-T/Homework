"""
Implement an iterator class EvenRange, which accepts start and end of the interval as
an init arguments and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.  
"""

class EvenRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.pointer = start if start % 2 == 0 else start+1

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer < self.stop:
            res = self.pointer
            self.pointer += 2
        else:
            print("Out of numbers!")
            raise StopIteration
        return res

if __name__ == "__main__":
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)