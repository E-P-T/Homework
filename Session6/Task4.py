"""
Create hierarchy out of birds. Implement 4 classes:

class Bird with an attribute name and methods fly and walk.
class FlyingBird with attributes name, ration, and with the same methods. ration must have default value.
Implement the method eat which will describe its typical ration.
class NonFlyingBird with same characteristics but which obviously without attribute fly.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
Implement str() function call for each class.
"""

class Bird:
    """class Bird with an attribute name and methods fly and walk."""
    def __init__(self, name):
        self.name = name

    def fly(self):
        return (self.name + ' bird can fly')
    def walk(self):
        return (self.name + ' bird can walk')

class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def swim(self):
        return self.name + " bird can swim"

class SuperBird(NonFlyingBird,FlyingBird,Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration



