
from abc import abstractmethod, ABC


class ICreateFile(ABC):

    @abstractmethod
    def create_file(self, file: str) -> None:
        """Create file.

        :param file: File name.
        :type file: str
        """
        pass
