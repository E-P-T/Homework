from loguru import logger
import json
from json2html import *


class Converter:
    """
    Convert from:   object to dict
                    json to dict
                    dict to json
                    json to HTML

    """

    def __init__(self, my_reader=None) -> None:
        self.my_reader = my_reader

    def to_dict(self) -> dict:
        logger.debug("Convert data to dictionary (debug)!")
        dict = {"name": self.my_reader.name,
                "size": self.my_reader.limit,
                "title": self.my_reader.title,
                "pubDate": self.my_reader.pubDate,
                "description": self.my_reader.clear_description,
                "link": self.my_reader.link}
        return dict

    def from_json(self) -> dict:
        logger.debug("Read data from json(debug)!")
        with open('data.json') as json_file:
            data = json.load(json_file)
            return data

    def to_JSON(self, dict=False) -> None:
        if not dict:
            dict = self.to_dict()
        logger.debug("Convert data to json (debug)!")
        with open('data.json', 'w+') as outfile:
            json.dump(dict, outfile, indent=4)

    def to_HTML(self):
        with open("data.json") as f:
            d = json.load(f)
            scanOutput = json2html.convert(json=d)
            htmlReportFile = "output.html"
            with open(htmlReportFile, 'w') as htmlfile:
                htmlfile.write(str(scanOutput))
                print("Data save in output.html")
