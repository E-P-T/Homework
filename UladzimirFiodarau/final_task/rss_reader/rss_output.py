import datetime
import os
import textwrap
import urllib.request
from urllib.parse import urlparse
import fpdf

fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__), 'fonts'))
script_root = os.path.dirname(__file__)


class RssConverter:
    """
    A base class for all data converters, which is used for keeping universal methods for all converters
    """
    def __init__(self, news_dict=None, url: str = '', date: str = ''):
        """
        Method is used to take and save a dictionary with news for processing and a file name for output while object
        of RssConverter class is formed
        :param news_dict: a dictionary with news
        :param url: URL of rss-feed
        :param date: date of news if given
        """
        self.url = url
        self.date = date
        self.file_name = self.create_file_name(url, date)
        self.news_dict = news_dict

    @staticmethod
    def create_file_name(url: str = '', date: str = ''):
        """
        Method is used to create unique filenames for saving converted news to file. It uses URL, if given, to get its
        network location domain name, and date, if given, to combine unique filename for output.
        :param url: URL of rss-feed
        :param date: date of news if given
        :return: a name of the file
        """
        file_date = 'cached_news_' + date.replace(':', '_') if date else f'{datetime.datetime.now():%Y_%m_%d}'
        file_domain = urlparse(url).netloc.split('.')[-2] + '_' if url else ''
        file_name = file_domain + file_date
        return file_name

    @staticmethod
    def check_output_directory():
        if not os.path.exists(script_root + '/output/'):
            os.mkdir(script_root + '/output/')


class PdfConverter(RssConverter):
    """
    A class for converting news data to PDF format
    """
    def __init__(self, news_dict=None, url: str = '', date: str = ''):
        RssConverter.__init__(self, news_dict, url, date)
        self.file_name = self.file_name + '.pdf'

    @staticmethod
    def print_cell(obj: fpdf.FPDF, text: str, length: int, tab: int = 1, link=None,
                   line_length: int = 200, line_height: int = 5, line_align: str = 'L'):
        lines = textwrap.wrap(text, length, break_long_words=True)
        for line in lines:
            obj.cell(tab)
            obj.cell(w=line_length, h=line_height, txt=line, ln=1, align=line_align, link=link)

    def pdf_output(self):
        news = self.news_dict
        pdf = fpdf.FPDF()
        pdf.add_font("DejaVuMono", style="", fname="DejaVuSansMono.ttf", uni=True)
        pdf.add_font("DejaVuMono", style="B", fname="DejaVuSansMono-Bold.ttf", uni=True)
        pdf.add_font("DejaVuMono", style="I", fname="DejaVuSansMono-Oblique.ttf", uni=True)
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=10)

        pdf.set_font('DejaVuMono', 'B', 14)
        pdf.cell(200, 5, txt="=" * 65, ln=1, align='L')
        if 'feed_media' in news:
            if 'type' not in news['feed_media'] or news['feed_media']['type'].startswith('image'):
                try:
                    pdf.image(news['feed_media']['url'], 12, 14, 33, 15)
                except Exception:  # if no image from feed or image of incorrect type - use a standard
                    feed_image = script_root + '/rss-header.png'
                    pdf.image(feed_image, 12, 14, 33, 15)
        PdfConverter.print_cell(pdf, tab=36, text=f"Feed_title: {news['feed_title']}",
                                length=53, line_length=164)
        PdfConverter.print_cell(pdf, tab=36, text=f"Feed_description: {news['feed_description']}",
                                length=53, line_length=164)
        PdfConverter.print_cell(pdf, tab=36, text=f"Feed_link: {news['feed_link']}", link=news['feed_link'],
                                length=53, line_length=164)
        pdf.cell(200, 5, txt="=" * 65, ln=1, align='L')

        for num, item in enumerate(sorted(news['feed_items'], reverse=True)):
            pdf.set_font('DejaVuMono', 'B', 14)
            news_title = news["feed_items"][item].get("title", "No title provided")
            PdfConverter.print_cell(pdf, text=news_title, length=65)
            pdf.cell(200, 1, ln=1, align='L')
            pdf.set_font('DejaVuMono', '', 12)
            news_date = f'Publication date: {news["feed_items"][item].get("pubDate", "No publication date provided")}'
            PdfConverter.print_cell(pdf, text=news_date, length=65)
            pdf.cell(200, 4, ln=1, align='L')

            news_media = ''
            if 'media' in news["feed_items"][item]:
                media = news["feed_items"][item]['media']
                if 'type' not in media or media['type'].startswith('image'):
                    try:
                        with urllib.request.urlopen(media['url']) as response:
                            temp_name = str(num) + '_' + "temp.jpg"
                            with open(temp_name, "wb") as temp:
                                temp.write(response.read())
                                pdf.image(temp_name, w=60)
                            if os.path.exists(temp_name):
                                os.remove(temp_name)
                    except Exception:  # if image format not supported, use URL to print it later
                        news_media = media['url']
                if 'type' in media and not media['type'].startswith('image'):
                    news_media = media['url']

            news_desc = news["feed_items"][item].get("description", None)
            if news_desc is None:
                news_desc = "No description provided"
            PdfConverter.print_cell(pdf, text=news_desc, length=75)
            news_link = news["feed_items"][item].get("link", "No link provided")
            pdf.set_font('DejaVuMono', 'I', 9)
            pdf.cell(200, 4, ln=1, align='L')
            pdf.set_text_color(0, 0, 255)
            PdfConverter.print_cell(pdf, text='Link: ' + news_link, length=100,
                                    link=news_link, line_height=4)
            if news_media:
                pdf.cell(200, 2, ln=1, align='L')
                PdfConverter.print_cell(pdf, text=f'Media link: {news_media}', length=100,
                                        link=news_media, line_height=4)
            pdf.set_font('DejaVuMono', '', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(200, 5, txt="-" * 76, ln=1, align='L')

        RssConverter.check_output_directory()
        file_name = script_root + '/output/' + self.file_name
        pdf.output(file_name, 'F')


if __name__ == '__main__':
    pass