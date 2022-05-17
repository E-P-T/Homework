"""### Task 4.1
Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement two methods: "increment" and "get"

* <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>"""
import math


class Counter:

    def __init__(self, start=0, stop=math.inf):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start < self.stop:
            self.start += 1
        else:
            print("Maximal value is reached.")

    def get(self):
        print(self.start)


if __name__ == '__main__':
    a = Counter(42, 45)
    a.increment()
    a.get()
    a.increment()
    a.get()
    a.increment()
    a.get()
    a.increment()

    c = Counter(42)
    c.increment()
    c.get()
    c.increment()
    c.get()

