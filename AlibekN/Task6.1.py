#Task 6.1
from cmath import inf

class Counter:
    def __init__(self, start = 0, stop = inf):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start != self.stop:
            self.start += 1
        else:
            print("Maximal value is reached.")
    
    def get(self):
        print( self.start ) 
        return self.start

obj = Counter(start=5,stop = 7)
obj.increment()
obj.increment()
obj.increment()
obj.get()