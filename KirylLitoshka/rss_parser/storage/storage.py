"""
module with Storage class
base storage path and filename are specified in global scope
"""
import os
import pathlib
import shelve
import json
from datetime import datetime
from dateutil.parser import parse
from ..rss import RssFeedItem
from .exceptions import StorageError


STORAGE_PATH = os.path.join(pathlib.Path(__file__).parent, "local")
STORAGE_FILENAME = "local"


class Storage:
    def __init__(self, path=STORAGE_PATH, filename=STORAGE_FILENAME):
        self.path = path
        self.filename = filename
        self.date_format = "%a, %d %b %Y %H:%M:%S %z"

    @property
    def filepath(self):
        """
        Checks for self full path validity.
        :raise StorageError: if path is not valid
        :return str: full path of local storage
        """

        if not os.path.exists(self.path):
            raise StorageError("Storage path doesn't exist")
        return os.path.join(self.path, self.filename)

    def save(self, source: str, feed: list):
        """
        Saves rss feed items by source name.
        :param source: inputted source
        :param feed: list of rss items
        :return: None
        """
        with shelve.open(self.filepath, "c", writeback=True) as storage:
            if source not in storage:
                storage.setdefault(source, [])
            source_data = storage[source]
            for item in feed:
                if item.to_json() not in source_data:
                    source_data.append(item.to_json())
            storage[source] = source_data

    def load(self):
        """
        Loads all records from local storage and return its
        :return data: dict object where key is source (url)
        """
        data = {}
        with shelve.open(self.filepath, "c") as storage:
            for key in storage.keys():
                data[key] = [json.loads(item) for item in storage[key]]
        return data

    def load_by_date(self, date: str, source=None):
        load_data = self.load()
        date = datetime.strptime(date, "%Y%m%d").date()
        result = []
        if source:
            load_data = {k: v for k, v in load_data.items() if k == source}
        for key in load_data:
            for item in load_data[key]:
                if item["date"] is None:
                    continue
                item_date = parse(item["date"]).date()
                if item_date == date:
                    result.append(item)
        if not result:
            raise StorageError("Data not found")
        return [RssFeedItem(item) for item in result]
