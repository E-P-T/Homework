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
        file.touch(exist_ok=True)
