

from typing import Optional
from rss_reader.interfaces.iviewer.iviewer import IViewHandler
from rss_reader.decorator.decorator import send_log_of_start_function


class AbstractViewHandler(IViewHandler):
    _next_handler: Optional[IViewHandler] = None

    @send_log_of_start_function
    def set_next(self, handler: IViewHandler) -> IViewHandler:
        """Set the next viewer in the handler chain."""

        self._next_handler = handler
        return handler

    def show(self, data: dict) -> None:
        pass
