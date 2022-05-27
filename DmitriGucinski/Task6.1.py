class Counter:
    _counter = 0
    _stop = 0
    def __init__(self, start=0, stop=0):
        self._counter = start
        self._stop = stop
        
    def increment(self):
        if self._stop == 0 or self._counter < self._stop:
            self._counter += 1
        else:
            raise CounterIncrementError("Maximal value is reached.")
        
    def get(self):    
        return self._counter


class CounterIncrementError(Exception):
    ''' Log error with logger '''
    pass


c = Counter(start=42)
c.increment()
print(c.get())

for i in range(100):
    c.increment()
    print(c.get())
