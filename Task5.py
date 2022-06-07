# Task 6.5
class Sun:
    """Singleton class."""

    _instance = None

    @classmethod
    def inst(cls):
        print(cls)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance