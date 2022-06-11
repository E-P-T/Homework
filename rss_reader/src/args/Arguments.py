from argparse import ArgumentParser
from datetime import datetime


class Arguments:
    """
    Class-wrapper for ArgumentParser
    """

    source: str = None
    json: bool
    verbose: bool
    limit: int
    date: datetime = None

    def __init__(self, name: str, version: float):
        parser = ArgumentParser(description=name)

        source = 'source'
        json = 'json'
        verbose = 'verbose'
        limit = 'limit'
        date = 'date'

        parser.add_argument('source', type=str, help='RSS URL', nargs='?', default=None)
        parser.add_argument('--version', action='version', version=f'v{version}')
        parser.add_argument(f'--{json}', action='store_true', help='show in JSON format')
        parser.add_argument(f'--{verbose}', action='store_true', help='show detailed information')
        parser.add_argument(f'--{limit}', type=int, help='limit the items')
        parser.add_argument(f'--{date}', type=str, help='show cached items from specified date')

        args = parser.parse_args().__dict__

        self.source = args.get(source)
        self.json = args.get(json)
        self.verbose = args.get(verbose)
        self.limit = args.get(limit)

        date_str = args.get(date)

        if self.source is None and date_str is None:
            parser.error(f'the following arguments are required: {source} or {date}')
        elif date_str is not None:
            try:
                self.date = datetime.strptime(date_str, '%Y%m%d')
            except ValueError:
                parser.error(f'date must be in %Y%m%d format')
