'''
### Task 4.1
Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

* <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>
'''


class Counter():
    def __init__(self, start=0, stop=None):
        self.stop = stop
        self.counter = start

    def increment(self):
        if self.stop and self.counter >= self.stop:
            print("Maximal value is reached.")
        else:
            self.counter += 1

    def get(self):
        return self.counter

# for i in range(15):
#     print(c.get())
#     c.increment()

c = Counter(start=42)
c.increment()
print(c.get())

c = Counter()
c.increment()
print(c.get())

c.increment()
print(c.get())

c = Counter(start=42, stop=43)
c.increment()
print(c.get())

c.increment()
print(c.get())
