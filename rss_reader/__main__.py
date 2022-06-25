"""Program entry point."""


from rss_reader.starter.base import (create_logger,
                                     init_arguments_functionality as iaf)
from rss_reader.starter.starter import Starter
from rss_reader.logger.logger import Logger


def main():
    args = iaf()
    create_logger(args.get('verbose'))
    s = Starter(args)

    log = Logger.get_logger(__name__)
    s.run()


if __name__ == "__main__":
    main()
