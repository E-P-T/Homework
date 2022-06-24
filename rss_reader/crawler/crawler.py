
from requests import Response, get


from rss_reader.interfaces.icrawler.icrawler import ICrawler
from .exceptions import BadURLError


class SuperCrawler(ICrawler):
    def __init__(self, url: str) -> None:
        self._url = url

    def get_data(self) -> bytes:
        r = self._get_response()
        status = self._get_status(r)

    def _get_response(self) -> Response:
        """Get the server's response to an HTTP request.

        :raises BadURLError: If the url is wrong.
        :return: Contains a server's response to an HTTP request.
        :rtype: Response
        """
        try:
            req = get(self._url)
        except ConnectionError as e:
            raise BadURLError(self._url) from e
        return req

    def _get_content(self, req: Response) -> bytes:
        """Get the content of the Response object.

        :param req: Contains a server's response.
        :type req: Response
        :return: Content of the response, in bytes.
        :rtype: bytes
        """
        return req.content

    def _get_status(self, req: Response) -> int:
        """Get status code.

        :param req: Contains a server's response.
        :type req: Response
        :return: Status code.
        :rtype: int
        """
        return req.status_code
