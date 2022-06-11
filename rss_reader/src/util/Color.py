from enum import Enum


class Color(Enum):
    """
    Enum for color.
    """
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'
