# Task 6.6
# A singleton is a class that allows only a single instance of itself to be created and gives access
# to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.
#
# Example:
#
# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True

class Sun:

    instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Sun, cls).__new__(cls)
        return cls.instance

p = Sun()
f = Sun()
print(p is f)