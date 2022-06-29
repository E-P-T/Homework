import json
import logging
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class RSSException(Exception):
    def __init__(self, message, is_logged):
        super().__init__(message)
        self.is_logged = is_logged


class ElementType(Enum):
    """
    An Enum class to represent types of Elements.
    """
    TITLE = 'Title'
    PUB_DATE = 'Publish Date'
    LINK = 'Link'
    DESCRIPTION = 'Description'
    MEDIA = 'Media Link'


@dataclass
class Element:
    """
    A class which contains the type and the value of an Element.
    """
    type: ElementType
    value: Optional[str] = None

    @staticmethod
    def _get_media_link_type(url: str) -> str:
        logging.info(f'Classifying media link type for {url}')
        if url.split('.')[-1] in ('jpg', 'jpeg', 'png', 'gif'):
            return '(Image)'
        return '(Link)'

    def __repr__(self) -> str:
        if self.type == ElementType.MEDIA:
            return f'{self.value} {get_media_link_type(self.value)}'
        if self.value:
            return self.value
        return f'{self.type.value} was not found.'

    def __hash__(self):
        return hash(self.value)


@dataclass
class ElementCollection:
    """
    A collection class for Elements
    """
    type: ElementType
    elements: list[Element]

    def __len__(self) -> int:
        elem_coll_len = 0
        for el in self.elements:
            if el.value:
                elem_coll_len += 1
        return elem_coll_len

    def __bool__(self):
        return len(self) > 0

    def __repr__(self) -> str:
        if len(self) == 0:
            return f'{self.type.value} was not found.'
        repr_str = ''
        for element_index, element in enumerate(self.elements):
            repr_str += f'[{element_index + 1}]: {element}\n'
        return repr_str


@dataclass
class Item:
    """
    A class to represent an Item with its Elements.
    """
    title: Element
    date: Element
    link: Element
    description: Element
    media_links: ElementCollection

    @property
    def value(self) -> dict:
        """
        Get the value's of an Item's Elements in a form of a dictionary.
        :return: Item's value dictionary
        """
        return {'title': self.title.value,
                'content': {
                    'date': self.date.value,
                    'link': self.link.value,
                    'description': self.description.value,
                    'media': [media_link.value for media_link in self.media_links.elements if media_link.value]}
                }

    def __repr__(self) -> str:
        repr_str = (f'Title: {self.title}\n'
                    f'Date: {self.date}\n'
                    f'Link: {self.link}\n\n'
                    f'Description:\n{self.description}\n\n'
                    f'Media Links:\n{self.media_links}\n\n')

        return repr_str


@dataclass
class Feed:
    """
    A class to represent an RSS feed with its title and items.
    """
    title: str
    url: Optional[str]
    items: list[Item]

    def to_json(self):
        """
                This function returns a JSON object representation of an RSS feed with the following fields:
                    - feed_title: The title of the RSS feed.
                    - items: A list of parsed items from the RSS feed.

                :return: A representation of an RSS feed.
                """
        json_dict = {
            'title': self.title,
            'items': [item.value for item in self.items]
        }
        if self.url:
            json_dict['url'] = self.url
        logging.info('Retrieving results in JSON format')
        return json.dumps(json_dict, indent=2)

    def __repr__(self):
        repr_str = ''
        if not self.items:
            repr_str += 'There were no items to fetch.'
            return repr_str
        if self.url:
            repr_str += f'Feed URL: {self.url}\n'
        repr_str += f'Feed Title: {self.title}\n\n'
        for item in self.items:
            repr_str += repr(item)
        logging.info('Printing results to the user in regular format')
        return repr_str


@dataclass
class RSSCache:
    """
    A class to represent the RSS feed for caching and its methods.
    """
    rss_feeds: list[Feed]

    def append(self, new_feed: Feed):
        is_existing_title = False
        for feed in self.rss_feeds:
            if new_feed.title == feed.title:
                unique_items = self._get_titles_set(feed.items)
                diff_titles = self._get_titles_set(new_feed.items).difference(unique_items)
                feed.items += [current_item for current_item in new_feed.items
                               if current_item.title in diff_titles]
                is_existing_title = True
        if not is_existing_title:
            self.rss_feeds.append(new_feed)

    @staticmethod
    def _get_titles_set(items: list[Item]) -> set[str]:
        return set(map(lambda item: item.title.value, items))
