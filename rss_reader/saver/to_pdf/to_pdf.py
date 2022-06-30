

from typing import Dict, List
from ..saver import AbstractSaveHandler


class PDFSaveHandler(AbstractSaveHandler):
    def __init__(self, request: Dict[str, str], folder: str) -> None:
        self._request = request
        self._folder = folder
    
    def save(self, data: List[dict]) -> None:
        pass
