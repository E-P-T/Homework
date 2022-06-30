
from typing import List

import pathlib
from jinja2 import FileSystemLoader, Environment

from rss_reader.interfaces.isaver.istrategies import StrategySaveHTML


class SuperStrategySaveHTML(StrategySaveHTML):
    def prepare_html(self, data: List[dict]) -> str:
        path_ = pathlib.Path(__file__).parent
        file_loader = FileSystemLoader(path_/'templates')
        env = Environment(loader=file_loader)
        template_ = env.get_template('main.html')
        html_ = template_.render(data=data)

        return html_
