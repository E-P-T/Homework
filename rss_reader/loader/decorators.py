from abc import ABC, abstractmethod

from pandas import DataFrame


class IComponent(ABC):
    """Basic Component Interface"""

    @abstractmethod
    def operation(self, data: DataFrame) -> DataFrame:
        pass


class BaseComponent(IComponent):
    """A base concrete component.

    It is a stub.
    """

    def operation(self, data) -> str:
        return data


class Decorator(IComponent):
    """Decorator base class."""

    _component: IComponent = None

    def __init__(self, component: IComponent) -> None:
        self._component = component

    @property
    def component(self) -> IComponent:
        return self._component

    def operation(self, data) -> DataFrame:
        return self._component.operation(data)


class LimitRecords(Decorator):
    def __init__(self, limit: int, component: IComponent) -> None:
        """Initializer.

        :param limit: How many records to return.
        :type limit: int
        :param component: object of type IComponent.
        :type component: IComponent
        """
        self._limit = limit
        super().__init__(component)
