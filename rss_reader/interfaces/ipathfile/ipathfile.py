"""This module contains a set of interfaces for the pathfile package."""


from abc import abstractmethod, ABC


class ICreateFile(ABC):
    """A interface for creating files."""

    @abstractmethod
    def create_file(self, file: str) -> None:
        """Create file.

        :param file: File name.
        :type file: str
        """
        pass
