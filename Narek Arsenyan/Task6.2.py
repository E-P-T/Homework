import ast


class HistoryDict:
    a = []
    def __init__(self, dict):
        self.dict = dict
    def setValue(self, key, value):
        self.a.append(key)
        self.dict.clear()
        self.dict[key] = value
        if len(self.a) > 10:
            self.a.pop(0)
    def printHistory(self):
        print(self.a)
p1 = HistoryDict({"beee": 1243})
p1.setValue("1", 123)
p1.setValue("2", 12443)
p1.setValue("33", 123)
p1.setValue("4", 12443)
p1.setValue("5", 123)
p1.setValue("6", 1244444443)
p1.setValue("7", 123)
p1.setValue("8", 124666666643)
p1.setValue("9", 123)
p1.setValue("10", 1266666443)
p1.setValue("11", 123)
p1.setValue("12", 12466643)
p1.setValue("13", 123)
p1.setValue("14", 12466643)
p1.printHistory()
