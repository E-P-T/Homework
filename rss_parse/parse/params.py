class Params:
    """
    Stores parameters to run rss reader.
    """

    def __init__(self, is_verbose, is_json, limit, source, pub_date, html_dir, pdf_dir):
        self.is_verbose = is_verbose
        self.is_json = is_json
        self.limit = limit
        self.source = source
        self.pub_date = pub_date
        self.html_dir = html_dir
        self.pdf_dir = pdf_dir

    @staticmethod
    def from_args(args):
        return Params(args.verbose, args.json, args.limit, args.source, args.date, args.to_html, args.to_pdf)
