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

    pass
