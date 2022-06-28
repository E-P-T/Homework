class Params:
    """
    Stores parameters to run rss reader.
    """

    def __init__(self, is_verbose, is_json, limit, source, pub_date):
        self.is_verbose = is_verbose
        self.is_json = is_json
        self.limit = limit
        self.source = source
        self.pub_date = pub_date

    @staticmethod
    def from_args(args):
        return Params(args.verbose, args.json, args.limit, args.source, args.date)
