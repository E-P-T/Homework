

class IReadFile(ABC):
    @abstractmethod
    def read_csv_file(self, file: str,
                      index_col_: str,
                      creater: ICreateFile,
                      encoding_: str = 'utf-8') -> Optional[DataFrame]:
        """Read csv file.

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
        pass
