class Params:
    """
    Stores parameters to run rss reader.
    """

    def __init__(self, is_verbose, is_json, limit, source):
        self.is_verbose = is_verbose
        self.is_json = is_json
        self.limit = limit
        self.source = source

    @staticmethod
    def from_args(args):
        return Params(args.verbose, args.json, args.limit, args.source)
