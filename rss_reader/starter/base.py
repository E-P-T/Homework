
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
