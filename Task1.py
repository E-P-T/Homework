# Task 6.1


def type_validator(type_=int):
    """Argument type validator"""

    def decorator(func):
        def wrapper(self, value):
            if isinstance(value, type_) or value is None:
                func(self, value)
            else:
                raise TypeError('{} must be a {}'.format(value, type_))
        return wrapper
    return decorator
