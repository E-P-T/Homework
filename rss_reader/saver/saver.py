
from typing import Optional

from rss_reader.interfaces.isaver.isaver import ISaveHandler


class AbstractSaveHandler(ISaveHandler):

    _next_handler: Optional[ISaveHandler] = None

    @send_log_of_start_function
    def set_next(self, handler: ISaveHandler) -> ISaveHandler:
        self._next_handler = handler
        return handler

    @send_log_of_start_function
    def save(self, data: dict, file: str):
        if self._next_handler:
            return self._next_handler.show(data)
