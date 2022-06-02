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

# Implement str() function call for each class.

# Example:
# ```python
# >>> b = Bird("Any")
# >>> b.walk()
# "Any bird can walk"

# >>> p = NonFlyingBird("Penguin", "fish")
# >>>  p.swim()
# "Penguin bird can swim"
# >>> p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
# >>> p.eat()
# "It eats mostly fish"

# >>> c = FlyingBird("Canary")
# >>> str(c)
# "Canary can walk and fly"
# >>> c.eat()
# "It eats mostly grains"

# >>> s = SuperBird("Gull")
# >>> str(s)
# "Gull bird can walk, swim and fly"
# >>> s.eat()
# "It eats fish"
# ```

# Have a look at __mro__ method of your last class.

class Bird:
    def __init__(self, name):
        self._name = name

    name = property(lambda self: self._name)

    def fly(self):
        print(f"{self.name} bird can fly")

    def walk(self):
        print(f"{self.name} bird can walk")

    def __str__(self):
        return f"{self.name} can walk and fly"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self._ration = ration

    def eat(self):
        print(f"It eats {self._ration}")

    def __str__(self):
        return f"{self.name} can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self._ration = ration

    # Deleted like
    def fly(self):
        print(f"AttributeError: '{self.name}' object has no attribute 'fly'")

    def eat(self):
        print(f"It eats mostly {self._ration}")

    def swim(self):
        print(f"{self.name} bird can swim")

    def __str__(self):
        return f"{self.name} can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


def main():
    """
    Entry point function.
    """
    b = Bird("Any")
    b.walk()

    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    p.fly()
    p.eat()

    c = FlyingBird("Canary")
    print(str(c))
    c.eat()

    s = SuperBird("Gull")
    print(str(s))
    s.eat()
    print(SuperBird.mro())


if __name__ == '__main__':
    main()
