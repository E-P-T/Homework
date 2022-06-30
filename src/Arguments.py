from argparse import ArgumentParser, Namespace
from datetime import datetime
from pathlib import Path


class Arguments(ArgumentParser):
    class Exception(ValueError):
        def __init__(self, message: str):
            self.message = message

    def __init__(self, name: str, version: float):
        super().__init__(description=name)

        self.add_argument('source', type=str, help='RSS URL', nargs='?')
        self.add_argument('--version', action='version', version=f'v{version}')
        self.add_argument('--json', action='store_true', help='show in JSON format')
        self.add_argument('--verbose', action='store_true', help='show detailed information')
        self.add_argument('--limit', type=int, help='limit the items')
        self.add_argument('--date', type=str, help='show items from specified date')
        self.add_argument('--to-fb2', type=str, help='save in fb2 format to specified path')
        self.add_argument('--to-html', type=str, help='save in html format to specified path')
        self.add_argument('--colorize', action='store_true', help='show items as colorized')

    def parse(self) -> Namespace:
        try:
            args = self.parse_args()

            if args.source is None and args.date is None:
                raise self.Exception('Either source or date should be specified')

            if args.date is not None:
                try:
                    args.date = datetime.strptime(args.date, '%Y%m%d')
                except ValueError:
                    raise self.Exception('Date must be in %Y%m%d format')

            self.check_absolute(args.to_fb2, '.fb2')
            self.check_absolute(args.to_html, '.html')

            return args
        except self.Exception as e:
            self.error(e.message)

    def check_absolute(self, path: str, ext: str) -> None:
        if path is None:
            return
        if not Path(path).is_absolute():
            raise self.Exception(path + ': should be absolute')
        if not path.endswith(ext):
            raise self.Exception(path + ': extension should be ' + ext)
