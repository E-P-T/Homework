# Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.
#
# Example:
# ```python
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()
# ["bar"]

# ```
# After your own implementation of the class have a look at collections.deque
# https://docs.python.org/3/library/collections.html#collections.deque


class HistoryDict:
    last10 = list()

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def set_value(self, key, value):
        self.dictionary[key] = value
        if key not in self.last10:
            self.last10.append(key)
        self.last10 = self.last10[-10:]

    def get_history(self):
        print(self.last10)
