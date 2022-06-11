#! /usr/bin/env python
# TODO: Create hierarchy out of birds. Implement 4 classes:
# 1) class Bird with an attribute name and methods fly and walk.
# 2) class FlyingBird with attributes name, ration, and with the same methods.
# ration must have default value. Implement the method eat which will describe
# its typical ration.
# 3) class NonFlyingBird with same characteristics but which obviously without
# attribute fly. Add same "eat" method but with other implementation regarding
# the swimming bird tastes.
# 4) class SuperBird which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.
# 5) Implement str() function call for each class.


"""
task_4.py: implemented hierarchy out of birds. Contains 4 classes and some
test statements for them.
"""


class Bird:
    """
    Bird: base class for FlyingBird, NonFlyingBird, SuperBird.
    Determine walk method and __str__ method.
    """
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name} bird can walk')

    def __str__(self):
        return f'{self.name} can walk'


class FlyingBird(Bird):
    """
    FlyingBird: derived class which determine fly, eat and __str__ methods.
    """
    def __init__(self, name, ration='worm'):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        print(f'{self.name} bird can fly')

    def eat(self):
        print(f'{self.name} bird eats mostly {self.ration}s')

    def __str__(self):
        return f'{self.name} can walk and fly'


class NonFlyingBird(Bird):
    """
    NonFlyingBird: derived class which determine swim, eat and __str__ methods.
    """
    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        print(f'{self.name} bird can swim')

    def eat(self):
        print(f'{self.name} bird eats mostly {self.ration}s')

    def __str__(self):
        return f'{self.name} can walk and swim'


class SuperBird(FlyingBird, NonFlyingBird):
    """
    SuperBird: derived class which determine eat and __str__ methods.
    """
    def __init__(self, name, ration='human'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f'{self.name} bird eats mostly {self.ration}s')

    def __str__(self):
        return f'{self.name} can walk and swim and fly'


if __name__ == '__main__':
    b = Bird('Any')
    print(str(b))
    b.walk()

    p = NonFlyingBird('Penguin', 'fish')
    print(str(p))
    p.swim()
    # p.fly()
    p.eat()

    c = FlyingBird('Canary', 'worm')
    print(str(c))
    c.fly()
    # c.swim()
    c.eat()

    s = SuperBird('Gull', 'human')
    print(str(s))
    s.fly()
    s.swim()
    s.eat()
