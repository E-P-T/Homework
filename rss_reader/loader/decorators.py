from abc import ABC, abstractmethod


class IComponent(ABC):
    """Basic Component Interface"""

    @abstractmethod
    def operation(self, data: DataFrame) -> DataFrame:
        pass
