

from typing import Dict, List
from io import BytesIO

from fpdf import FPDF
from PIL import Image
import requests

from rss_reader.pathfile.pathfile import PathFile
from ..saver import AbstractSaveHandler


class PDFSaveHandler(AbstractSaveHandler):
    def __init__(self, request: Dict[str, str], folder: str) -> None:
        self._request = request
        self._folder = folder

    def convert_to_latin1(self, data: str) -> str:
        """Convert to latin1 encoding.

        :param data: Data to be converted.
        :type data: str
        :return: String in the new encoding.
        :rtype: str
        """
        data = data.encode('ascii', errors='ignore')
        return data.decode('latin1', errors='ignore')

    def save(self, data: List[dict]) -> None:
        """Save data to PDF.

        :param data: Dictionary with data to save.
        :type data: List[dict]
        :raises FileExistsError: An error occurs when the specified path
        does not exist.
        """
        file = self._request.get('to_pdf')
        if file:
            pdf = FPDF()
            pdf.set_font("Arial", size=14)

            y = 10
            imgs = []

            for i in data:
                pdf.add_page()

                title_ = i.get('title_web_resource')
                if title_:
                    title_ = self.convert_to_latin1(title_)
                    pdf.cell(150, 10, txt=title_, ln=1, align='L')

                link_feed = i.get('link')
                if link_feed:
                    pdf.cell(150, 10, txt='Link to feed.', ln=1,
                             align='L', link=link_feed)

                for key, item in enumerate(i.get('items')):
                    t = item.get('title')

                    if t:
                        t = self.convert_to_latin1(t)
                        pdf.cell(150, 10, txt=t, ln=1, align='L')

                    item_link = item.get('link')
                    if item_link:
                        pdf.cell(150, 10, txt='Link to news.', ln=1,
                                 align='L', link=item_link)

                    pd = item.get('pubDate')
                    if pd:
                        pdf.cell(150, 10, txt=pd, ln=1, align='L')

                    s = item.get('source')
                    if s:
                        s = self.convert_to_latin1(s)
                        pdf.cell(150, 10, txt=s, ln=1, align='L')

                    url_image = item.get("content").get("url")
                    if url_image:
                        resp = requests.get(url_image, stream=True)
                        img = Image.open(BytesIO(resp.content))
                        name_img = f'{self._folder}\\{key}.jpg'
                        imgs.append(name_img)

                        # create empty files.
                        PathFile().create_file(name_img)
                        img.save(name_img)

                        pdf.image(name_img, x=10, y=pdf.get_y(), w=40)
                        pdf.line(10, pdf.get_y()+60, 200, pdf.get_y()+60)
                        pdf.cell(150, pdf.get_y()+25-y, ln=1, align='L')
                        y = pdf.get_y()-25

            exists_file = PathFile.exists_file(file)
            if exists_file:
                pdf_file = file + 'news.pdf'
                pdf.output(pdf_file)
            else:
                raise FileExistsError('The requested path does not exist.')

            # del all images
            for i in imgs:
                PathFile.unlink(i)
        else:
            super().save(data)
