# Task 7.7
# Implement your custom collection called MyNumberCollection. It should be able to contain only numbers.
# It should NOT inherit any other collections.
# If user tries to add a string or any non numerical object there, exception TypeError should be raised.
# Method init sholud be able to take either start,end,step arguments, where start - first number of collection,
# end - last number of collection or some ordered iterable collection (see the example). Implement following functionality:

# appending new element to the end of collection
# concatenating collections together using +
# when element is addressed by index(using []), user should get square of the addressed element.
# when iterated using cycle for, elements should be given normally
# user should be able to print whole collection as if it was list.

class MyNumberCollection:
    """Custom collection class, can contains numbers only."""

    def __init__(self, *args):
        """
        Initialize internal collection with [start, end] range or input collection.
        """
        self.store = []
        # Input collection
        if len(args) == 1:
            for i in args[0]:
                if not (isinstance(i, int) or isinstance(i, float)):
                    raise TypeError("MyNumberCollection supports only numbers!")
            self.store.extend(args[0])
        # Range
        elif len(args) == 3:
            for i in range(args[0], args[1], args[2]):
                self.store.append(i)
            self.store.append(args[1])

    def append(self, value):
        """
        Append `value` to the end of collection.
        """
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError(f"'{value}' - object is not a number!")
        self.store.append(value)

    def __add__(self, col):
        return self.store + col.store

    def __getitem__(self, i):
        return self.store[i]**2

    def __str__(self) -> str:
        return str(self.store)

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if self.pos < len(self.store):
            value = self.store[self.pos]
            self.pos += 1
            return value
        else:
            raise StopIteration


def main():
    """
    Entry point function.
    """
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)

    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)

    try:
        col3 = MyNumberCollection((1, 2, 3, "4", 5))
    except TypeError as e:
        print(f"TypeError: {e}")

    col1.append(7)
    print(col1)

    try:
        col2.append("string")
    except TypeError as e:
        print(f"TypeError: {e}")

    print(col1 + col2)
    print(col1)
    print(col2)
    print(col2[4])
    for item in col1:
        print(item, end=' ')
    print()


if __name__ == '__main__':
    main()
