# Task 6.1
# Implement a Counter class which optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."

# Implement to methods: "increment" and "get"

# * If you are familiar with Exception rising use it to display the "Maximal value is reached." message.

# Example:
# ```python
# >>> c = Counter(start=42)
# >>> c.increment()
# >>> c.get()
# 43

# >>> c = Counter()
# >>> c.increment()
# >>> c.get()
# 1
# >>> c.increment()
# >>> c.get()
# 2

# >>> c = Counter(start=42, stop=43)
# >>> c.increment()
# >>> c.get()
# 43
# >>> c.increment()
# Maximal value is reached.
# >>> c.get()
# 43
# ```

class Counter:
    """Custom counter class. Can count from start to stop or infinitely when stop is not specified."""

    def __init__(self, start: int = 0, stop: int = -1):
        """
        Initialize the counter.
        `start` & `stop` are optional, if `stop` is not specified the counter runs infinitely.
        """
        self._counter = start
        self._stop = stop

    def increment(self):
        """
        Increment counter by 1. Raise ValueError if stop is reached.
        """
        if self._counter != self._stop:
            self._counter += 1
        else:
            raise ValueError("Maximal value is reached.")

    def get(self):
        """
        Print current counter value.
        """
        print(self._counter)


def main():
    """
    Entry point function.
    """
    c = Counter(start=42)
    try:
        c.increment()
    except ValueError as e:
        print(e)
    c.get()

    c = Counter()
    try:
        c.increment()
    except ValueError as e:
        print(e)
    c.get()

    try:
        c.increment()
    except ValueError as e:
        print(e)
    c.get()

    c = Counter(start=42, stop=43)
    try:
        c.increment()
    except ValueError as e:
        print(e)
    c.get()

    try:
        c.increment()
    except ValueError as e:
        print(e)
    c.get()


if __name__ == '__main__':
    main()
