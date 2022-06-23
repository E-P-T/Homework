

from typing import Dict

from rss_reader.logger.logger import Logger


class Starter:
    def __init__(self, argv: Dict[str, str]) -> None:
        """Initializer.

        :param argv: Command line parameter dictionary.
        :type argv: Dict[str, str]
        """
        self._argv = argv
