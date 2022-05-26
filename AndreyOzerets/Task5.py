# Task 2.5

from typing import Dict, List, Set


def func_comprs(data_list: List[Dict[str, str]]) -> Set[str]:
    '''Return unique dictionary values

    Implemented via set comprehension.
    '''
    return {dict_[value] for dict_ in data_list for value in dict_}
