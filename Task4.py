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
