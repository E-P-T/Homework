# Task 2.5

from typing import Dict, Iterable, List, Set


def func_comprs(data_list: List[Dict[str, str]]) -> Set[str]:
    '''Return unique dictionary values

    Implemented via set comprehension.
    '''
    return {dict_[value] for dict_ in data_list for value in dict_}


def func_for(data_list: List[Dict[str, str]]) -> Set[str]:
    '''Return unique dictionary values

    Implemented via for loops.
    '''
    un_set: Set[str] = set()
    un_set_add = un_set.add

    for dict_ in data_list:
        for value in dict_.values():
            un_set_add(value)

    return un_set


def func_gen(data_list: List[Dict[str, str]]) -> Iterable[Dict[str, str]]:
    '''Return list element.'''
    for i in data_list:
        yield i


def func_iter(gen: Iterable[Dict[str, str]]) -> Set[str]:
    '''Return unique dictionary values

    Implemented via iterator.
    '''
    un_set: Set[str] = set()
    un_set_add = un_set.add

    for i in gen:
        un_set_add(*i.values())

    return un_set
