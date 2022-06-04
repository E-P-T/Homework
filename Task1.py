# Task 6.1


def type_validator(type_=int):
    """Argument type validator"""

    def decorator(func):
        def wrapper(self, value):
            if isinstance(value, type_) or value is None:
                func(self, value)
            else:
                raise TypeError('{} must be a {}'.format(value, type_))
        return wrapper
    return decorator


class Counter():
    """Counter class.

    Count from start to finish. If stop is not specified, counts to infinity.

    Attributes
    ----------
    start : int
        initial value
    stop : int
        finite value

    """

    def __init__(self, start=0, stop=None) -> None:
        """initializer for class Counter.

        Attributes
        ----------
        start : int
            initial value
        stop : int
            finite value

        """

        self.start = start
        self.stop = stop

    @property
    def start(self):
        return self._start

    @start.setter
    @type_validator()
    def start(self, value):
        self._start = value

    @property
    def stop(self):
        return self._stop

    @stop.setter
    @type_validator()
    def stop(self, value):
        if value is None or value > self.start:
            self._stop = value
        else:
            raise TypeError(
                f'{value} must be greater than {self.start}')

    def increment(self):
        """The function of incrementing one to a number."""

        if self.start != self.stop:
            self.start += 1
        else:
            raise Exception("Maximal value is reached.")

    def get(self):
        """Returns the current value of the monitored number."""

        return self.start


def main():
    """Main function."""

    print('\n{:*^30}'.format('Task 6.1'), end='\n\n')

    try:
        c = Counter(start='s', stop='42')
    except TypeError as e:
        print(e, end='\n\n')

    c = Counter(42)
    c.increment()
    print(c.get())

    print('-'*25)
    c = Counter()
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())

    print('-'*25)
    c = Counter(start=42, stop=43)
    c.increment()
    print(c.get())

    try:
        c.increment()
    except Exception as ex:
        print(ex)

    print(c.get())
