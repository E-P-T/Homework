# Task 6.2

def typed_property(name, expected_type):
    """Function to check the type of an argument."""

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


class LimitedQueue:
    def __init__(self, max_elms=10):
        self._items = []
        self.max_elms = max_elms
