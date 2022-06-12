import contextlib
import json
import re
from urllib.request import urlopen
from xml.etree import ElementTree as ET

from xhtml2pdf import pisa

from .Color import Color


class Util:
    indent = 2

    @staticmethod
    def url_to_element(source: str) -> ET.Element:
        """
        Returns an ElementTree.Element from a URL.
        """
        with urlopen(source) as file:
            return ET.parse(file).getroot().find('channel')

    @staticmethod
    def to_json(obj: object) -> str:
        """
        Returns a JSON string from an object.
        """
        return json.dumps(
            obj, indent=Util.indent, default=lambda o:
            o.__dict__ if hasattr(o, '__dict__') else str(o)
        )

    @staticmethod
    def to_str(obj: object) -> str:
        """
        Returns a string from an object.
        """
        string = Util.to_json(obj)
        string = re.sub(r'^\s*[{}],?\s?', '', string, flags=re.MULTILINE)
        string = re.sub(r'^\s{' + str(Util.indent) + '}', '', string, flags=re.MULTILINE)
        string = re.sub(r'"(\w+)"', lambda match: match.group(1).capitalize(), string, flags=re.MULTILINE)
        string = re.sub(r'"(.+)",?', lambda match: match.group(1), string, flags=re.MULTILINE)
        string = re.sub(r'[\[\]]', '', string, flags=re.MULTILINE)
        return string.strip()

    @staticmethod
    def colorize(message: str, color: Color) -> str:
        """
        Returns a string with colorized text.
        """
        return f'{color.value}{message}{Color.END.value}'

    @staticmethod
    def html_to_pdf(html: str, path: str):
        """
        Converts an HTML file to a PDF file.
        """
        with open(path, 'w+b') as file:
            with contextlib.redirect_stdout(None):
                pisa.CreatePDF(html, file)
