

from typing import Dict, Optional
from rss_reader.interfaces.iviewer.iviewer import IViewHandler
from rss_reader.decorator.decorator import send_log_of_start_function


class AbstractViewHandler(IViewHandler):
    """The base class of the handler."""

    _next_handler: Optional[IViewHandler] = None

    @send_log_of_start_function
    def set_next(self, handler: IViewHandler) -> IViewHandler:
        """Set the next viewer in the handler chain.

        :param handler: Next handler.
        :type handler: IViewHandler
        :return: Handler.
        :rtype: IViewHandler
        """

        self._next_handler = handler
        return handler

    @send_log_of_start_function
    def show(self, data: dict) -> None:
        """Show data.

        :param data: Dictionary with data to be printed on the screen.
        :type data: dict
        """
        if self._next_handler:
            return self._next_handler.show(data)


class StandartViewHandler(AbstractViewHandler):
    """Displays data on standard output

    It is the base handler.
    Executed when others have failed to process the data.
    """

    def show(self, data: dict) -> None:
        """Show data.

        :param data: Dictionary with data to be printed on the screen.
        :type data: dict
        """

        self._get_info(data, "title_web_resource", "\nFeed: ", end="\n\n\n")
        items = data.get('items')
        if isinstance(items, list):
            for i in items:
                self._get_info(i, "title", "Title")
                self._get_info(i, "source", "Source")
                self._get_info(i, "pubDate", "PubDate")
                self._get_info(i, "link", "Link")
                media_content = i.get("content")
                if media_content:
                    print("Media content:")
                    self._get_info(media_content, "title",
                                   "[title of media content]")
                    self._get_info(media_content, "url",
                                   "[source of media content]")
                print('\n\n')
        elif items:
            print(items)

    def _get_info(self, dict_: dict, attr: str, str_: str, end='\n') -> None:
        """Print a string containing data from a dictionary."""
        x = dict_.get(attr)
        if x:
            print(f'{str_}: {x}', end=end)


class JSONViewHandler(AbstractViewHandler):
    def __init__(self, request: Dict[str, str]) -> None:
        """Initializer.

        :param request: A dictionary in which there may be a key
                        by which this handler will work.
        :type request: Dict[str, str]
        """
        self._request = request

    def show(self, data: dict) -> None:
        if self._request.get('json'):
            print(dumps(data, indent=3))
        else:
            super().show(data)
