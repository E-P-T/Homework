
from abc import abstractmethod, ABC


class IDataConverter(ABC):
    @abstractmethod
    def concat_data(self, data, local_data) -> Optional[DataFrame]:
        pass
