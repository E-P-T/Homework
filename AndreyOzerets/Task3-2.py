# Task 2.3-2


def get_number(greeting: str) -> int:
    '''Get number from user.'''
    while True:
        try:
            number = int(input(greeting))
            break
        except ValueError:
            print("You entered not a number!!! Try it again...")
    return number
