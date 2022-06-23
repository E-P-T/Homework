
from abc import ABC, abstractmethod


class ISetLoggerConfig(ABC):
    @abstractmethod
    def set_config(self, name: str):
        pass
