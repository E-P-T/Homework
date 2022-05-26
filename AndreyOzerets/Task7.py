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
