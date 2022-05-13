"""
A singleton is a class that allows only a single instance of itself to be created and gives access to
that created instance. Implement singleton logic inside your custom class using a method to initialize class instance.
"""

class singleton:
    def __init__(self, nm):
        self.nm = nm

    def inst(self):
        pass

@singleton
class Sun:
    def __init__(self):
        pass

p = Sun.inst()
f = Sun.inst()
print(p is f)