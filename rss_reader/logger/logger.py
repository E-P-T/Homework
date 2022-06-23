
from logging import (getLogger, StreamHandler, Formatter,
                     NullHandler, Logger as LG,  DEBUG as DBG)

from rss_reader.interfaces.ilogger.ilogger import ISetLoggerConfig


class StreamHandlerConfig(ISetLoggerConfig):
    """Basic configuration.

    Sets up logging with the output of the result on the screen.
    """

    def set_config(self, name: str) -> LG:
        """Set logger configuration.

        :param name: Logger name.
        :type name: str
        :return: object Logger.
        :rtype: LG
        """

        logger = getLogger(name)
        logger.setLevel(DBG)
        sh = StreamHandler()
        sh.setLevel(DBG)
        li = ['%(asctime)s', '%(name)s', '%(levelname)s', '%(funcName)s',
              '%(lineno)d', '%(message)s']
        str_f = '|'.join(li)
        formatter = Formatter(str_f, '%Y-%m-%d %H:%M:%S')
        sh.setFormatter(formatter)
        logger.addHandler(sh)
        return logger


class NullHandlerConfig(ISetLoggerConfig):
    """Logger configuration with output to the void."""

    def set_config(self, name: str) -> LG:
        """Set logger configuration.

        :param name: Logger name.
        :type name: str
        :return: object Logger.
        :rtype: LG
        """

        logger = getLogger(name)
        logger.setLevel(DBG)
        sh = NullHandler()
        sh.setLevel(DBG)
        logger.addHandler(sh)
        return logger


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
