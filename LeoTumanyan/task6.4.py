# ### Task 6.4
# Create hierarchy out of birds. 
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value. 
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.

# Implement str() function call for each class.

class Bird:
    def __init__(self, name):
        self._name = name

    def fly(self):
        print(f"{self._name} bird can fly.")

    def walk(self):
        print(f"{self._name} bird can walk.")

    def __str__(self):
        return "{self.name} bird can walk and fly."


class FlyingBird(Bird):
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"{self._name} eats mostly {self.ration}.")


class NonFlyingBird(Bird):
    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        print(f"{self._name} bird can swim.")

    def fly(self):
        raise AttributeError(f"'{self._name}' object has no attribute 'fly'")

    def eat(self):
        print(f"{self._name} eats mostly {self.ration}.")

    def __str__(self):
        return f"{self._name} bird can walk and swim."


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        super(FlyingBird, self).fly()

    def __str__(self):
        return f"{self._name} bird can walk, swim and fly."


b = Bird("Any")
b.walk()
p = NonFlyingBird("Penguin", "fish")
p.swim()
try:
    p.fly()
except AttributeError as ae:
    print('AttributerError:', ae)
p.eat()
c = FlyingBird("Canary")
str(c)
c.eat()
s = SuperBird("Gull")
# Have a look at __mro__ method of your last class.
print(SuperBird.__mro__)
s.eat()
print(s)

