"""This module contains objects that receive data from the internet."""


from requests import Response, get, ConnectionError
from requests.exceptions import MissingSchema

from rss_reader.interfaces.icrawler.icrawler import ICrawler
from rss_reader.decorator.decorator import send_log_of_start_function
from .exceptions import BadURLError, FailStatusCodeError


class SuperCrawler(ICrawler):
    """A class to represent a crawler."""

    def __init__(self, url: str) -> None:
        """Initializer.

        :param url: URL of the requested web page.
        :type url: str
        """
        self._url = url

    @send_log_of_start_function
    def get_data(self) -> bytes:
        """Get the content of the requested page.

        :raises FailStatusCodeError: If status code is not equal to 200.
        :return: Page data.
        :rtype: bytes
        """

        r = self._get_response()
        status = self._get_status(r)
        if status == 200:
            return self._get_content(r)
        raise FailStatusCodeError(status)

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
        except MissingSchema as e:
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
