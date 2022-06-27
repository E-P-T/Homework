
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
        local_storage = None

        try:
            local_storage = read_csv(file,
                                     index_col=index_col_,
                                     encoding=encoding_)
        except EmptyDataError as e:
            pass
        except FileNotFoundError as e:
            pass

        return local_storage
