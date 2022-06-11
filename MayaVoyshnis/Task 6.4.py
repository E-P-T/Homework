class Bird:
    def __init__(self, name):
        self._name = name

    def fly(self):
        print(f'{self._name} can fly')

    def walk(self):
        print(f'{self._name} can walk')

    def __str__(self):
        return f'{self._name} can  fly, walk.'


class FlyingBird(Bird):
    def __init__(self, name, ration='warms'):
        super(FlyingBird, self).__init__(name)
        self._ration = ration

    def eat(self):
        print(f'It is eat mostly {self._ration}')

    def __str__(self):
        return f'{self._name} can eat, fly, walk.'


class NonFlyingBird(Bird):
    def __init__(self, name, ration='fish'):
        super(NonFlyingBird, self).__init__(name)
        self._ration = ration

    def eat(self):
        print(f'It is eat mostly {self._ration}')

    def swim(self):
        print(f'{self._name} can swim')

    def fly(self):
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute 'fly'")

    def __str__(self):
        return f'{self._name} can eat, swim, walk.'


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super(SuperBird, self).__init__(name)

    def fly(self):
        print(f'{self._name} can fly')

    def __str__(self):
        return f'{self._name} can eat, fly, swim, walk.'


if __name__ == '__main__':
    b = Bird("Any")
    b.walk()
    print(b)

    c = FlyingBird('Sokol')
    print(c)
    d = NonFlyingBird('Ping')
    c.fly()
    c.eat()
    d.eat()
    print(d)

    super = SuperBird('Dragon')
    super.walk()
    super.eat()
    super.swim()
    super.fly()
    print(super)
