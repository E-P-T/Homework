"""
main() - entry point: parse CLI arguments & run RSS reading.
"""

import subprocess
import sys

from engine.argparser import ArgParser
from engine.rssreader import RssReader

version = '1.5'
db = "storage.db"


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

        date = None
        if args['date'] is not None:
            date = args['date']

        html_path = None
        if args['to_html'] is not None:
            html_path = args['to_html']

        epub_path = None
        if args['to_epub'] is not None:
            epub_path = args['to_epub']

        colorizer = None
        if args['colorize']:
            if sys.platform == "linux":
                colorizer = subprocess.Popen("colorize",
                                             stdin=subprocess.PIPE,
                                             encoding='utf-8')
                sys.stdout = colorizer.stdin
            else:
                print("Unable to set colorized mode, set to normal mode.", flush=True)

    except Exception:
        print("Invalid argument value", flush=True)
        exit(1)

    if url or date:
        if verbose:
            print(f"URL is set: '{url}', read from {'cache' if date else 'URL'}", flush=True)
        try:
            rss = RssReader(verbose, db).read_rss(url, limit, json, date, html_path, epub_path)
            print(rss, flush=True)
        except Exception as e:
            print(f"{type(e).__name__}: {e}", flush=True)
            exit(1)
        finally:
            if colorizer:
                colorizer.communicate()
    else:
        arg_parser.print_help()


if __name__ == '__main__':
    main()
