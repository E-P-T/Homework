# Task 5.3


import csv
from functools import partial
from heapq import merge, nlargest
from itertools import chain, islice
from typing import Callable, Iterable, List, Optional, OrderedDict, Sequence


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


def list_sorted_chunks(f_csv,
                       gen_funk,
                       sort_funk) -> List[List[OrderedDict]]:
    '''List of sorted elements'''

    sorted_tmp_files: List[List[OrderedDict]] = []
    sorted_tmp_files_append = sorted_tmp_files.append

    for chunk in gen_funk(f_csv):
        sorted_chunk = sort_funk(chunk)
        sorted_tmp_files_append(sorted_chunk)

    return sorted_tmp_files


def sort_csv(in_file: str,
             out_file: str,
             sort_func: Callable[[Iterable],
                                 List[List[OrderedDict]]],
             merge_func) -> None:
    '''Write sorted csv file'''

    fields: Optional[Sequence[str]] = []

    try:
        with open(in_file) as f:
            f_csv = csv.DictReader(f)
            fields = f_csv.fieldnames
            sorted_files = sort_func(f_csv)

    except FileNotFoundError as er:
        print(er)
        raise er
    else:
        with open(out_file, 'w', newline='') as output_file:
            out_csv = csv.DictWriter(output_file, fields)
            out_csv.writeheader()
            out_csv.writerows(merge_func(*sorted_files))


if __name__ == '__main__':
    in_file = 'data/students.csv'
    out_file = 'data/sorted_by_names.csv'

    print()
    print('{:*^30}'.format('Task 5.3.1'))
    names = get_top_performers(in_file)
    print(f'Names of top performer students: {names}', end='\n\n')

    print('{:*^30}'.format('Task 5.3.2'))
    sort_funk = partial(
        sorted, key=lambda student: student['age'], reverse=True)
    sort_chunks = partial(list_sorted_chunks,
                          gen_funk=get_chunk, sort_funk=sort_funk)
    merge_func = partial(
        merge, key=lambda student: student['age'], reverse=True)
    sort_csv(in_file, out_file, sort_chunks, merge_func)
    print(f'The sorted "{out_file}" file is written.', end='\n\n')