#### Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.
# Example:
# ```python
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()
# ["bar"]
# ```
# <em>After your own implementation of the class have a look at collections.deque
# https://docs.python.org/3/library/collections.html#collections.deque </em>

class HistoryDict:
    def __init__(self, k_v):
        self.dictionary = k_v
        self.ret = []

    def set_value(self, key, val):
        self.dictionary[key] = val
        if len(self.ret) == 10:
            del self.ret[0]
        self.ret.append(key)

    def get_history(self):
        print(self.ret)


d = HistoryDict({"foo": 42})
d.set_value("ba", 43)
d.set_value("gur", 982)
d.get_history()
