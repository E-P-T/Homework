from abc import ABC, abstractmethod

from pandas import DataFrame


class IComponent(ABC):
    """Basic Component Interface"""

    @abstractmethod
    def operation(self, data: DataFrame) -> DataFrame:
        pass


class BaseComponent(IComponent):
    def operation(self, data) -> str:
        return data
