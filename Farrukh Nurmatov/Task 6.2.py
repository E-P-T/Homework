"""Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys."""


class HistoryDict:
    def __init__(self, dicto):
        self.dicto = dicto
        self.history_keys = []

    def set_value(self, key, value):
        self.dicto.clear()
        self.dicto[key] = value
        if len(self.history_keys) >= 10:
            self.history_keys.pop(0)
            self.history_keys.append(key)
        else:
            self.history_keys.append(key)

    def get_history(self):
        return self.history_keys


if __name__ == '__main__':
    a = HistoryDict({"foo": 42})
    a.set_value("bar", 43)
    print(a.get_history())
    a.set_value("off", 55)
    print(a.get_history())
    a.set_value("set", 58)
    a.set_value("ket", 596)
    a.set_value("get", 65)
    a.set_value("kst", 142)
    a.set_value("asd", 45)
    a.set_value("fas", 96)
    a.set_value("gdf", 45)
    a.set_value("ghf", 44)
    print(a.get_history())
    a.set_value("dfd", 58)
    print(a.get_history())
