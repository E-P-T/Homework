
from typing import Optional, List

from rss_reader.interfaces.isaver.isaver import ISaveHandler
from rss_reader.decorator.decorator import send_log_of_start_function


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
    def save(self, data: List[dict], file: str) -> None:
        """Save data.

        :param data: Dictionary with data to save.
        :type data: List[dict]
        :param file: File save path.
        :type file: str
        """
        if self._next_handler:
            return self._next_handler.show(data)


class LocalSaveHandler(AbstractSaveHandler):
    def save(self, data: List[dict], file: str = 'local_storage.csv') -> None:
        local_data = ReaderFiles().read_csv_file(file, 'index', CreaterFiles())

        norm_data = DataConverter().concat_data(data, local_data)