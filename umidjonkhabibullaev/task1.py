class Counter:
    def __init__(self, start = 0, stop = float('inf')):
        self.start = start
        self.stop = stop
    
    def increment(self):
        self.start += 1
        if self.start > self.stop:
            print("Maximal value is reached.")
            self.start -= 1
    
    def get(self):
        return self.start
