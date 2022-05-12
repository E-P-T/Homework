"""
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.
"""

class HistoryDict:
    def __init__(self, dict):
        self.dict = dict
        self.last_key = []
    
    def set_value(self,dkey,dval):
        self.dict[dkey] = dval
        if len(self.last_key)==10:
            del self.last_key[0]
        self.last_key.append(dkey)

    def get_history(self):
        print(self.last_key)