#! /usr/bin/env python
# TODO: Implement a Counter class which optionally accepts the start value
# and the counter stop value. If the start value is not specified the counter
# should begin with 0. If the stop value is not specified it should be counting
# up infinitely. If the counter reaches the stop value, print "Maximal value
# is reached." Implement to methods: "increment" and "get"
# If you are familiar with Exception rising use it to display the "Maximal
# value is reached." message.


"""
task_1.py: implemented class Counter with required functionality. Also contains
some statements for testing this class.
"""


class Counter:
    """
    Counter: count values from start to stop. If stop doesn't specify it will
    count endlessly. If start doesn't specify it will count from 0. If it
    will reach stop it raise an exception StopIteration with informational msg.
    """
    def __init__(self, start=0, stop=float('inf')):
        self.current = start
        self.stop = stop

    def increment(self):
        if self.current < self.stop:
            self.current += 1
        else:
            raise StopIteration('Maximal value is reached.')

    def get(self):
        return self.current


if __name__ == '__main__':
    c = Counter(start=42)
    c.increment()
    print(c.get())

    c = Counter()
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())

    c = Counter(start=42, stop=43)
    # c.increment()
    print(c.get())

    c.increment()
    print(c.get())
