import os.path

from rss_parse.exceptions.exceptions import ProcessingException
from rss_parse.processor.rss_processor import RssProcessor
from rss_parse.utils.formatting_utils import format_date_pretty


class RssToHtmlConverter(RssProcessor):
    """
    Converts RSS to an HTML Format and saves it in a file
    """
    HTML_FILE_NAME = "rss_feed.html"

    def __init__(self, rss_feed, dir, mc=None):
        super().__init__(rss_feed, mc=mc)
        self.__dir = dir
        if not os.path.exists(dir):
            raise ProcessingException(f"Path {dir} doesn't exist")

    def process(self):
        html_res = self.__convert_to_html()
        with open(os.path.join(self.__dir, RssToHtmlConverter.HTML_FILE_NAME), "w", encoding="UTF-8") as f:
            f.write(html_res)

    def __convert_to_html(self):
        html_res = (
            '<html>'
            '<head>'
            '<meta http-equiv="Content-Type" content="text/html;charset=utf-8">'
            '<title>RSS Feed</title>'
            '</head>'
            '<body>'
            '<h1>RSS Feed</h1>'
        )

        for item in self.rss_feed.rss_items:
            html_res += '<div>'
            html_res += f'<h2>{item.title}</h2>'
            html_res += f'<p>{format_date_pretty(item.publication_date)}</p>'
            html_res += f'<p><a href={item.link}>Link</a></p>'
            if item.image_url:
                html_res += f'<div><img src="{item.image_url}" width="600" height="400"></div>'

            if item.description:
                html_res += f'<p>{item.description}</p>'

            html_res += '</div><br><br>'
        html_res += '</body></html>'

        return html_res
