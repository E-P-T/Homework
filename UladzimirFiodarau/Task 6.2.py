# Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys. Using method "get_history" return this keys.


class HistoryDict(object):
    """
    Implements custom dictionary that memorizes a limit of latest changed keys (by default 10)
    """
    def __init__(self, dictionary=None, limit=10):
        if dictionary is None:
            dictionary = {}
        self._dictionary = dictionary
        self._limit = limit

    def set_value(self, key, value):
        """
        sets new dict with given key:value pair
        :param key: dictionary key
        :param value: dictionary value
        :return: None
        """
        self._dictionary = {key: value}


    def dequeue(self):
        """
        removes the first entry pair key:value of self.dictionary
        :return: a pair: key:value
        """
        self._dictionary.pop(self.get_history()[0])


    def add_value(self, key, value):
        """
        adds a pair key: value to self.dictionary
        :param key: dictionary key
        :param value: dictionary value
        :return: None
        """
        self._dictionary[key] = value
        while len(self._dictionary) > self._limit:
            self.dequeue()

    def get_history(self):
        """
        Returns a list of dictionary keys in order of entry
        :return: list of dictionary keys
        """
        return list(self._dictionary.keys())


d = HistoryDict({"foo": 42})

d.add_value("bar", 43)
d.add_value("far", 43)
d.add_value("aar", 43)
d.add_value("var", 43)
d.add_value("war", 43)
d.add_value("ear", 43)
d.add_value("rar", 43)
d.add_value("tar", 43)
d.add_value("yar", 43)
d.add_value("uar", 43)

print(d.get_history())

k = HistoryDict({"foo": 42})
k.add_value("var", 43)
k.add_value("war", 43)
k.add_value("ear", 43)
k.set_value("bar", 43)
print(k.get_history())
