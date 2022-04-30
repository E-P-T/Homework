class Counter:
    def __init__(self, start = 5, stop = float("inf")):
        self.start = start
        self.stop = stop
    def increment(self):
        if self.stop != self.start:
            self.start += 1
        else:
            print("Maximal value is reached.")
    def get(self):
        print(self.start)
p1 = Counter(start=22, stop=23)
p1.get()
p1.increment()
p1.get()
