import datetime
import os
import textwrap
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import fpdf
from tqdm import tqdm

script_dir = os.path.dirname(__file__)


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
    def check_directory(directory: str):
        """
        Method checks if passed directory exists in script_root directory and creates it if it doesn't
        :param directory: directory name to check
        :return: None
        """
        if not os.path.exists(script_dir + directory):
            os.mkdir(script_dir + directory)


class PdfConverter(RssConverter):
    """
    A class for converting news data to PDF format
    If date is specified only cached sources are used without getting information from URL
    """
    def __init__(self, news_dict=None, url: str = '', date: str = ''):
        RssConverter.__init__(self, news_dict, url, date)
        self.file_name = self.file_name + '.pdf'

    @staticmethod
    def print_cell(obj: fpdf.FPDF, text: str, length: int, tab: int = 1, link=None,
                   line_length: int = 200, line_height: int = 5, line_align: str = 'L'):
        """
        Method is used to split text into lines of set length and save them to pdf cells with given parameters.
        It uses 'textwrap.wrap' for splitting text and method of fpdf.FPDF class instances 'cell' for making
        a pdf cell output. If user requires additional information - it can be found in used methods descriptions.

        :param obj: pdf object, must be an instance of fpdf.FPDF class
        :param text: text to split
        :param length: length of splitting in printing symbols
        :param tab: tabulation of text from the beginning of pdf cell if required
        :param link: URL to connect with text if required
        :param line_length: length of pdf cell
        :param line_height: width of pdf cell
        :param line_align: alignment of text in pdf cell ('L', 'R', 'C')
        :return: None
        """
        lines = textwrap.wrap(text, length, break_long_words=True) if text else ''
        for line in lines:
            obj.cell(tab)
            obj.cell(w=line_length, h=line_height, txt=line, ln=1, align=line_align, link=link)

    def pdf_output(self):
        """
        method converts a dictionary of news into a pdf file saved in 'output' directory which is formed in script
        directory (by default script directory is the 'rss_reader' directory in root directory 'final_task')
        If date is specified only cached sources are used without getting information from URL
        :return: None
        """
        news = self.news_dict
        pdf = fpdf.FPDF()
        pdf.add_font("DejaVuMono", style="", fname=script_dir + "/fonts/" + "DejaVuSansMono.ttf", uni=True)
        pdf.add_font("DejaVuMono", style="B", fname=script_dir + "/fonts/" + "DejaVuSansMono-Bold.ttf", uni=True)
        pdf.add_font("DejaVuMono", style="I", fname=script_dir + "/fonts/" + "DejaVuSansMono-Oblique.ttf", uni=True)
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=10)
        #  setting a separate font for header block
        pdf.set_font('DejaVuMono', 'B', 14)
        pdf.cell(200, 5, txt="=" * 65, ln=1, align='L')
        # trying to use feed logo if it is saved and can be accessed. If not - will use a standard rss logo
        feed_image = script_dir + '/rss-header.png'
        if self.date:
            pdf.image(feed_image, 12, 14, 33, 15)
        else:
            if 'feed_media' in news:
                if 'type' not in news['feed_media'] or news['feed_media']['type'].startswith('image'):
                    try:
                        pdf.image(news['feed_media']['url'], 12, 14, 33, 15)
                    except Exception:
                        pdf.image(feed_image, 12, 14, 33, 15)
            else:
                pdf.image(feed_image, 12, 14, 33, 15)
        # printing Feed header
        PdfConverter.print_cell(pdf, tab=36, text=news['feed_title'], length=53, line_length=164)
        pdf.cell(200, 2, ln=1, align='L')
        PdfConverter.print_cell(pdf, tab=36, text=news['feed_description'], length=53, line_length=164)
        pdf.cell(200, 2, ln=1, align='L')
        PdfConverter.print_cell(pdf, tab=36, text=f"Feed link: {news['feed_link']}", link=news['feed_link'], length=53,
                                line_length=164)
        pdf.cell(200, 5, txt="=" * 65, ln=1, align='L')
        # going into a for loop to iterate over gathered/cached news and form a standardised print
        for num, item in enumerate(tqdm(sorted(news['feed_items'], reverse=True))):
            pdf.set_font('DejaVuMono', 'B', 14)
            news_title = news["feed_items"][item].get("title", "No title provided")
            news_link = news["feed_items"][item].get("link", "No link provided")  # will also be used later
            PdfConverter.print_cell(pdf, text=news_title, length=65, link=news_link)  # link to make Title clickable
            pdf.cell(200, 1, ln=1, align='L')
            pdf.set_font('DejaVuMono', '', 12)
            news_date = f'Publication date: {news["feed_items"][item].get("pubDate", "No publication date provided")}'
            PdfConverter.print_cell(pdf, text=news_date, length=65)
            pdf.cell(200, 4, ln=1, align='L')
            # as fpdf.FPDF sometimes fails to get an image from URL we try to get it through Request
            news_media = ''
            if 'media' in news["feed_items"][item] and 'url' in news["feed_items"][item]['media']:
                media = news["feed_items"][item]['media']
                news_media = media['url']  # We will use a link to media later in script
                if 'type' not in media or media['type'].startswith('image'):
                    if not self.date:
                        temp_name = script_dir + '/temp/' + str(num) + '_' + "temp.jpg"
                        try:
                            with urlopen(Request(news_media), timeout=3) as response:
                                RssConverter.check_directory('/temp/')
                                with open(temp_name, "wb") as temp:
                                    temp.write(response.read())
                                    pdf.image(temp_name, w=60)
                        except Exception:  # if script could not get the image or format not supported, we supress
                            pass           # Exception and will use a link to media later in script
                        finally:
                            if os.path.exists(temp_name):
                                os.remove(temp_name)
            # Printing news description
            news_desc = news["feed_items"][item].get("description", None)
            if news_desc is None:
                news_desc = "No description provided"
            PdfConverter.print_cell(pdf, text=news_desc, length=75)
            # changing font and colour and printing links (news_link formed previously in news_title section)
            pdf.set_font('DejaVuMono', 'I', 9)
            pdf.cell(200, 4, ln=1, align='L')
            pdf.set_text_color(0, 0, 255)
            PdfConverter.print_cell(pdf, text='Link: ' + news_link, length=100, link=news_link, line_height=4)
            if news_media:
                pdf.cell(200, 2, ln=1, align='L')
                PdfConverter.print_cell(pdf, text=f'Media link: {news_media}', length=100, link=news_media,
                                        line_height=4)
            pdf.set_font('DejaVuMono', '', 12)
            pdf.set_text_color(0, 0, 0)
            # finishing news item block with printing a separator between news
            pdf.cell(200, 5, txt="-" * 76, ln=1, align='L')
        # checking for output directory and saving pdf to file
        RssConverter.check_directory('/output/')
        file_name = script_dir + '/output/' + self.file_name
        pdf.output(file_name)


if __name__ == '__main__':
    pass
