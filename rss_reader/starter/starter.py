

from typing import Dict

from rss_reader.logger.logger import Logger
from rss_reader.interfaces.iloader.iloader import IHandler
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

    def _get_data_from_resource(self):
        pass
