

from typing import Optional
from rss_reader.interfaces.iviewer.iviewer import IViewHandler
from rss_reader.decorator.decorator import send_log_of_start_function


class AbstractViewHandler(IViewHandler):
    """The base class of the handler."""

    _next_handler: Optional[IViewHandler] = None

    @send_log_of_start_function
    def set_next(self, handler: IViewHandler) -> IViewHandler:
        """Set the next viewer in the handler chain."""

        self._next_handler = handler
        return handler

    @send_log_of_start_function
    def show(self, data: dict) -> None:
        """Show data."""
        if self._next_handler:
            return self._next_handler.show(data)


class StandartViewHandler(AbstractViewHandler):
    def show(self, data: dict) -> None:
        self._get_info(data, "title_web_resource", "\nFeed: ", end="\n\n\n")
        items = data.get('items')

    def _get_info(self, dict_: dict, attr: str, str_: str, end='\n') -> None:
        """Print a string containing data from a dictionary."""
        x = dict_.get(attr)
        if x:
            print(f'{str_}: {x}', end=end)
