"""This module contains data readers from files."""


from pandas import DataFrame, read_csv
from pandas.errors import EmptyDataError

from rss_reader.interfaces.iloader.ireader_files import IReadFile
from .exceptions import DataFileNotFoundError, DataFileEmptyError


class ReaderCSVFile(IReadFile):
    """Reader CSV File."""

    @staticmethod
    def read(file: str,
             index_col: str = 'index', encoding='utf-8') -> DataFrame:
        """Read CSV File.

        :param file: File name.
        :type file: str
        :param index_col: Column(s) to use as the row labels of the DataFrame,
        either given as string name or column index. If a sequence of
        int / str is given, a MultiIndex is used, defaults to 'index'.
        :type index_col: str, optional
        :param encoding: Encoding to use for UTF when reading/writing
        (ex. ‘utf-8’). , defaults to 'utf-8'
        :type encoding: str, optional
        :raises DataFileNotFoundError: Occurs when the file is not found.
        :raises DataFileEmptyError: Occurs when there is no data in the
        uploaded file.
        :return: The data read from the file as a DataFrame.
        :rtype: DataFrame
        """
        try:
            raw_data = read_csv(file, index_col=index_col, encoding=encoding)
        except FileNotFoundError as e:
            raise DataFileNotFoundError(file) from e
        except EmptyDataError as e:
            raise DataFileEmptyError(file) from e

        return raw_data
