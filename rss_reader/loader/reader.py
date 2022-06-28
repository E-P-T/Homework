
from pandas import DataFrame, read_csv
from pandas.errors import EmptyDataError

from rss_reader.interfaces.iloader.ireader_files import IReadFile
from .exceptions import DataFileNotFoundError, DataFileEmptyError


class ReaderCSVFile(IReadFile):
    @staticmethod
    def read(file: str,
             index_col: str = 'index', encoding='utf-8') -> DataFrame:
        try:
            raw_data = read_csv(file, index_col=index_col, encoding=encoding)
        except FileNotFoundError as e:
            raise DataFileNotFoundError(file) from e
        except EmptyDataError as e:
            raise DataFileEmptyError(file) from e

        return raw_data
