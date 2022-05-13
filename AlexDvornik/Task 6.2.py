"""
Task 6.2
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.

Example:
d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()
["bar"]
"""


class HistoryDict:
    def __init__(self, dct):
        self.__dct = dct
        self.__storage = []

    def set_value(self, key: str, value: int):
        self.__dct[key] = value
        self.__storage.append(key)

    def get_history(self):
        print(self.__storage[-10:])


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.set_value("amogus", 45)
d.set_value("bar", 43)
d.set_value("amogus", 45)
d.set_value("amogus", 45)
d.get_history()

