### Task 4.4
'''Create hierarchy out of birds.
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.

Have a look at __mro__ method of your last class.'''

class Bird():

    def __init__(self, name):
        self.name = name

    def fly(self):
        pass

    def walk(self):
        print(f'{self.name} bird can walk')

    def __str__(self):
        return self.name


class FlyingBird(Bird):

    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        pass

    def walk(self):
        pass

    def eat(self):
        print(f'{self.name} eats mostly {self.ration}')

    def __str__(self):
        return f'{self.name} can walk and fly'


class NonFlyingBird(Bird):

    def __init__(self, name, ration):
        super().__init__(name)
        self.ration = ration

    def walk(self):
        pass

    def eat(self):
        print(f'{self.name} eats mostly {self.ration}')

    def swim(self):
        print(f'{self.name} bird can swim')

    def __str__(self):
        return self.name

class SuperBird(FlyingBird):

    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def walk(self):
        pass

    def eat(self):
        print(f'{self.name} eats {self.ration}')

    def swim(self):
        pass

    def fly(self):
        pass

    def __str__(self):
        return f'{self.name} bird can walk, swim and fly'


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

print(SuperBird.__mro__)