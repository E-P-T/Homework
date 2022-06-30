"""
Module for Feed class

exports Feed class
"""

import json
import utils.config as config
from bs4 import BeautifulSoup
from link import Link
from utils.exceptions import ConvertJSONError


class Feed:
    """Class which describes normalized Feed object"""
    def __init__(self,
                 source_title: str,
                 source_url: str,
                 title: str,
                 date: str,
                 link: str,
                 content: str,
                 non_media_links: list[Link],
                 media_links: list[Link]
                 ):
        """
        The constructor of Feed class

        Args:
            source_title:       the title of source from where the feed was fetched
            title:              the title of the current feed
            date:               the date of publication of the current feed
            link:               the link where feed is stored
            content:            the content of the current feed
            non_media_links:    non-media links, that are used in the feed
            media_links:        media links, that are used in the feed
        """

        self.source_title = source_title
        self.source_url = source_url
        self.title = title
        self.date = date.replace("Z", "+00:00")
        self.link = link
        self.content = content
        self.non_media_links = non_media_links
        self.media_links = media_links

    def to_json(self):
        """
        The function for converting Feed object to JSON string

        Returns:
            JSON string

        Raises:
            ConvertJSONError
        """

        config.verbose_print("Converting feed to JSON format", "blue")
        try:
            return json.dumps(self, default=lambda o: o.__dict__, indent=4)
        except Exception as e:
            raise ConvertJSONError(f"Error when converting feed to JSON ({e})")

    def to_readable(self) -> str:
        """
        The function for converting Feed type object to readable string

        Returns:
            str: Readable string based on Feed object
        """

        config.verbose_print("Converting feed to readable format", "blue")
        all_links = self.non_media_links.copy()
        all_links.extend(self.media_links)
        formatted_links = ""
        for i in range(0, len(all_links)):
            formatted_links += f"[{i + 1}]: {str(all_links[i])}\n"
        if formatted_links == "":
            formatted_links = None

        content = BeautifulSoup(self.content, 'lxml')
        feed_links = content.find_all("a", href = True)

        for a in content.select("a"):
            anchor_index = next((i for i, item in enumerate(feed_links) if item["href"] == a["href"]), None)
            anchor_before = f"[link {anchor_index + 1}: "
            anchor_after = f"][{anchor_index + 1}]"
            a.insert_before(anchor_before)
            a.insert_after(anchor_after)
            a.unwrap()

        formatted_content = content.get_text()
        formatted_feed = \
            f"Feed: {self.source_title}\n\n" + \
            f"Title: {self.title}\n" + \
            f"Date: {self.date}\n" + \
            f"Link: {self.link}\n\n" + \
            f"{formatted_content}\n\n" + \
            f"Links:\n{formatted_links}\n\n"

        return formatted_feed

    @staticmethod
    def json_to_feed(json_feed: str):
        """
        The function for converting JSON of feed to Feed object

        Args:
            json_feed:  JSON string of feed

        Returns:
            Feed:       Feed object
        """

        converted_feed = json.loads(json_feed)
        non_media_links = list(map(lambda l: Link(l["href"], l["link_type"]), converted_feed["non_media_links"]))
        media_links = list(map(lambda l: Link(l["href"], l["link_type"]), converted_feed["media_links"]))

        return Feed(converted_feed["source_title"],
                    converted_feed["source_url"],
                    converted_feed["title"],
                    converted_feed["date"],
                    converted_feed["link"],
                    converted_feed["content"],
                    non_media_links,
                    media_links)
