"""
    Module that contains main function for running parsing
"""

import warnings
from .parsers import Parser

warnings.filterwarnings("ignore", module="bs4")


def main():
    """
    Function that creates a parser object which takes command line arguments
    and prints result to stdout (output result is depending on arguments)
    :return:
    """
    parser = Parser()
    try:
        result = parser.start_parse()
        print(result)
    except Exception as exc:
        print(exc.__class__.__name__)
        print(exc)
