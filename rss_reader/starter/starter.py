

from typing import Dict

from rss_reader.logger.logger import Logger
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

        lim = self._argv.get('limit')
        limit = int(lim) if lim else None

        log.info("Number was received.")
