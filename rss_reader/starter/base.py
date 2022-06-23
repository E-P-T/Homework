"""Initial program setup.

This module contains functions intended for the initial setup of the program.
"""


import argparse
from typing import Dict


NAME_LOGGER = 'rss-reader'
version = '0.0.1'


def init_arguments_functionality(args=None) -> Dict[str, str]:
    """Create command line options.

    :param args: Command line options, defaults to None.
    :type args: List, optional.
    :return: Command line parameter dictionary.
    :rtype: Dict[str, str]
    """

    parser = argparse.ArgumentParser(
        prog='RSS reader',
        description='Pure Python command-line RSS reader.',
        epilog='''(c) 2022. Have a nice day.'''
    )

    parser.add_argument('source',
                        nargs='?',
                        default='https://news.yahoo.com/rss/',
                        help='RSS URL')

    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s version {}'.format(version),
                        help='Print version info')

    parser.add_argument('--json',
                        action='store_true',
                        help='Print result as JSON in stdout')

    parser.add_argument('--verbose',
                        action='store_true',
                        help='Outputs verbose status messages')

    parser.add_argument('--limit',
                        help='Limit news topics if this parameter provided')

    namespace_ = parser.parse_args(args)

    return vars(namespace_)


def create_logger(verbose: Optional[str]) -> None:
    if verbose:
        config = StreamHandlerConfig()
    else:
        config = NullHandlerConfig()
