# Task 5.3


import csv
from heapq import nlargest
from itertools import chain, islice
from typing import Iterable, List, OrderedDict


def get_chunk(data: Iterable,
              amount_of_elmnts: int = 100) -> Iterable[List[OrderedDict[str,
                                                                        str]]]:
    '''Return a chunk of strings'''

    while True:
        chunk = list(islice(data, amount_of_elmnts))
        if not chunk:
            break
        yield chunk


def get_top_performers(file: str,
                       number_of_top_students: int = 5) -> List[str]:
    '''Return top performers list'''

    dic_out: List[OrderedDict] = []

    with open(file) as f:
        f_csv = csv.DictReader(f)
        for i in get_chunk(f_csv):
            q = nlargest(number_of_top_students, chain(i, dic_out),
                         key=lambda student: float(student['average mark']))
            dic_out.clear()
            dic_out.extend(q)
        return [i['student name'] for i in dic_out]


if __name__ == '__main__':
    in_file = 'data/students.csv'
    out_file = 'data/sorted_by_names.csv'

    print()
    print('{:*^30}'.format('Task 5.3.1'))
    names = get_top_performers(in_file)
    print(f'Names of top performer students: {names}', end='\n\n')
