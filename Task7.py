# Task 6.7
# Task 6.8


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
