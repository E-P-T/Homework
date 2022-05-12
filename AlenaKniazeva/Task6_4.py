"""
Create hierarchy out of birds. 
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` 
must have default value. 
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
"""

class Bird:
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        print("{} bird can fly.".format(self.name))

    def walk(self):
        print("{} bird can walk.".format(self.name))

    def __str__(self):
        return "{} bird can walk and fly.".format(self.name)

class FlyingBird(Bird):
    def __init__(self, name, ration = 'grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print("{} eats mostly {}.".format(self.name, self.ration))

class NonFlyingBird(Bird):
    def __init__(self, name, ration = 'fish'):
        super().__init__(name)
        self.ration = ration
    
    def swim(self):
        print("{} bird can swim.".format(self.name))

    def fly(self):
        raise AttributeError ("'{}' object has no attribute 'fly'".format(self.name))
    
    def eat(self):
        print("{} eats mostly {}.".format(self.name, self.ration))

    def __str__(self):
        return "{} bird can walk and swim.".format(self.name)

class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        super(FlyingBird,self).fly()

    def __str__(self):
        return "{} bird can walk, swim and fly.".format(self.name)