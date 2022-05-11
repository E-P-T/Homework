# Task 6.1
# Implement a Counter class which optionally accepts the start value and the
# counter stop value. If the start value is not specified the counter should begin with
# 0. If the stop value is not specified it should be counting up infinitely. If the counter
# reaches the stop value, print "Maximal value is reached."
#
# Implement to methods: "increment" and "get"
#
# If you are familiar with Exception rising use it to display the "Maximal value is reached." message.
# Example:
#

class Counter:
    def __init__(self, start=0):
        self.start = start

    def get(self):
        print(self.start)

    def increment(self):
        self.start += 1


c = Counter(5)
c.get()
c.increment()
c.get()
# >>> c = Counter(start=42)
# >>> c.increment()
# >>> c.get()
# 43
#
# >>> c = Counter()
# >>> c.increment()
# >>> c.get()
# 1
# >>> c.increment()
# >>> c.get()
# 2
#
# >>> c = Counter(start=42, stop=43)
# >>> c.increment()
# >>> c.get()
# 43
# >>> c.increment()
# Maximal value is reached.
# >>> c.get()
# 43
