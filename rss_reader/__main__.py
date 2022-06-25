"""Entry point to the program."""


from rss_reader.starter.base import (create_logger,
                                     init_arguments_functionality as iaf)
from rss_reader.logger.logger import Logger
from rss_reader.starter.ecxeptions import NonNumericError
from rss_reader.parser.exceptions import EmptyListError
from rss_reader.crawler.exceptions import BadURLError


def main():
    args = iaf()
    create_logger(args.get('verbose'))

    from rss_reader.starter.starter import Starter
    s = Starter(args)

    log = Logger.get_logger(__name__)
    s.run()


if __name__ == "__main__":
    main()
