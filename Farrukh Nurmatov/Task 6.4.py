"""Create hierarchy out of birds.
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class."""


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} bird can fly")

    def walk(self):
        print(f"{self.name} bird can walk")

    def __str__(self):
        return f"{self.name} bird can fly and walk"


class FlyingBird(Bird):
    ration = "grains"

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f'It eats mostly {self.ration}')


class NonFlyingBird:
    ration = "fish"

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} bird can walk")

    def swim(self):
        print(f"{self.name} bird can swim")

    def eat(self):
        print(f"It eats mostly {self.ration}")

    def __str__(self):
        return f"{self.name} bird can swim and walk"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} bird can walk, swim and walk"


if __name__ == '__main__':
    b = Bird("Any")
    b.fly()
    b.walk()
    print(b)
    c = FlyingBird("Canary")
    c.fly()
    c.walk()
    c.eat()
    print(c)
    p = NonFlyingBird("Penguin")
    p.swim()
    p.walk()
    print(p)
    s = SuperBird("Gull")
    s.swim()
    s.walk()
    s.fly()
    s.eat()
    print(s)
    print(SuperBird.mro())

