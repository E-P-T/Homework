
from abc import abstractmethod, ABC
from typing import Optional
from pandas import DataFrame


class IDataConverter(ABC):
    @abstractmethod
    def concat_data(self, data, local_data) -> Optional[DataFrame]:
        pass
