#Task6.2.py

class HistoryDict:
    def __init__(self, list={}):
        self.list = list

    def set_value(self, key, value):
        self.list.update({key: value})

    def get_history(self):
       keys = list(self.list.keys())
       keys.reverse()
       for i in keys[:9]:
           print(i)
    def print(self):
        print(self.list)


obj = HistoryDict({"foo": 42})
obj.set_value("bar", 13)
obj.set_value("mat", 17)
obj.get_history()
#obj.print()