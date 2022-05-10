class HistoryDict:
    def __init__(self, dict):
        self.d = dict
        self.history = []
    def set_value(self, key, value):
        self.history.append(key)
        self.d.clear()
        self.d[key] = value
        if len(self.history) > 10:
            self.history.pop(0)


    def get_history(self):
        print(self.history)




h = HistoryDict({"foo": 42})
h.set_value("bar", 4)
h.get_history()
