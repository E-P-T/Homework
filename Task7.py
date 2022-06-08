# Task 6.7

from math import ceil


def type_prop(name, expected_type):
    """Argument type validator

    Args:
        name (str): argument name
        expected_type (class): expected type

    Raises:
        TypeError: when expected type and actual type do not match

    Returns:
        property: property
    """
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)
    return prop


class lazyproperty:
    """Lazily evaluated property.

    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Pagination:
    """Stores page pagination."""

    amount = type_prop('amount', int)
    text = type_prop('text', str)

    def __init__(self, text, amount) -> None:
        """Initializer for class Pagination.

        Args:
            text (str): text that is paginated.
            amount (int): how many symbols will be allowed per each page.
        """
        self.text = text
        self.amount = amount

    @lazyproperty
    def page_count(self):
        """Get number of pages.

        Returns:
            int: number of pages.
        """
        return ceil(len(self.text)/self.amount)
