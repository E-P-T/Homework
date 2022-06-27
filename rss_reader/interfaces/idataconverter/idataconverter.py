"""This module contains a set of interfaces for the logger."""


from abc import abstractmethod, ABC
from typing import List, Optional
from pandas import DataFrame


class IDataConverter(ABC):
    """Basic converter interface."""

    @abstractmethod
    def concat_data(self, data: List[dict], local_data: str) -> Optional[DataFrame]:
        """Get normalized data."""
        pass
