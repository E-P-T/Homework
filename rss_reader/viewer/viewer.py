

from typing import Optional
from rss_reader.interfaces.iviewer.iviewer import IViewHandler


class AbstractViewHandler(IViewHandler):
    _next_handler: Optional[IViewHandler] = None
