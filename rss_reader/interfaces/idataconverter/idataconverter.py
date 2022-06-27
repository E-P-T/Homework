"""This module contains a set of interfaces for the logger."""


from abc import abstractmethod, ABC
from typing import Optional
from pandas import DataFrame


class IDataConverter(ABC):
    """Basic converter interface."""

    @abstractmethod
    def concat_data(self, data, local_data) -> Optional[DataFrame]:
        """Get normalized data."""
        pass
