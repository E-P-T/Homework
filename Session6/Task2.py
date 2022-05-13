"""
Implement custom dictionary that will memorize 10 latest changed keys. Using method "get_history" return this keys.
"""

class HistoryDict:
    lst = []
    def __init__(self, Dict):
        Dict = {}
        self.Dict = Dict


    def set_value(self, key, val):
        self.Dict = {key: val}
        self.lst.append(key)
        if len(self.lst) > 10:
            self.lst.pop(0)

    def get_history(self):

        return self.lst

d = HistoryDict({"mek":1})
d.set_value("erku",2)
d.set_value("ereq",3)
d.set_value("chors",4)
d.set_value("hing",5)
d.set_value("vec",6)
d.set_value("yot",7)
d.set_value("ut",8)
d.set_value("iny",9)
d.set_value("tas",10)
d.set_value("tt",11)


print(d.get_history())