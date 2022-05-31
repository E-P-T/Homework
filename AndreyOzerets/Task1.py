# Task 5.1

from heapq import merge
from itertools import islice
from typing import Iterable, List
from tempfile import _TemporaryFileWrapper, TemporaryFile


def line_from_file(file: str, end: str = '\n', **kwargs) -> Iterable[str]:
    '''Return a string in one iteration'''

    with open(file, **kwargs) as raw_file:
        for line in raw_file:
            if not line.endswith(end):
                line = line + end
            yield line


def get_chunk(data: Iterable[str],
              amount_of_elements: int = 10,
              **kwargs) -> Iterable[List[str]]:
    '''Return a chunk of strings'''

    while True:
        chunk = list(islice(data, amount_of_elements, **kwargs))
        if not chunk:
            break
        yield chunk


def write_to_tmp_file(tmp_file: _TemporaryFileWrapper,
                      chunk: List[str]) -> _TemporaryFileWrapper:
    '''Write a list of lines to a temporary file'''

    tmp_file.writelines(chunk)
    tmp_file.seek(0)

    return tmp_file


def close_tmp_files(tmp_files: List[_TemporaryFileWrapper]) -> None:
    '''Close list of temporary files'''

    for f in tmp_files:
        f.close()


if __name__ == '__main__':
    sorted_tmp_files: List[_TemporaryFileWrapper] = []
    sorted_tmp_files_append = sorted_tmp_files.append
    print()
    print('{:*^30}'.format('The task 5.1'), end='\n\n')

    try:
        for chunk in get_chunk(line_from_file('data/unsorted_names.txt')):
            chunk.sort()
            tmp_file = TemporaryFile('w+')
            tmp_file_with_data = write_to_tmp_file(tmp_file, chunk)
            sorted_tmp_files_append(tmp_file_with_data)
    except FileNotFoundError as er:
        print(er, end='\n\n')
    else:
        with open('data/sorted_names.txt', 'w') as output_file:
            output_file.writelines(merge(*sorted_tmp_files))

        print(f'Names sorted and wrote to file', end='\n\n')
    finally:
        close_tmp_files(sorted_tmp_files)
