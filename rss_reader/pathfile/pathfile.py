
from pathlib import Path

from rss_reader.interfaces.ipathfile.ipathfile import ICreateFile


class PathFile(ICreateFile):
    def create_file(self, file: str) -> None:
        file = Path(file)
        file.touch(exist_ok=True)
