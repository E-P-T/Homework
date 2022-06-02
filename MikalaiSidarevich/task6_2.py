# Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.

# Example:
# ```python
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()

# ["bar"]
# ```

from collections import deque


class HistoryDict:
    """Custom dictionary that memorize 10 latest changed keys."""

    def __init__(self, dct: dict, lmt: int = 10):
        """
        Initialize custom dictionary with `dct`, set limit of last changes with `lmt`.
        """
        self._dct = dct
        self._lmt = lmt
        self._mem = deque()

    def set_value(self, key, value):
        """
        Set a new `value` into the dictionary. Replace different values only.
        """
        if self._dct.get(key) != value:
            self._dct[key] = value
            # Pop too old key from queue
            if len(self._mem) == self._lmt:
                self._mem.popleft()
            self._mem.append(key)

    def get_history(self) -> deque:
        """
        Print and return last changed keys.
        """
        print(list(self._mem))
        return self._mem


def main():
    """
    Entry point function.
    """
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    d.get_history()
    d.set_value("foo", 42)
    for i in range(10):
        d.set_value(f"k{i:>02}", 0)
    d.get_history()


if __name__ == '__main__':
    main()
