# The Task 4.5


from typing import List, Tuple


def option_1(num: int) -> Tuple[int]:
    '''Returns a tuple of a given integer's digits

    Option number 1.
    '''
    return tuple(int(i) for i in str(num))


def option_2(num: int) -> Tuple[int]:
    '''Returns a tuple of a given integer's digits

    Option number 2.
    '''
    digits: List[int] = []
    digits_append = digits.append
    while num:
        digits_append(num % 10)
        num //= 10
    return tuple(digits[::-1])


if __name__ == '__main__':

    print()
    print('{:*^30}'.format('Task 4.5'), end='\n\n')
    print(f'Option_1:', end='\n\n')
    print(option_1(87178291199))

    print('-'*30, end='\n\n')

    print(f'Option_2:', end='\n\n')
    print(option_1(87178291199))
