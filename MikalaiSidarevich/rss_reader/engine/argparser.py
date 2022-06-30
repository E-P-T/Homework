"""
ArgParser - parser for CLI arguments.
"""

import argparse
import sys


class ArgParser:
    """Parser for CLI arguments based on `argparse.ArgumentParser` parser."""

    def __init__(self):
        """
        Initialize parser with configured settings.
        """
        description = "Pure Python command-line RSS reader."
        self._parser = argparse.ArgumentParser(description=description)
        self._configure()

    def _configure(self):
        """
        Configure parser - add CLI arguments.
        """
        self._parser.add_argument("source", nargs='?', help="RSS URL")
        self._parser.add_argument("--version", action='store_true', help="Print version info")
        self._parser.add_argument("--json", action='store_true', help="Print result as JSON in stdout")
        self._parser.add_argument("--verbose", action='store_true', help="Outputs verbose status messages")
        self._parser.add_argument("--limit", help="Limit news topics if this parameter provided")
        self._parser.add_argument("--date", help="Read cached news by date specified like '%%Y%%m%%d'")

    @property
    def args(self):
        """
        Get CLI arguments in a dictionary format.
        """
        return vars(self._parser.parse_args(sys.argv[1:]))

    def print_help(self):
        """
        Print help message to console.
        """
        self._parser.print_help()
