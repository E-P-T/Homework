
from requests import Response


from rss_reader.interfaces.icrawler.icrawler import ICrawler


class SuperCrawler(ICrawler):
    def __init__(self, url: str) -> None:
        self._url = url

    def get_data(self) -> bytes:
        pass

    def _get_response(self) -> Response:
        pass

    def _get_content(self, req: Response) -> bytes:
        pass

    def _get_status(self, req: Response) -> int:
        pass
