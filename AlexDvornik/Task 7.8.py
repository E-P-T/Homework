"""
Task 7.8
Implement your custom iterator class called MySquareIterator
which gives squares of elements of collection it iterates through.
"""


class MySquareIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.last_element = len(numbers) - 1
        self.n = 0

    def __iter__(self):
        return self

    def get_element(self, n):
        return self.numbers[n]

    def __next__(self):
        if self.n <= self.last_element:
            number = self.get_element(self.n)**2
        else:
            raise StopIteration
        self.n += 1
        return number


lst = [1, 2, 3, 4, 5]
iterator = MySquareIterator(lst)
for it in iterator:
    print(it)
