
from requests import Response, get


from rss_reader.interfaces.icrawler.icrawler import ICrawler
from .exceptions import BadURLError


class SuperCrawler(ICrawler):
    def __init__(self, url: str) -> None:
        self._url = url

    def get_data(self) -> bytes:
        pass

    def _get_response(self) -> Response:
        req = get(self._url)
        return req

    def _get_content(self, req: Response) -> bytes:
        pass

    def _get_status(self, req: Response) -> int:
        pass
