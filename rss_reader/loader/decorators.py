"""This module implements the decorator pattern."""


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
    """A decorator that produces a certain number of entries."""

    def __init__(self, limit: int, component: IComponent) -> None:
        """Initializer.

        :param limit: How many records to return.
        :type limit: int
        :param component: object of type IComponent.
        :type component: IComponent
        """
        self._limit = limit
        super().__init__(component)

    def operation(self, data: DataFrame) -> DataFrame:
        """Return the required number of data records.

        :param data: Sample data.
        :type data: DataFrame
        :return: Data sampling.
        :rtype: DataFrame
        """
        result = self.component.operation(data)
        return result.head(self._limit)


class SortByEqual(Decorator):
    def __init__(self, search_column: str, criterion: str,
                 component: IComponent) -> None:
        """Initializer.

        :param search_column: the name of the column to select from.
        :type search_column: str
        :param criterion: comparison criterion.
        :type criterion: str
        :param component: object of type IComponent.
        :type component: IComponent
        """
        self._search_column = search_column
        self._criterion = criterion
        super().__init__(component)

    def operation(self, data: DataFrame) -> DataFrame:
        """Return records that match the criteria.

        :param data: sample data.
        :type data: DataFrame
        :return: data sampling.
        :rtype: DataFrame
        """
        result = self.component.operation(data)
        return result[result[self._search_column] == self._criterion]
