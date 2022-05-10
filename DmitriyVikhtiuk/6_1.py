class Counter:
    def __init__(self, stop=float('inf'), start=0):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start < self.stop:
            self.start += 1
        else:
            print("Max value is reached")

    def get(self):
        if self.start <= self.stop:
            print(self.start)
        else:
            print(self.stop)


c = Counter()
c.increment()
c.get()


