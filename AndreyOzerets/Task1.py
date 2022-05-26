# Task 5.1

from itertools import islice
from typing import Iterable, List
from tempfile import _TemporaryFileWrapper


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
    '''Return a chunk of string'''

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
