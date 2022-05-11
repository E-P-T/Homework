# Task 4.2
# Implement custom dictionary that will memorize 10 latest changed keys. Using method
# "get_history" return this keys.
#
# Example:
#
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()
#
# ["bar"]
# After your own implementation of the class have a look at collections.deque
# https://docs.python.org/3/library/collections.html#collections.deque

class MyDictionary:
    temp_list_history = []

    def __init__(self, dict):
        self.dictionary = {}
        self.dictionary = dict

    def set_value(self, key, value):
        self.dictionary[key] = value
        if len(self.temp_list_history) < 10:
            self.temp_list_history.append(key)
        else:
            del self.temp_list_history[0]
            self.temp_list_history.append(key)

    def get_history(self):
        print(f"added keys {self.temp_list_history}")


d = MyDictionary({"foo": 42})
d.set_value("bar", 43)
c = MyDictionary()
c.set_value("cat", 36)
d.get_history()
