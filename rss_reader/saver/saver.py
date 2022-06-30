
import pandas as pd
from typing import Optional, List


from rss_reader.interfaces.isaver.isaver import ISaveHandler
from rss_reader.decorator.decorator import send_log_of_start_function
from rss_reader.data_converter.data_converter import DataConverter
from rss_reader.saver.reader_files import ReaderFiles
from rss_reader.pathfile.pathfile import PathFile


class AbstractSaveHandler(ISaveHandler):

    _next_handler: Optional[ISaveHandler] = None

    @send_log_of_start_function
    def set_next(self, handler: ISaveHandler) -> ISaveHandler:
        """Set the next saver in the handler chain.

        :param handler: Next handler.
        :type handler: ISaveHandler
        :return: Handler.
        :rtype: ISaveHandler
        """
        self._next_handler = handler
        return handler

    @send_log_of_start_function
    def save(self, data: List[dict]) -> None:
        """Save data.

        :param data: Dictionary with data to save.
        :type data: List[dict]
        """
        if self._next_handler:
            return self._next_handler.save(data)


class LocalSaveHandler(AbstractSaveHandler):
    """Stores data locally."""

    def __init__(self, file: str) -> None:
        self._file = file

    def save(self, data: List[dict]) -> None:
        """Save data.

        :param data: Dictionary with data to save.
        :type data: List[dict]
        """
        local_data = ReaderFiles().read_csv_file(
            self._file, 'index', PathFile())

        try:
            dc = DataConverter()
            norm_data = dc.normalize_(data, record_path=['items'],
                                      meta=['title_web_resource', 'link'],
                                      record_prefix="item.")
            norm_data = dc.convert_date(norm_data, 'item.pubDate')
            data_concat = dc.concat_data(local_data, norm_data,
                                         ignore_index=True)
            data_to_file = dc.drop_duplicates_(data_concat, keep='first',
                                               ignore_index=True)
        except NotImplementedError as e:
            local_data = None
            data_to_file = pd.DataFrame()

        data_to_file.to_csv(self._file, encoding='utf-8', index_label='index')
