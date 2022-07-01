"""This module implements specific strategies that form html files."""


from typing import List

import pathlib
from jinja2 import FileSystemLoader, Environment

from rss_reader.interfaces.isaver.istrategies import StrategySaveHTML


class SuperStrategySaveHTML(StrategySaveHTML):
    """Implements the simplest strategy for generating an HTML file."""

    def prepare_html(self, data: List[dict]) -> str:
        """Prepare html page.

        The operation of preparing a page according to a specific algorithm.
        Each specific strategy defines its own page creation logic.

        :param data: Initial data intended for display on the html page.
        :type data: List[dict]
        :return: Generated html page according to a certain algorithm.
        :rtype: str
        """

        path_ = pathlib.Path(__file__).parent
        file_loader = FileSystemLoader(path_/'templates')
        env = Environment(loader=file_loader)
        template_ = env.get_template('main.html')
        html_ = template_.render(data=data)

        return html_
