"""
Implement a Counter class which optionally accepts the start value and the counter stop value. If the start value
is not specified the counter should begin with 0. If the stop value is not specified it should be
counting up infinitely. If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"
"""
class Counter:

    def __init__(self, start = 0, stop = float("inf")):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.stop == self.start:
            print("Maximal value is reached.")
        else:
            self.start += 1

    def get(self):
        return self.start

c = Counter(start=42, stop=43)
c.increment()
print(c.get())