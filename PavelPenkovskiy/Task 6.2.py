# #### Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.
#
# Example:
# ```python
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()
#
# ["bar"]
#
# After your own implementation of the class have a look at collections.
# deque https://docs.python.org/3/library/collections.html#collections.deque

from collections import deque

class HistoryDict(dict):

    @staticmethod
    def set_value(key, value):
        with open('data/task_6.2_data.txt', mode='a') as f:
            f.write(str(key) + '\n')

    @staticmethod
    def get_history():
        with open('data/task_6.2_data.txt') as f:
            result = [x[:-1:] for x in list(deque(f, 10))]
            print(result)


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.set_value("lidbeerbar", 45)
d.get_history()


