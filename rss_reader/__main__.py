"""Entry point to the program."""


from rss_reader.starter.base import (create_logger,
                                     init_arguments_functionality as iaf)
from rss_reader.logger.logger import Logger
from rss_reader.starter.ecxeptions import NonNumericError
from rss_reader.crawler.exceptions import BadURLError


def main():

    args = iaf()
    create_logger(args.get('verbose'))
    log = Logger.get_logger(__name__)

    from rss_reader.starter.starter import Starter
    log.debug("Create a Starter object.")
    s = Starter(args)

    try:
        log.info("Start the program.")
        s.run()
    except NonNumericError as e:
        print(f'Sorry, we have to stop working. Because:')
        print(f'\t {e}')
        log.error(e)
    except BadURLError as e:
        print(f'Sorry, we have to stop working. Because:')
        print(f'\t {e}')
        log.error(e)
    except Exception as e:
        s = ('Sorry, we have to stop working. Something went wrong.'
             'We are terribly sorry.')
        print(s)
        log.error(e)
    finally:
        log.info("Stop the program.")
        exit()


if __name__ == "__main__":
    main()
