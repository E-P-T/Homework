"""Entry point module"""
import cv_json
import logging
import allargs, argverbose
import feed_parser


class RssReader(allargs.Arguments):
    def __reaction_to_arguments(self) -> None:
        """
        Method that performs various actions
        depending on command line arguments
        """
        limit = self.args.limit
        source = self.args.source
        debug_string = "Start with arguments: " +\
            f"--limit: {limit}, " +\
            f"--json {self.args.json}, " +\
            f"--verbose {self.args.verbose}, "
        feed_json = cv_json.JsonConversion(source, limit)
        logging.debug(debug_string)
        logging.debug(f"URL: {source}")

        feed = feed_parser.RssParser(source, limit)

        if limit is not None and limit < 1:
            msg = "Limit is less than one"
            logging.info(f"Stop. {msg}")
            return msg

        news_parsing = feed.parse_news()
        logging.info(f"Get rss from {source}")
        if self.args.json:
            logging.info(f"Convert rss from {source} to json")
            result = feed_json.convert_to_json(news_parsing)
        else:
            logging.info("Show result of parsing")
            result = feed.make_pretty_rss(news_parsing)

        return result

    def get_verbose(self):
        return argverbose.AppLogging.show_logs() if self.args.verbose else ""

    def run(self) -> None:
        """Application launch"""
        logging.info("Run app")
        return self.__reaction_to_arguments()


def main():
    """Main application method"""
    try:
        argverbose.AppLogging.log_setup()
        rss_app = RssReader()
        print(rss_app.run())
        print(rss_app.get_verbose())
    except Exception as e:
        logging.error(e)
        print(e)

if __name__ == "__main__":
    main()
