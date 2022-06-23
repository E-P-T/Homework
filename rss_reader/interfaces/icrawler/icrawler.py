
from abc import ABC, abstractmethod


class ICrawler(ABC):

    @abstractmethod
    def get_data(self) -> bytes:
        """Get the content of the requested page.

        :return: Returns the result as a byte string.
        :rtype: bytes
        """
        pass
