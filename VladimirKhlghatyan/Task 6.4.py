# Task 6.4
# Create hierarchy out of birds.
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.
#
# Implement str() function call for each class.
#
# Example:
# ```python
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
# ```
#
# Have a look at __mro__ method of your last class.


class Bird:

    def __init__(self, name):
        self.name = name
        self._fly = '{} bird can fly'.format(self.name)
        self._walk = '{} bird can walk'.format(self.name)

    def fly(self):
        print(self._fly)

    def walk(self):
        print(self._walk)

    def __str__(self):
        return '{} bird can walk and fly'.format(self.name)


class FlyingBird(Bird):

    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print('It eats mostly {}'.format(self.ration))


class NonFlyingBird(Bird):

    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration
        self._swim = '{} bird can swim'.format(self.name)

    def fly(self):
        print("AttributeError: {} object has no attribute 'fly'".format(self.name))

    def swim(self):
        print(self._swim)

    def eat(self):
        print('It eats mostly {}'.format(self.ration))

    def __str__(self):
        return '{} bird can walk and swim'.format(self.name)


class SuperBird(NonFlyingBird, FlyingBird, Bird):

    def __init__(self, name, ration='any food'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print('It eats mostly {}'.format(self.ration))

    def fly(self):
        print(self._fly)

    def __str__(self):
        return '{} bird can walk, swim and fly'.format(self.name)
