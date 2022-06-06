# Task 6.4

class FlyMixin():
    """Flying bird mixin class."""

    def fly(self):
        """The bird can fly

        Returns:
            str: a flying bird can do something
        """
        return f'{self._name} can fly'


class EatMixin():
    """Mixin class for birds that can eat."""

    def eat(self):
        """The bird can eat

        Returns:
            str: a eating bird can do something
        """
        return f'It eats mostly {self._ration}'


class SwimMixin():
    """Mixin class for birds that can swim."""

    def swim(self):
        """The bird can swim

        Returns:
            str: a swiming bird can do something
        """
        return f'{self._name} bird can swim'


class BaseBird():
    """The base class for the bird object."""

    def __init__(self, name):
        """Initializer for class BaseBird.

        Args:
            name (str): bird name
        """
        self._name = name

    def walk(self):
        """The bird can walk

        Returns:
            str: the bird can walk
        """
        return f'{self._name} can walk'

    def __str__(self) -> str:
        return self._name

    def __getattr__(self, name):
        raise AttributeError(
            f'"{self._name}" object has no attribute "{name}"')


class Bird(BaseBird, FlyMixin):
    """Class for birds that can walk and fly."""

    def __str__(self) -> str:
        return f'{super().__str__()} can walk and fly'


class FlyingBird(BaseBird, FlyMixin, EatMixin):
    """Flying bird class."""

    def __init__(self, name, ration='worm'):
        """Initializer for class FlyingBird.

        Args:
            name (str): bird name
            ration (str, optional): what does it eat?. Defaults to 'worm'.
        """
        super().__init__(name)
        self._ration = ration

    def __str__(self) -> str:
        return f'{super().__str__()} can walk and fly'


class NonFlyingBird(BaseBird, EatMixin, SwimMixin):
    """Class for birds that can't fly."""

    def __init__(self, name, ration):
        """Initializer for class NonFlyingBird.

        Args:
            name (str): bird name
            ration (str): what does it eat?
        """
        super().__init__(name)
        self._ration = ration

    def eat(self):
        """Bird food.

        Returns:
            str: describes the bird's taste preferences
        """
        return f'{super().eat()}. This is delicious'

    def __str__(self) -> str:
        return f'{super().__str__()} can walk and swim'


class SuperBird(BaseBird, FlyMixin, EatMixin, SwimMixin):
    """Class for birds that can do everything."""

    def __init__(self, name, ration='fish'):
        """Initializer for class SuperBird.

        Args:
            name (str): bird name
            ration (str, optional):  what does it eat? Defaults to 'fish'.
        """
        super().__init__(name)
        self._ration = ration

    def eat(self):
        """Bird food.

        Returns:
            str: describes the bird's taste preferences
        """
        return f'It eats {self._ration}'

    def __str__(self):
        return f'{super().__str__()} can walk, swim and fly'


def main():
    print()
    print('{:*^30}'.format('The task 6.4'), end='\n\n')

    b = Bird('Any')
    print(f'walk() method: {b.walk()}')
    print(f'fly() method: {b.fly()}')
    print(f'str() method: {b}')
    print('-'*15)

    fb = FlyingBird('Canary')
    print(f'eat() method: {fb.eat()}')
    print(f'walk() method: {fb.walk()}')
    print(f'fly() method: {fb.fly()}')
    print(f'str() method: {fb}')

    print('-'*15)

    nfb = NonFlyingBird('Penguin', 'fish')
    print(f'eat() method: {nfb.eat()}')
    print(f'swim() method: {nfb.swim()}')
    print(f'walk() method: {nfb.walk()}')
    print(f'str() method: {nfb}')

    try:
        nfb.fly()
    except AttributeError as e:
        print(f'fly() method: {e}')

    print('-'*15)

    super_bird = SuperBird('Pelican', ration='shellfish')
    print(f'eat() method: {super_bird.eat()}')
    print(f'swim() method: {super_bird.swim()}')
    print(f'walk() method: {super_bird.walk()}')
    print(f'fly() method: {super_bird.fly()}')
    print(f'str() method: {super_bird}')

    print(SuperBird.mro())
