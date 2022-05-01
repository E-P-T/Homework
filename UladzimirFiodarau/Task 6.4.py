# Task 4.4
# Create hierarchy out of birds. Implement 4 classes:
# class Bird with an attribute name and methods fly and walk.

# class FlyingBird with attributes name, ration, and with the same methods. ration must have default value.
# Implement the method eat which will describe its typical ration.

# class NonFlyingBird with same characteristics but which obviously without attribute fly.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.

# class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
# Implement str() function call for each class.
#
class Bird(object):
    """
    class Bird with an attribute name and methods fly and walk.
    """

    def __init__(self, name):
        self._name = name
        self._walk = f"{self._name} bird can walk"

    def __str__(self):
        return f'{self._name} bird can walk'

    def fly(self):
        try:
            return self._fly
        except AttributeError:
            return f"AttributeError: {self._name} object has no attribute 'fly'"

    def walk(self):
        try:
            return self._walk
        except AttributeError:
            return f"AttributeError: {self._name} object has no attribute 'walk'"


class FlyingBird(Bird):
    """
    class FlyingBird with attributes name, ration, and with the same methods. ration has default value.
    Method eat describes its typical ration.
    """

    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self._ration = ration
        self._fly = f"{self._name} bird can fly"

    def __str__(self):
        return f'{self._name} bird can walk and fly'

    def eat(self):
        return f"It eats mostly {self._ration}"


class NonFlyingBird(Bird):
    """
    class NonFlyingBird which objects have attribute swim but no attribute fly.
    Add same "eat" method but with other implementation regarding the swimming bird tastes.
    """

    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self._ration = ration
        self._swim = f"{self._name} bird can swim"

    def __str__(self):
        return f'{self._name} bird can walk and swim'

    def swim(self):
        try:
            return self._swim
        except AttributeError:
            return f"AttributeError: {self._name} object has no attribute 'swim'"

    def eat(self):
        return f"It eats mostly {self._ration}"


class SuperBird(NonFlyingBird, FlyingBird, Bird):
    """
    class SuperBird objects of which can walk, fly, swim and eat.
    """

    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self._ration = ration

    def __str__(self):
        return f'{self._name} bird can walk, swim and fly'


b = Bird("Any")
print(b.walk())
# "Any bird can walk"
print(b.fly())
# AttributeError: 'Any' object has no attribute 'fly'

p = NonFlyingBird("Penguin", "fish")
print(p.swim())
# "Penguin bird can swim"
print(p.fly())
# AttributeError: 'Penguin' object has no attribute 'fly'
print(p.eat())
# "It eats mostly fish"

c = FlyingBird("Canary")
print(str(c))
# "Canary can walk and fly"
print(c.eat())
# "It eats mostly grains"

s = SuperBird("Gull")
print(str(s))
# "Gull bird can walk, swim and fly"
print(s.eat())
print(s.fly())
# "It eats fish"

print(SuperBird.__mro__)