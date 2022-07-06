# Task 7.9

def typed_prop(name, expectrd_type):
    """Type checking"""

    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expectrd_type):
            raise TypeError(f'{name} must be a {expectrd_type}')
        setattr(self, storage_name, value)

    return prop


class EvenRange:
    pass
