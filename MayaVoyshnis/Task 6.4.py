"""
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

Example:
```python
# >>> b = Bird("Any")
# >>> b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
# >>> p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
# >>> p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
# >>> str(c)
# "Canary can walk and fly"
# >>> c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
# >>> str(s)
# "Gull bird can walk, swim and fly"
# >>> s.eat()
"It eats fish"
```

Have a look at __mro__ method of your last class.

"""


class Bird:
    def __init__(self, name):
        self._name = name

    def fly(self):
        print(f'{self._name} can fly')

    def walk(self):
        print(f'{self._name} can walk')

    def __str__(self):
        activity = ''
        for el in reversed(dir(self)):
            if '_' in el: break
            activity += el + ', '
        return f'{self._name} can {activity}'


class FlyingBird(Bird):
    def __init__(self, name, ration='warms'):
        super(FlyingBird, self).__init__(name)
        self._ration = ration

    def eat(self):
        print(f'It is eat mostly {self._ration}')


class NonFlyingBird(Bird):
    def __init__(self, name, ration='fish'):
        super(NonFlyingBird, self).__init__(name)
        self._ration = ration

    def fly(self):
        raise AttributeError(f"'{self._name}' object has no attribute 'fly'")

    def eat(self):
        print(f'It is eat mostly {self._ration}')

    def swim(self):
        print(f'{self._name} can swim')


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super(SuperBird, self).__init__(name)

    def fly(self):
        return FlyingBird.fly(self)


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
