"""The main configurator for launching the program."""

from typing import Dict
from bs4 import BeautifulSoup

from rss_reader.logger.logger import Logger
from rss_reader.interfaces.iloader.iloader import IHandler, ILoadHandler
from rss_reader.loader.loader import FromWebHandler, FromLocalSTorageHandler
from rss_reader.parser.parser import BeautifulParser
from rss_reader.crawler.crawler import SuperCrawler
from rss_reader.crawler.exceptions import BadURLError
from rss_reader.interfaces.iviewer.iviewer import IViewHandler
from rss_reader.viewer.viewer import StandartViewHandler, JSONViewHandler
from rss_reader.pathfile.pathfile import PathFile

from rss_reader.interfaces.isaver.isaver import ISaveHandler
from rss_reader.saver.saver import LocalSaveHandler

from .ecxeptions import NonNumericError

log = Logger.get_logger(__name__)

LOCAL_STORAGE = '.rss-reader/local_storage.csv'


class Starter:
    """A class to represent a starter main program."""

    def __init__(self, argv: Dict[str, str]) -> None:
        """Initializer.

        :param argv: Command line parameter dictionary.
        :type argv: Dict[str, str]
        """
        self._argv = argv

    def run(self) -> None:
        """Program launch."""

        data_handler = self._get_data_from_resource()
        try:
            data = data_handler.get_data()
        except BadURLError as e:
            log.error(e)
            raise

        log.info("Start getting the viewer object.")
        viewer = self._get_viewer(self._argv)
        log.info("Stop getting the viewer object.")

        log.info("Start displaying data.")
        viewer.show(data)
        log.info("Stop displaying data.")

        # the place where the database of saved queries is stored
        local_storage = PathFile().home()/LOCAL_STORAGE

        # save data
        self._get_saver().save(data, local_storage)

    def _get_limit(self) -> None:
        log.info("Get the number of requested news.")
        try:
            lim = self._argv.get('limit')
            limit = int(lim) if lim else None
        except ValueError as e:
            log.exception(e)
            raise NonNumericError("--limit has a non-numeric value") from e

        if limit is not None and limit < 0:
            raise ValueError('--limit must be positive')
        log.info("Number was received.")

        self._argv['limit'] = limit

    def _get_data_from_resource(self) -> ILoadHandler:
        """настроить обработчик иданных"""

        self._get_limit()

        wh = FromWebHandler('item',
                            'channel > title',
                            self._argv.get('source'),
                            self._argv.get('limit'),
                            SuperCrawler,
                            BeautifulParser(BeautifulSoup))
        local_storage = PathFile().home()/LOCAL_STORAGE

        ls = FromLocalSTorageHandler(local_storage, self._argv)
        ls.set_next(wh)
        return ls

    def _get_viewer(self, request: Dict[str, str]) -> IViewHandler:
        """Get data viewer."""
        stdout_ = StandartViewHandler()
        json_ = JSONViewHandler(request)
        json_.set_next(stdout_)
        return json_

    def _get_saver(self) -> ISaveHandler:
        standart_saver = LocalSaveHandler()

        return standart_saver
