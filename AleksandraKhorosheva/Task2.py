#### Task 4.2
'''Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.


Example:
```python
d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()

["bar"]
```
<em>After your own implementation of the class have a look at collections.deque https://docs.python.org/3/library/collections.html#collections.deque </em>
'''


class HistoryDict(object):

    def __init__(self, dict, count=10):
        self.dict = dict
        self.count = count
        self.history = []

    def set_value(self, key, value):
        self.dict[key] = value
        self.history.append(key)
        self.history = self.history[-self.count:]

    def get_history(self):
        return self.history


d = HistoryDict({"foo": 42})
d.set_value("a", 43)
d.set_value("b", 43)
d.set_value("c", 43)
d.set_value("d", 43)
print(d.get_history())
