#!/usr/bin/env python
import sys
from rss_reader.run import run
from rss_reader.exceptions import PythonVersionError

if __name__ == '__main__':
    sys.tracebacklimit = -1
    if sys.version_info < (3, 9):
        raise PythonVersionError('It needs at least 3.9 version of Python to run the application')
    run()
