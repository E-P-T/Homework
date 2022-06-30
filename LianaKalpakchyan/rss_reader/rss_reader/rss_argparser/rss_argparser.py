#!/usr/bin/env python3
import argparse


class Argparser():
    """
    A class to get arguments from CLI

    ...

    Attributes
    ----------
    version: str
       Keeps the program current version

    Methods
    -------
    get_args():
        Implements cli arguments processing
    """

    def __init__(self):
        self.version = '0.4.0'

    def get_args(self):
        """This function processes arguments received from console using argparse module.
        :return: Namespace (args)
        """
        parser = argparse.ArgumentParser(
            description='One-shot command-line RSS reader ^_^')
        parser.add_argument('source',
                            help='RSS URL',
                            nargs='?',
                            default=None)
        parser.add_argument('--version',
                            action='store_true',
                            help='Print version info')
        parser.add_argument('--json',
                            action='store_true',
                            help='Print result as JSON in stdout')
        parser.add_argument('--verbose', '--v',
                            action='store_true',
                            help='Outputs verbose status messages')
        parser.add_argument('--limit',
                            type=int,
                            help='Limit news topics if this parameter provided',
                            default=-1)
        parser.add_argument('--date',
                            help='Takes a date. For example: for "--date 20191020" \
                            news from the specified day will be printed out.',
                            type=int,
                            default=None)
        parser.add_argument('--to-pdf',
                            help='Conversion of news into a PDF format',
                            nargs='*')
        parser.add_argument('--to-html',
                            help='Conversion of news into an HTML format',
                            nargs='*')
        args = parser.parse_args()
        if args.version:
            print(f'Program version: {self.version}')
            if args.source is None:
                exit()

        return args
