# Task 6.2

from copy import deepcopy


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

    """A queue with a limited number of elements.

    When the maximum number of elements is reached,
    removes the last element and inserts a new one.

    Attributes
    ----------
    max_elms : int
        maximum number of elements. Defaults to 10.

    """

    def __init__(self, max_elms=10):
        """Initializer for class LimitedQueue.

        Args:
            max_elms (int, optional): maximum number of elements. Defaults to 10.
        """
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

    @property
    def get_items(self):
        """Return a list of elements.

        Returns:
            List[int]: a list of elements.
        """
        return self._items


class HistoryDict():

    """Remember last modified dictionary keys.

    When saving a new element, controls the dictionary
    in which to store N last changed keys. N is set by the user.

    Attributes
    ----------
    lim_queue (LimitedQueue):
                A queue with a limited number of elements.
    data_dict (Dict[str, int], optional):
                source dict. Defaults to None.

    """

    def __init__(self, lim_queue, data_dict=None) -> None:
        """Initializer for class HistoryDict.

        Args:
            lim_queue (LimitedQueue):
                A queue with a limited number of elements.
            data_dict (Dict[str, int], optional):
                source dict. Defaults to None.

        """
        self.data_dict = data_dict
        self._lim_queue = lim_queue

    @property
    def data_dict(self):
        return self._data_dict

    @data_dict.setter
    def data_dict(self, value):
        if value is None:
            self._data_dict = {}
        else:
            self._data_dict = deepcopy(value)

    def get_history(self):
        """Return a list of elements.

        Returns:
            List[int]: a list of elements.
        """
        return self._lim_queue.get_items

    def set_value(self, key, value):
        """Set new element to dictionary.

        Args:
            key (str): key dictionary element.
            value (int): value dictionary element.
        """
        self.data_dict[key] = value
        self._lim_queue.enqueue(key)


def main():
    """Main function."""

    print('\n{:*^30}'.format('The task 6.2'))

    source_dict = {'a': 1}

    d = HistoryDict(LimitedQueue(2), source_dict)
    print(f'Last added keys: {d.get_history()}')

    d.set_value("bar", 43)
    print(f'Last added keys: {d.get_history()}')
    d.set_value("bs", 3)
    print(f'Last added keys: {d.get_history()}')
    d.set_value("x", 31)
    print(f'Last added keys: {d.get_history()}')
    d.set_value("g", 333)
    print(f'Last added keys: {d.get_history()}')
    d.set_value("k", 35677)
    print(f'Last added keys: {d.get_history()}')

    print(f'Data Dictionary: {d.data_dict}')
    print(f'Source dictionary: {source_dict}')


if __name__ == '__main__':
    main()
