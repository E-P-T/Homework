import base64
import io
import json
import re
from pathlib import Path
from typing import Union
from urllib.request import urlopen
from xml.etree.ElementTree import Element, parse as parse_xml

from PIL import Image
from colorama import Fore


class UtilException(Exception):
    def __init__(self, message):
        self.message = message


class Util:
    indent = '  '
    cached_file = Path(__file__).parent.parent.joinpath('cached.json')

    @classmethod
    def colorize(cls, message: str, color: str, back_color: str = None) -> str:
        message = color + message + Fore.RESET
        if back_color is not None:
            message = Fore.RESET + message + back_color
        return message

    @classmethod
    def to_element(cls, url: str) -> Element:
        with urlopen(url) as content:
            return parse_xml(content).getroot().find('channel')

    @classmethod
    def to_json(cls, obj: object) -> str:
        string = json.dumps(obj, indent=Util.indent, default=cls.safe_vars)
        return string

    @classmethod
    def safe_vars(cls, obj: object) -> Union[dict, str]:
        try:
            return vars(obj)
        except:
            return str(obj)

    @classmethod
    def vars_to_string(cls, obj: object):
        items = []
        for key, value in vars(obj).items():
            if isinstance(value, list):
                continue
            items.append(f'{key.capitalize()}: {value}')

        return '\n'.join(items)

    @classmethod
    def make_indent(cls, string: str):
        return re.sub(
            '^', cls.indent, string,
            flags=re.MULTILINE
        )

    @classmethod
    def get_cached(cls) -> str:
        content: str
        try:
            with open(cls.cached_file, 'r') as file:
                content = file.read()
        except:
            content = ''

        return content

    @classmethod
    def save_cache(cls, content: str) -> None:
        with open(cls.cached_file, 'w+') as file:
            file.write(content)

    @classmethod
    def unique(cls, items: list) -> list:
        unique = []
        for item in items:
            if item in unique:
                continue
            unique.append(item)

        return unique

    @classmethod
    def save(cls, content: str, path: str):
        with open(path, 'w+') as file:
            file.write(content)

    @classmethod
    def to_base64(cls, url: str) -> str:
        with urlopen(url) as content:
            with io.BytesIO(content.read()) as buf:
                with io.BytesIO() as image_buf:
                    with Image.open(buf) as image:
                        image.thumbnail((500, 500), Image.ANTIALIAS)
                        image.save(image_buf, 'PNG')

                    return base64.b64encode(image_buf.getvalue()).decode()

    @classmethod
    def colorize_object(cls, string: str):
        main = Fore.CYAN
        key = Fore.YELLOW
        curly = Fore.WHITE
        square = Fore.WHITE
        string = Util.regex(r'[\[\]]', cls.colorize(r'\g<0>', square, main), string)
        string = Util.regex(r'[\{\}]', cls.colorize(r'\g<0>', curly, main), string)
        string = Util.regex(r'^ *(\"|\w)+:', cls.colorize(r'\g<0>', key, main), string)
        return string + Fore.RESET

    @classmethod
    def regex(cls, pattern: str, replace: str, string: str) -> str:
        return re.sub(pattern, replace, string, flags=re.MULTILINE)
