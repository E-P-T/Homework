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
