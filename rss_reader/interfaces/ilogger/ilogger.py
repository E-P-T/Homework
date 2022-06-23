
from abc import ABC, abstractmethod
from logging import Logger as LG


class ISetLoggerConfig(ABC):
    @abstractmethod
    def set_config(self, name: str):
        pass
