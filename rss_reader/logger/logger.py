
from logging import (getLogger, StreamHandler, Formatter,
                     Logger as LG,  DEBUG as DBG)

from rss_reader.interfaces.ilogger.ilogger import ISetLoggerConfig


class StreamHandlerConfig(ISetLoggerConfig):

    def set_config(self, name: str) -> LG:
        logger = getLogger(name)
        logger.setLevel(DBG)
        sh = StreamHandler()
        sh.setLevel(DBG)
        li = ['%(asctime)s', '%(name)s', '%(levelname)s', '%(funcName)s',
              '%(lineno)d', '%(message)s']
        str_f = '|'.join(li)
        formatter = Formatter(str_f, '%Y-%m-%d %H:%M:%S')


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

    def setup_logger(self) -> LG:
        """Set logger configuration.

        :return: object Logger
        :rtype: LG
        """
        return self._config.set_config(Logger.NAME_LOGGER)

    @classmethod
    def get_logger(cls, module_name: str) -> LG:
        """Get logger by name.

        :param module_name: Logger name.
        :type module_name: str
        :return: object Logger
        :rtype: LG
        """
        return getLogger(cls.NAME_LOGGER).getChild(module_name)
