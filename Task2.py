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

    def is_empty(self):
        """Return a boolean whether the list is empty.

        Returns:
            bool: the list is empty?
        """
        return not bool(self._items)

    def dequeue(self):
        """Remove the last element from the list.

        Returns:
            int or None: last element from the list or None.
        """
        return self._items.pop(0) if self._items else None

    def enqueue(self, item):
        """Add a new element to the list.

        Args:
            item (int): new element
        """
        if self.size() >= self.max_elms:
            self.dequeue()
        self._items.append(item)

    def size(self):
        """Return the number of elements in the list.

        Returns:
            int: the number of elements in the list.
        """
        return len(self._items)
