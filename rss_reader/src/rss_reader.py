from urllib.error import URLError
from xml.etree.ElementTree import ParseError

from args.Arguments import Arguments
from info import name, version
from news.News import News
from util.Logger import Logger
from util.Util import Util


def main() -> None:
    """
    Main function of the program.
    """

    args = Arguments(name, version)

    logger = Logger(args.verbose)
    logger.info(f'Downloading from {args.source}')
    try:
        element = Util.url_to_element(args.source)
    except (URLError, ValueError):
        logger.error('Invalid URL')
        return
    except ParseError:
        logger.error('Invalid XML')
        return

    logger.info('Parsing XML')
    news = News.parse(element, args.limit)

    print(
        Util.to_json(news) if args.json
        else Util.to_str(news)
    )


if __name__ == '__main__':
    main()
