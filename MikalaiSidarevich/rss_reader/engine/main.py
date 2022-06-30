"""
main() - entry point: parse CLI arguments & run RSS reading.
"""

import sys

from engine.argparser import ArgParser
from engine.rssreader import RssReader

version = '1.2'


def main():
    """
    Entry point - get CLI arguments and start process.
    """
    # Set console encoding to UTF-8
    sys.stdout.reconfigure(encoding='utf-8')

    arg_parser = ArgParser()
    args = arg_parser.args

    try:
        if args['version']:
            print(f"Version {version}")
            exit(0)

        json = False
        if args['json']:
            json = args['json']

        verbose = False
        if args['verbose']:
            verbose = args['verbose']

        limit = None
        if args['limit'] is not None:
            limit = int(args['limit'])

        url = None
        if args['source'] is not None:
            url = args['source']

    except Exception:
        print("Invalid argument value", flush=True)
        exit(1)

    if url:
        if verbose:
            print(f"URL is set: '{url}'", flush=True)
        try:
            rss = RssReader(verbose).read_rss(url, limit, json)
            print(rss, flush=True)
        except Exception as e:
            print(f"{type(e).__name__}: {e}", flush=True)
            exit(1)
    else:
        arg_parser.print_help()


if __name__ == '__main__':
    main()
