"""This class generate files for news item."""
import dominate.tags as tag

from dominate import document
from fpdf import FPDF
from os import path, getcwd
from reader.exceptions import PATHError


class Convert:
    @classmethod
    def converter(cls, to_html, to_pdf, news_item):
        """For the given argument generate pdf and/or html files"""
        if to_html:
            cls.create_html_file(news_item)
        if to_pdf:
            cls.create_pdf_file(news_item)

    @classmethod
    def create_html_file(cls, all_news):
        """Creates and fills in the HTML file with the required data."""
        path_to_html = path.join(getcwd(), 'RSS_NEWS.html')
        html_doc = document(title='RSS NEWS')
        with html_doc:
            tag.h1("RSS News")
        for news in all_news:
            html_file = cls.convert_news_in_html(news, html_doc)
            try:
                with open(path_to_html, 'w') as file:
                    file.write(str(html_file))
            except FileNotFoundError:
                raise PATHError
        print(f"Download HTML file with the required news to the {path_to_html}")

    @staticmethod
    def convert_news_in_html(news, html_file):
        """Convert news to HTML format"""

        with html_file:
            with tag.div():
                tag.h2(news.get_title())
                tag.p(news.get_date())
                tag.br()
                tag.a("Read the full article", href=news.get_link())
                tag.br()

                if news.get_image() is not None:
                    tag.img(src=news.get_image(), width=600)
                tag.p(news.get_news())
                tag.br()

        return html_file

    @classmethod
    def create_pdf_file(cls, all_news):
        """Creates and fills in the PDF file with the required data"""
        path_to_pdf = path.join(getcwd(), 'RSS_NEWS.pdf')
        pdf = FPDF()
        pdf.add_page()

        pdf.add_font('DejaVu', fname=path.join(getcwd(), 'font', 'DejaVuSans.ttf'), uni=True)
        pdf.set_font('DejaVu', size=40)
        pdf.set_text_color(100, 100, 50)
        pdf.cell(200, 20, txt='RSS News', ln=True, align='C')

        for news in all_news:
            cls.convert_news_in_pdf(pdf, news)
        pdf.output(path_to_pdf)
        print(f"Download PDF file with the required news to the {path_to_pdf}")

    @staticmethod
    def convert_news_in_pdf(pdf, news):
        """Convert news to PDF format"""

        pdf.set_font('DejaVu', size=16)
        pdf.set_text_color(0, 150, 150)
        pdf.multi_cell(200, 5, txt=news.get_title(), ln=True)

        pdf.set_font('DejaVu', '', 8)
        pdf.set_text_color(0, 150, 250)
        pdf.cell(100, 5, txt=news.get_date(), ln=True)

        pdf.set_font('DejaVu', 'U', 10)
        pdf.set_text_color(0, 50, 200)
        pdf.cell(200, 10, txt="Read the full article", link=news.get_link(), ln=True)

        if news.get_image() is not None:
            pdf.set_font('DejaVu', '', 16)
            pdf.image(w=120, h=80, name=news.get_image())

        pdf.set_font('DejaVu', '', 8)
        pdf.set_text_color(0, 150, 150)
        pdf.multi_cell(400, 5, txt=news.get_news(), ln=True)
        pdf.ln(5)
