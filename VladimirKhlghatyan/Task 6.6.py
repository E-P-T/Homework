# Task 6.6
#
# A singleton is a class that allows only a single instance of itself to be created and gives access
# to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.
#
# Example:
#
# ```python
# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True
# ```

class Singleton:

    def __init__(self, name):
        self.name = name

    def inst(self):
        pass


@Singleton
class Sun:
    def __init__(self):
        pass
