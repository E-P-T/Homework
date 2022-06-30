"""Contains a specific HTML file handler."""

from typing import Dict, List


from rss_reader.pathfile.pathfile import PathFile
from ..saver import AbstractSaveHandler
from .strategies import StrategySaveHTML


class HTMLSaveHandler(AbstractSaveHandler):
    """Saves the data to an HTML file.

    Processed in a chain.
    """
    def __init__(self, request: Dict[str, str],
                 strategy: StrategySaveHTML) -> None:
        """Initializer.

        :param request: A dictionary in which there may be a key
                        by which this handler will work.
        :type request: Dict[str, str]
        :param strategy: The strategy by which the data file will be farmed.
        :type strategy: StrategySaveHTML
        """

        self._request = request
        self._strategy = strategy

    def save(self, data: List[dict]) -> None:
        """Save data.

        :param data: Dictionary with data to save.
        :type data: List[dict]
        :raises FileExistsError: An error occurs when the specified path
        does not exist.
        """

        file = self._request.get('to_html')

        if file:
            html_ = self._strategy.prepare_html(data)
            exists_file = PathFile.exists_file(file)

            if exists_file:
                news_file = file + 'news.html'

                with open(news_file, "w", encoding='utf-8') as file_:
                    file_.write(html_)
            else:
                raise FileExistsError('The requested path does not exist.')

        else:
            super().save(data)
