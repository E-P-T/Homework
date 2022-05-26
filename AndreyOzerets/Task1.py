# Task 5.1

from typing import Iterable


def line_from_file(file: str, end: str = '\n', **kwargs) -> Iterable[str]:
    '''Return a string in one iteration'''

    with open(file, **kwargs) as raw_file:
        for line in raw_file:
            if not line.endswith(end):
                line = line + end
            yield line
