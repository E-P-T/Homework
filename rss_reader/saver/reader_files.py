
from pandas import DataFrame, read_csv
from pandas.errors import EmptyDataError
from typing import Optional

from rss_reader.interfaces.isaver.ireader_files import IReadFile
from rss_reader.interfaces.ipathfile.ipathfile import ICreateFile
from rss_reader.logger.logger import Logger

log = Logger.get_logger(__name__)


class ReaderFiles(IReadFile):
    def read_csv_file(self, file: str,
                      index_col_: str,
                      creater: ICreateFile,
                      encoding_: str = 'utf-8') -> Optional[DataFrame]:
        """Read csv file.

        If the file does not exist, it will be created

        :param file: File name.
        :type file: str
        :param index_col_: Column(s) to use as the row labels of the DataFrame,
                        either given as string name or column index. If a
                        sequence of int / str is given, a MultiIndex is used.
        :type index_col_: str
        :param creater: An object that implements the ability to create a file.
                        Used when the requested file does not exist.
        :type creater: ICreateFile
        :param encoding_: File encoding, defaults to 'utf-8'
        :type encoding_: str, optional
        :return: Return the read data as a DataFrame.
        :rtype: Optional[DataFrame]
        """
        local_storage = None

        try:
            local_storage = read_csv(file,
                                     index_col=index_col_,
                                     encoding=encoding_)
        except EmptyDataError as e:
            log.error(f'{file} is empty')
        except FileNotFoundError as e:
            log.exception(f'No such file or directory: {file}')
            creater.create_file(file)

        return local_storage
