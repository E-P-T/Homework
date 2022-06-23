"""This module contains a set of interfaces for the logger."""


from abc import ABC, abstractmethod
from logging import Logger as LG


class ISetLoggerConfig(ABC):
    @abstractmethod
    def set_config(self, name: str) -> LG:
        """Set logger configuration.

        :param name: Logger name.
        :type name: str
        :return: object Logger.
        :rtype: LG
        """
        pass
