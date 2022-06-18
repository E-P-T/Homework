
class HistoryDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._history = []

    def __setitem__(self, key, value):
        self._update_history(key)
        super().__setitem__(key, value)

    def _update_history(self, key):
        self._history.append(key)
        if len(self._history) == 11:
            self._history.pop(0)

    def get_history(self):
        return self._history


if __name__ == '__main__':
    d = HistoryDict({'foo': 42})
    d['bar'] = 43
    print(d.get_history())
    d['baz'] = 45
    print(d.get_history())
    d['bay'] = 41
    print(d.get_history())
