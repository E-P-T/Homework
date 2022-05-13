"""
Task 6.4
Create hierarchy out of birds.
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.
"""


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'{self.name} can fly')

    def walk(self):
        print(f'{self.name} can walk')

    def swim(self):
        print(f'{self.name} can swim')

    def __str__(self):
        return f'The {self.name} can walk'


class FlyingBird(Bird):
    def __init__(self, name, ration='mosquito'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f'It eats mostly {self.ration}')

    def __str__(self):
        return f'The {self.name} can walk, fly and maybe swim'


class NonFlyingBird(Bird):
    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        raise AttributeError(f"{self.name} object has no attribute 'fly'")

    def eat(self):
        print(f'It eats mostly {self.ration}')

    def __str__(self):
        return f'The {self.name} can walk and maybe swim'


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration='any'):
        FlyingBird.__init__(self, name=name, ration=ration)
        NonFlyingBird.__init__(self, name=name, ration=ration)

    def __str__(self):
        return f'The {self.name} can walk, fly, swim and eat'

    def fly(self):
        print(f'{self.name} can fly')


b = Bird('Bird')
print(str(b))
flying_bird = FlyingBird('Parrot', ration='grains')
flying_bird.eat()
flying_bird.walk()
print(str(flying_bird))
non_flying_bird = NonFlyingBird('Penguin', ration='something')
non_flying_bird.eat()
super_bird = SuperBird(name="Angry Bird", ration='stuff')
super_bird.eat()
super_bird.fly()
print(str(super_bird))
