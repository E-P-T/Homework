

from typing import Optional
from rss_reader.interfaces.iviewer.iviewer import IViewHandler


class AbstractViewHandler(IViewHandler):
    _next_handler: Optional[IViewHandler] = None

    def set_next(self, handler: IViewHandler) -> IViewHandler:
        self._next_handler = handler
        return handler
