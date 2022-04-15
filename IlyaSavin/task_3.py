# TASK2.3 FROM LECTION 2
"""
This module contains 2 functions that return unique and sorted sequence.
from arbitrary sequence. Also it contains speed tests for these functions.
"""


import timeit
from numpy import average as avg


def print_uniq_sorted_words(words_sequence, *, trace_output=False):
    """
    Function returns unique and sorted sequence of words.
    Type of sequence isn't changed by function.
    Argument trace_output gets False when it's no need to print output.
    """
    sequnce_type = type(words_sequence)
    unique_words_list = sorted(set(words_sequence))
    unique_words_sequence = sequnce_type(unique_words_list)
    if trace_output:
        print(unique_words_sequence)
    return unique_words_sequence


def print_uniq_sorted_words2(words_sequence, *, trace_output=False):
    """
    Function returns unique and sorted sequence of words.
    Type of sequence isn't changed by function.
    Argument trace_output gets False when it's no need to print output.
    """
    sequnce_type = type(words_sequence)
    unique_words_list = []
    for word in words_sequence:
        if word not in unique_words_list:
            unique_words_list.append(word)
    unique_words_list.sort()
    unique_words_sequence = sequnce_type(unique_words_list)
    if trace_output:
        print(unique_words_sequence)
    return unique_words_sequence


if __name__ == '__main__':
    print_uniq_sorted_words(
        ('red', 'white', 'black', 'red', 'green', 'black'),
        trace_output=True
    )  # Result: ('black', 'green', 'red', 'white')
    print_uniq_sorted_words(
        ['red', 'white', 'black', 'red', 'green', 'black'],
        trace_output=True
    )  # Result: ['black', 'green', 'red', 'white']
    print_uniq_sorted_words2(
        ('red', 'white', 'black', 'red', 'green', 'black'),
        trace_output=True
    )  # Result: ('black', 'green', 'red', 'white')
    print_uniq_sorted_words2(
        ['red', 'white', 'black', 'red', 'green', 'black'],
        trace_output=True
    )  # Result: ['black', 'green', 'red', 'white']
    result = timeit.repeat(
        stmt='print_uniq_sorted_words(("red", "white", "black", '
             + '"red", "green", "black"))',
        setup='import task_3',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00034506

    result = timeit.repeat(
        stmt='print_uniq_sorted_words2(("red", "white", "black", '
             + '"red", "green", "black"))',
        setup='import task_3',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00045342

    # ------------------------Results----------------------------------------
    # The best way to do this task is to use built-in functions.
