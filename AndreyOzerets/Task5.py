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


if __name__ == '__main__':

    print()
    print('{:*^30}'.format('Task 2.5'), end='\n\n')

    i = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
         {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

    it = func_gen(i)

    print(f'Function result "func_comprs": {func_comprs(i)}', end='\n\n')
    print(f'Function result "func_for": {func_for(i)}', end='\n\n')
    print(f'Function result "func_iter": {func_iter(it)}', end='\n\n')
