from argparse import ArgumentParser


class Arguments:
    """
    Class-wrapper for ArgumentParser
    """

    source: str
    json: bool
    verbose: bool
    limit: int

    def __init__(self, name: str, version: float):
        parser = ArgumentParser(description=name)

        source = 'source'
        json = 'json'
        verbose = 'verbose'
        limit = 'limit'

        parser.add_argument(source, type=str, help='RSS URL')
        parser.add_argument('--version', action='version', version=f'v{version}')
        parser.add_argument(f'--{json}', action='store_true', help='show in JSON format')
        parser.add_argument(f'--{verbose}', action='store_true', help='show detailed information')
        parser.add_argument(f'--{limit}', type=int, help='limit the items')

        args = parser.parse_args().__dict__

        self.source = args.get(source)
        self.json = args.get(json)
        self.verbose = args.get(verbose)
        self.limit = args.get(limit)
