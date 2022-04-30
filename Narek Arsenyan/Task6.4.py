class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(self.name + ' bird can fly')

    def walk(self):
        print(self.name + ' bird can walk')

    def str(self):
        print(self.name + ' can walk and fly')


class NonFlyingBird(Bird):
    def __init__(self, name, food='fish'):
        super().__init__(name)
        self.food = food

    def fly(self):
        raise AttributeError("'{0}' object has no attribute 'fly'".format(self.name))

    def swim(self):
        print(self.name + ' bird can swim')

    def eat(self):
        print(self.name + ' eats mostly ' + self.food)

    def str(self):
        print(self.name + ' can walk and swim')


class FlyingBird(Bird):
    def __init__(self, name, food='grains'):
        super().__init__(name)
        self.food = food

    def eat(self):
        print(self.name + ' eats mostly ' + self.food)


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def str(self):
        print(self.name + ' bird can walk, swim and fly')


b = Bird('Any')
p = NonFlyingBird('Penguin', 'fish')
f = FlyingBird('Canary')
s = SuperBird('Gull')
print(SuperBird.mro())
