class HistoryDict:
    _latest_changed_keys = list() # the list of keys

    def __init__(self, initial_dict: dict):
        self.dictionary = initial_dict
    
    def set_value(self, key, value):
        self.dictionary[key] = value
        if len(self._latest_changed_keys) == 10:
            self._latest_changed_keys.pop()
        self._latest_changed_keys.insert(0, key)

    def get_history(self):
        return self._latest_changed_keys


from collections import deque
class HistoryDictDeque:
    _latest_changed_keys = deque(maxlen=10)

    def __init__(self, initial_dict: dict):
        self.dictionary = initial_dict
    
    def set_value(self, key, value):
        self.dictionary[key] = value
        self._latest_changed_keys.appendleft(key)

    def get_history(self):
        return self._latest_changed_keys
