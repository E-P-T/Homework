# Task 7.10


def endless_generator():
    """Endless generator."""
    number = 1
    while True:
        yield number
        number += 2
