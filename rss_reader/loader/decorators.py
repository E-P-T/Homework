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

    _component: IComponent = None

    def __init__(self, component: IComponent) -> None:
        self._component = component

    @property
    def component(self) -> IComponent:
        return self._component
