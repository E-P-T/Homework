"""This module contains specific viewers.

Viewers display data in the desired form.
Each viewer is called in a chain.
"""

from typing import Dict, List, Optional
from json import dumps

from rss_reader.interfaces.iviewer.iviewer import IViewHandler
from rss_reader.decorator.decorator import send_log_of_start_function
from rss_reader.logger.logger import Logger

log = Logger.get_logger(__name__)


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
    def show(self, data: List[dict]) -> None:
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

    def show(self, data: List[dict]) -> None:
        for i in data:
            self._show_item(i)

    def _show_item(self, data: dict):
        """Показать данные"""
        self._get_info(data, "title_web_resource", "\nFeed: ", end="\n\n\n")
        items = data.get('items')
        if isinstance(items, list):
            for i in items:
                self._get_info(i, "title", "Title")
                self._get_info(i, "source", "Source")
                self._get_info(i, "pubDate", "PubDate")
                self._get_info(i, "link", "Link")
                media_content = i.get("content")

                if not self._is_empty(media_content):
                    print("Media content:")
                    self._get_info(media_content, "title",
                                   "[title of media content]")
                    self._get_info(media_content, "url",
                                   "[source of media content]")
                print('\n\n')
        elif items:
            print(items)

    def _is_empty(self, lst: List[Dict[str, str]]) -> bool:
        result = True
        for i in lst:
            if lst[i] is not None:
                result = False
                break

        return result

    def _get_info(self, dict_: dict, attr: str, str_: str, end='\n'):
        """получить строку с данными из словаря"""
        x = dict_.get(attr)
        if x:
            print(f'{str_}: {x}', end=end)


class JSONViewHandler(AbstractViewHandler):
    """Process data as JSON."""

    def __init__(self, request: Dict[str, str]) -> None:
        """Initializer.

        :param request: A dictionary in which there may be a key
                        by which this handler will work.
        :type request: Dict[str, str]
        """
        self._request = request

    def show(self, data: dict) -> None:
        """Display the data as a JSON structure.

        :param data: Dictionary with data to be printed on the screen.
        :type data: dict
        """
        log.debug("Start outputting news in json format.")
        if self._request.get('json'):
            print(dumps(data, indent=3, ensure_ascii=False))
        else:
            super().show(data)
