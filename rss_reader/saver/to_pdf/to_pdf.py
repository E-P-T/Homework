

from typing import Dict, List

from fpdf import FPDF
from PIL import Image

from ..saver import AbstractSaveHandler


class PDFSaveHandler(AbstractSaveHandler):
    def __init__(self, request: Dict[str, str], folder: str) -> None:
        self._request = request
        self._folder = folder

    def save(self, data: List[dict]) -> None:
        file = self._request.get('to_pdf')
        if file:
        else:
            super().save(data)
