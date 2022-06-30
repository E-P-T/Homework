

from typing import Dict, List
from io import BytesIO

from fpdf import FPDF
from PIL import Image
import requests


from ..saver import AbstractSaveHandler


class PDFSaveHandler(AbstractSaveHandler):
    def __init__(self, request: Dict[str, str], folder: str) -> None:
        self._request = request
        self._folder = folder

    def save(self, data: List[dict]) -> None:
        file = self._request.get('to_pdf')
        if file:
            pdf = FPDF()
            pdf.set_font("Arial", size=14)

            y = 10
            imgs = []

            for i in data:
                pdf.add_page()

                pdf.cell(150, 10, txt=i.get(
                    'title_web_resource'), ln=1, align='L')

                pdf.cell(150, 10, txt='Link to feed.', ln=1,
                         align='L', link=i.get('link'))

                for key, item in enumerate(i.get('items')):
                    pass
        else:
            super().save(data)
