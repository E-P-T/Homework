

from typing import List

from ..saver import AbstractSaveHandler


class HTMLSaveHandler(AbstractSaveHandler):
    def __init__(self, request: Dict[str, str]) -> None:
        """Initializer.

        :param request: A dictionary in which there may be a key
                        by which this handler will work.
        :type request: Dict[str, str]
        """
        self._request = request

    def save(self, data: List[dict], file: str) -> None:
        pass
