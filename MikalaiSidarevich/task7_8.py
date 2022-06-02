# Task 7.8
# Implement your custom iterator class called MySquareIterator
# which gives squares of elements of collection it iterates through.

class MySquareIterator:
    """Iterator class which gives squares of elements of collection it iterates through."""

    def __init__(self, col):
        """
        Initialize internal collection with `col`.
        """
        self.store = col

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if self.pos < len(self.store):
            value = self.store[self.pos]**2
            self.pos += 1
            return value
        else:
            raise StopIteration


def main():
    """
    Entry point function.
    """
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)


if __name__ == '__main__':
    main()
