import os.path

from fpdf import FPDF, HTMLMixin

from rss_parse.exceptions.exceptions import ProcessingException
from rss_parse.processor.rss_processor import RssProcessor
from rss_parse.utils.formatting_utils import format_date_pretty


class PdfWithHtml(FPDF, HTMLMixin):
    pass


class RssToPdfConverter(RssProcessor):
    """
    Converts RSS to a PDF Format and saves it in a file
    """
    PDF_FILE_NAME = "rss_feed.pdf"

    def __init__(self, rss_feed, dir, mc=None):
        super().__init__(rss_feed, mc=mc)
        self.__dir = dir
        if not os.path.exists(dir):
            raise ProcessingException(f"Path {dir} doesn't exist")

    def process(self):
        pdf = PdfWithHtml()
        pdf.add_font('OpenSans', '', 'OpenSans.ttf', uni=True)
        pdf.set_font('OpenSans', size=12)
        pdf.add_page()

        items = self.rss_feed.rss_items
        for index, item in enumerate(items):
            pdf.multi_cell(w=0, h=5, txt=item.title, new_x="LEFT")
            pdf.multi_cell(w=0, h=5, txt="", new_x="LEFT")
            pdf.multi_cell(w=0, h=5, txt=f"Date: {format_date_pretty(item.publication_date)}", new_x="LEFT")
            pdf.multi_cell(w=0, h=5, txt="", new_x="LEFT")
            pdf.set_text_color(0, 0, 255)
            pdf.multi_cell(w=0, h=5, txt=item.link, new_x="LEFT")
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(w=0, h=5, txt="", new_x="LEFT")
            try:
                if item.image_url:
                    pdf.image(item.image_url, h=70)
                    pdf.multi_cell(w=0, h=5, txt="", new_x="LEFT")
            except:
                pass

            if item.description:
                pdf.write_html(item.description)

            if index != len(items) - 1:
                pdf.add_page()

        pdf.output(os.path.join(self.__dir, RssToPdfConverter.PDF_FILE_NAME))
