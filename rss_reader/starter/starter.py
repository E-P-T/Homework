

from typing import Dict
from bs4 import BeautifulSoup

from rss_reader.logger.logger import Logger
from rss_reader.interfaces.iloader.iloader import IHandler
from rss_reader.loader.loader import FromWebHandler
from rss_reader.parser.parser import BeautifulParser
from rss_reader.crawler.crawler import SuperCrawler
from rss_reader.interfaces.iviewer.iviewer import IViewHandler
from rss_reader.viewer.viewer import StandartViewHandler, JSONViewHandler

from .ecxeptions import NonNumericError

log = Logger.get_logger(__name__)


class Starter:
    def __init__(self, argv: Dict[str, str]) -> None:
        """Initializer.

        :param argv: Command line parameter dictionary.
        :type argv: Dict[str, str]
        """
        self._argv = argv

    def run(self) -> None:
        log.info("Get the number of requested news.")

        try:
            lim = self._argv.get('limit')
            limit = int(lim) if lim else None
        except ValueError as e:
            log.exception(e)
            raise NonNumericError("--limit has a non-numeric value") from e

        log.info("Number was received.")

        data_handler = self._get_data_from_resource()

    def _get_data_from_resource(self) -> IHandler:
        """Get data handler.

        :return: Data handler.
        :rtype: IHandler
        """
        web_hendler = FromWebHandler(SuperCrawler,
                                     BeautifulParser(BeautifulSoup))
        return web_hendler

    def _get_viewer(self, request: Dict[str, str]) -> IViewHandler:
        """Get data viewer."""
        stdout_ = StandartViewHandler()
        json_ = JSONViewHandler(request)
        json_.set_next(stdout_)
        return json_
