
from logging import Logger as LG

from rss_reader.interfaces.ilogger.ilogger import ISetLoggerConfig


class Logger:
    """Logs data."""

    NAME_LOGGER = 'base_logger'

    def __init__(self, name_loger: str, config: ISetLoggerConfig) -> None:
        """Initializer.

        :param name_loger: Logger name.
        :type name_loger: str
        :param config: Logger configuration.
        :type config: ISetLoggerConfig
        """
        Logger.NAME_LOGGER = name_loger
        self._config = config

    def setup_logger(self):
        return self._config.set_config(Logger.NAME_LOGGER)

    def get_logger(cls, module_name: str):
        pass
