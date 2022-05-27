from collections import deque

class HistoryDict:
    _dictionary = {}
    _history_keys = []
    _history_deque_keys = deque(maxlen=10)
    def __init__(self, dictionary):
        self._dictionary = dictionary
    
    def set_value(self, key, value):
        self._dictionary[key] = value        
        self._history_keys.append(key)
        
        self._history_keys = self._history_keys[-10:]
        
    def set_value_deque(self, key, value):
        self._dictionary[key] = value        
        self._history_deque_keys.append(key)     
            
        
    def get_history(self):
        return self._history_keys
        
    def get_history_deque(self):
        return list(self._history_deque_keys)
        

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.set_value("fera", 44)
d.set_value("roba", 45)
d.set_value("zero", 46)
d.set_value("fora", 47)
d.set_value("laba", 48)
d.set_value("true", 49)
d.set_value("false", 50)
d.set_value("laky", 51)
d.set_value("olaf", 52)
d.set_value("buter", 53)
d.set_value("orbit", 54)
print(
    d.get_history()
)

d.set_value_deque("bar", 43)
d.set_value_deque("fera", 44)
d.set_value_deque("roba", 45)
d.set_value_deque("zero", 46)
d.set_value_deque("fora", 47)
d.set_value_deque("laba", 48)
d.set_value_deque("true", 49)
d.set_value_deque("false", 50)
d.set_value_deque("laky", 51)
d.set_value_deque("olaf", 52)
d.set_value_deque("buter", 53)
d.set_value_deque("orbit", 54)
print(
    d.get_history_deque()
)
