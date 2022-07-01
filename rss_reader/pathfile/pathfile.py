"""This module contains objects that work with the file system of the OS."""


from pathlib import Path

from rss_reader.interfaces.ipathfile.ipathfile import ICreateFile


class PathFile(ICreateFile):
    """Works with the file system of the operating system."""

    def create_file(self, file: str) -> None:
        """Create file.

        :param file: File name.
        :type file: str
        """
        file = Path(file)
        Path.mkdir(file.parent, parents=True, exist_ok=True)
        file.touch(exist_ok=True)

    def home(self) -> None:
        """Return a new path pointing to the user's home directory."""
        return Path.home()

    @staticmethod
    def exists_file(file: str) -> bool:
        path = Path(file)
        return path.exists()

    @staticmethod
    def unlink(file: str) -> None:
        Path(file).unlink()
