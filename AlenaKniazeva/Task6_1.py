"""Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."
"""

class Counter:
    def __init__(self, start = 0, stop = None):
        self.start = start
        self.stop = stop
    
    def increment(self):
        try:
            if self.start == self.stop:
                raise ValueError
            else:
                self.start += 1
        except ValueError:
            print("Maximal value is reached.")

    def get(self):
        print(self.start)