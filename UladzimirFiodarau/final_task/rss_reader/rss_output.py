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
        :param date: date of news
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
        :param date: date of news
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
        """
        Method is used to take and save a dictionary with news and data of news if given for later processing and
        creating a file name with file extension for output while object of PdfConverter class is formed
        :param news_dict: a dictionary with news
        :param url: URL of rss-feed
        :param date: date of news

        """
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

    def convert(self):
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
        PdfConverter.print_cell(pdf, tab=36, text=news.get('feed_title', 'No title'), length=53, line_length=164)
        pdf.cell(200, 2, ln=1, align='L')
        PdfConverter.print_cell(pdf, tab=36, text=news.get('feed_description', 'No additional description'), length=53,
                                line_length=164)
        pdf.cell(200, 2, ln=1, align='L')
        feed_link = news.get('feed_link', '')
        PdfConverter.print_cell(pdf, tab=36, text=feed_link, link=feed_link, length=53, line_length=164)
        pdf.cell(200, 5, txt="=" * 65, ln=1, align='L')
        # 'tdqm' package is used to show user a progress bar while converting news (especially requesting images)
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
            news_desc = news["feed_items"][item].get("description", "No description provided")
            PdfConverter.print_cell(pdf, text=news_desc, length=75)
            # changing font and colour for printing links (news_link formed previously in news_title section)
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
        print(f'\nConversion successful.\nFile saved at {file_name}')


class HtmlConverter(RssConverter):
    """
    A class for converting news data to HTML format
    """
    def __init__(self, news_dict=None, url: str = '', date: str = ''):
        """
        Method is used to take and save a dictionary with news and data of news if given for later processing and
        creating a file name with file extension for output while object of PdfConverter class is formed
        :param news_dict: a dictionary with news
        :param url: URL of rss-feed
        :param date: date of news
        """
        RssConverter.__init__(self, news_dict, url, date)
        self.file_name = self.file_name + '.html'

    def convert(self):
        """
        method converts a dictionary of news into a html file saved in 'output' directory which is formed in script
        directory (by default script directory is the 'rss_reader' directory in root directory 'final_task')
        It forms HTML document structure in a list and then writes list items to a file.
        'tdqm' package is used to show user a progress bar
        :return: None
        """
        news = self.news_dict
        # We will form HTML document structure in a list, starting with head
        html_buffer = ['<!DOCTYPE html>',
                       '<html>',
                       '<head><meta charset="utf-8"><title>News gathered by rss_reader</title></head>',
                       ]
        # forming Feed info block
        html_buffer.append(f'<h1 style="text-align:left">{"=" * 83}</h1>')
        feed_image = 'https://www.ict4dconference.org/wp-content/uploads/2020/10/rss-feed-logo.png'
        if 'feed_media' in news:
            if 'type' not in news['feed_media'] or news['feed_media']['type'].startswith('image'):
                feed_image = news['feed_media']['url']
        feed_title = news.get('feed_title', 'No title')
        html_buffer.append(f'<img src="{feed_image}" alt="Logo" width="120" height="60" style="float:left">'
                           f'<h1 style = "margin-left: 130px">{feed_title}</h1>')
        feed_desc = news.get('feed_description', 'No additional description')
        html_buffer.append(f'<h2 style = "margin-left: 130px">{feed_desc}</h2>')
        feed_link = news.get('feed_link', '')
        html_buffer.append(f'<h3 style = "margin-left: 130px"><a href={feed_link}>{feed_link}</a></h3>')
        html_buffer.append(f'<h1 style="text-align:left">{"=" * 83}</h1>')
        # 'tdqm' package is used to show user a progress bar while converting news
        for item in tqdm(sorted(news['feed_items'], reverse=True)):
            news_title = news["feed_items"][item].get("title", "No title provided")
            # checking for media and its type for forming the document
            news_media = None
            news_image = None
            if 'media' in news["feed_items"][item] and 'url' in news["feed_items"][item]['media']:
                media = news["feed_items"][item]['media']
                news_media = media['url']  # We will use a link to media later in script
                if 'type' not in media or media['type'].startswith('image'):
                    news_image = media['url']
            tab = 330 if news_image else 0
            # printing image if found and title
            if news_image:
                html_buffer.append(f'<img src="{news_image}" alt="Image" width="320" height="200" style="float:left">'
                                   f'<h3 style = "margin-left: {tab}px">{news_title}</h3>')
            else:
                html_buffer.append(f'<h3 style = "margin-left: 0px">{news_title}</h3>')
            # printing publication date
            news_date = f'Publication date: {news["feed_items"][item].get("pubDate", "No publication date provided")}'
            html_buffer.append(f'<p style = "margin-left: {tab}px">{news_date}</p>')
            # printing description
            news_desc = news["feed_items"][item].get("description", "No description provided")
            html_buffer.append(f'<p style = "margin-left: {tab}px">{news_desc}</p><br>')
            # printing news link and media link
            news_link = news["feed_items"][item].get("link", "No link provided")
            if news_link != "No link provided":
                html_buffer.append(f'<p style = "margin-left: {tab}px"><a href={news_link}>{news_link}</a><p>')
            else:
                html_buffer.append(f'<p style = "margin-left: {tab}px"><{news_link}<p>')
            if news_media:
                html_buffer.append(f'<p style = "margin-left: {tab}px"><a href={news_media}>Media link: {news_media}'
                                   f'</a><p>')
            # finishing news item block with printing a separator between news
            html_buffer.append(f'<p style="text-align:left">{"-" * 280}</p>')
        # closing previously opened tags
        html_buffer.append('</html>')
        # checking for output directory and saving html to file
        RssConverter.check_directory('/output/')
        file_name = script_dir + '/output/' + self.file_name
        with open(file_name, 'w', encoding='utf-8') as out:
            for line in html_buffer:
                print(line, file=out)
        print(f'\nConversion successful.\nFile saved at {file_name}')


if __name__ == '__main__':
    pass
    # with open(script_dir + '/test_examples/dict_v3.txt', encoding='utf-8') as file:
    #     dictionary = eval(file.read())
    #     html = HtmlConverter(dictionary)
    #     html.convert_to_html()
