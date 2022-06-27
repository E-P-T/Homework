"""This module contains a set of interfaces for the logger."""


from abc import abstractmethod, ABC
from typing import List, Optional
from pandas import DataFrame


class IDataConverter(ABC):
    """Basic converter interface."""

    @abstractmethod
    def concat_data(self, data: List[dict],
                    local_data: str) -> Optional[DataFrame]:
        """Get normalized data.

        :param data: Data for concatenation.
        :type data: List[dict]
        :param local_data: The name of the file where the locally saved data
                            is stored.
        :type local_data: str
        :return: DataFrame with merged data. Duplicates are removed.
        :rtype: Optional[DataFrame]
        """
        pass
