# Task 6.5
class Sun:
    """Singleton class."""

    _instance = None

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def main():
    """Main function."""

    w = Sun.inst()
    q = Sun.inst()
    print(w is q)
