import argparse
import os
from datetime import datetime


class ArgumentParser(argparse.ArgumentParser):
    """
    Class-wrapper for the argparse.ArgumentParser class
    """

    def __init__(self, name: str, version: float):
        super().__init__(description=name)

        self.add_argument('source', type=str, help='RSS URL', nargs='?', default=None)
        self.add_argument('--version', action='version', version=f'v{version}')
        self.add_argument('--json', action='store_true', help='show in JSON format')
        self.add_argument('--verbose', action='store_true', help='show detailed information')
        self.add_argument('--limit', type=int, help='limit the items')
        self.add_argument('--date', type=str, help='show cached items from specified date')
        self.add_argument('--to-html', type=str, help='generate HTML file and save it to specified path')
        self.add_argument('--to-pdf', type=str, help='generate PDF file and save it to specified path')

    class Arguments:
        source: str
        json: bool
        verbose: bool
        limit: int
        date: datetime
        html: str
        pdf: str

        def __init__(self, source: str, json: bool, verbose: bool, limit: int, date: str, html: str, pdf: str):
            if source is None and date is None:
                raise ValueError('Either source or date must be specified')

            if date is not None:
                try:
                    date = datetime.strptime(date, '%Y%m%d')
                except ValueError:
                    raise ValueError(f'date must be in %Y%m%d format')

            self.assert_file(html, '.html')
            self.assert_file(pdf, '.pdf')

            self.source = source
            self.json = json
            self.verbose = verbose
            self.limit = limit
            self.date = date
            self.html = html
            self.pdf = pdf

        @staticmethod
        def assert_file(path: str, ext: str) -> None:
            if path is not None:
                if not os.path.isabs(path):
                    raise ValueError(f'{path} must be an absolute path')
                if not path.endswith(ext):
                    raise ValueError(f'{path} must have {ext} extension')

    def parse(self) -> Arguments:
        """
        Parses the arguments.
        """
        try:
            return self.Arguments(*self.parse_args().__dict__.values())
        except ValueError as e:
            self.error(str(e))
