

from rss_reader.interfaces.isaver.ireader_files import IReadFile


class ReaderFiles(IReadFile):
    def read_csv_file(self, file: str,
                      index_col_: str,
                      creater: ICreateFile,
                      encoding_: str = 'utf-8') -> Optional[DataFrame]:
        local_storage = None
