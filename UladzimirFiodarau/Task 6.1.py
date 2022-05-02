# Task 6.1
# Implement a Counter class which optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0. If the stop value is not specified it should be
# counting up infinitely. If the counter reaches the stop value, print "Maximal value is reached."
# Implement to methods: "increment" and "get"
# If you are familiar with Exception rising use it to display the "Maximal value is reached." message.


class Counter(object):
    """
    Counter class which optionally accepts the start value and the counter stop value.
    If the start value is not specified the counter begins with 0. If the stop value is not specified it will be
    counting up infinitely. If the counter reaches the stop value, raises "Maximal value is reached."
    """
    def __init__(self, start: int = 0, stop: int = -1):
        self._count = start
        self._stop = stop

    def increment(self):
        """
        increments counter's attribute count by one if it is lower than stop value
        :return: None
        """
        if self._stop != self._count:
            self._count += 1
        else:
            raise Exception("Maximal value is reached.")

    def get(self):
        """
        returns current counters count value
        :return:
        """
        return self._count


# c = Counter(start=42)
# c.increment()
# print(c.get())
# 43
#
# c = Counter()
# c.increment()
# print(c.get())
# # 1
# c.increment()
# print(c.get())
# # 2
#
# c = Counter(start=42, stop=43)
# c.increment()
# print(c.get())
# # 43
# c.increment()
# # Maximal value is reached.
# print(c.get())
# # 43
