class Counter:
    def __init__(self, start=0, stop=False):
        self.current = start
        self.stop = stop

    def increment(self):
        if not(self.stop) or self.current < self.stop:
            self.current += 1
        else:
            print('Maximal value is reached.')

    def get(self):
        print(self.current)

