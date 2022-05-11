# Task 6.4
# Create hierarchy out of birds. Implement 4 classes:
#
# class Bird with an attribute name and methods fly and walk.
# class FlyingBird with attributes name, ration, and with the same methods.
# ration must have default value. Implement the method eat which will describe
# its typical ration.
# class NonFlyingBird with same characteristics but which obviously
# without attribute fly. Add same "eat" method but with other implementation
# regarding the swimming bird tastes.
# class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
# Implement str() function call for each class.
#
# Example:
#
# >>> b = Bird("Any")
# >>> b.walk()
# "Any bird can walk"
#
# p = NonFlyingBird("Penguin", "fish")
# >> p.swim()
# "Penguin bird can swim"
# >>> p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
# >>> p.eat()
# "It eats mostly fish"
#
# c = FlyingBird("Canary")
# >>> str(c)
# "Canary can walk and fly"
# >>> c.eat()
# "It eats mostly grains"
#
# s = SuperBird("Gull")
# >>> str(s)
# "Gull bird can walk, swim and fly"
# >>> s.eat()
# "It eats fish"
# Have a look at mro method of your last class.


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'{self.name} can fly')

    def walk(self):
        print(f'{self.name} can walk')


class FlyingBird(Bird):
    def __init__(self, name, ration='mostly grains'):
        self.name = name
        self.ration = ration

    def eat(self):
        print(f'{self.name} eats {self.ration}')


class NonFlyingBird(Bird):
    def __init__(self, name, ration="mostly fish"):
        self.name = name
        self.ration = ration

    def eat(self):
        print(f'{self.name} eats {self.ration}')


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f'{self.name} can swim')


print(SuperBird.mro())
