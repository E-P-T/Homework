# Task 5.3


import csv
from heapq import nlargest
from itertools import chain
from typing import List, OrderedDict


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
