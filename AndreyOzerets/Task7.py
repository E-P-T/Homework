# Task 4.7


from typing import List


def foo(data: List[int]) -> List[int]:
    '''Return a list of products of numbers from the given list.

    The i-st element itself is not taken into account in the calculation.
    '''
    result = []

    for i in range(len(data)):
        accumulation = 1
        for key, value in enumerate(data):
            if i == key:
                continue
            else:
                accumulation *= value
        result.append(accumulation)

    return result


if __name__ == '__main__':
    print()
    print('{:*^30}'.format('Task 4.7'), end='\n\n')

    res = foo([1, 2, 3, 4, 5])
    print(res)
    res = foo([3, 2, 1])
    print(res)

    print()
