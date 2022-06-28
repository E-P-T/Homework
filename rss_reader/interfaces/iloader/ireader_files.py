
from abc import ABC, abstractmethod
from pandas import DataFrame


class IReadFile(ABC):
    @abstractmethod
    def read(file: str,
             index_col: str = 'index', encoding='utf-8') -> DataFrame:
        pass
