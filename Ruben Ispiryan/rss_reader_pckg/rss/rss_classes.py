import logging
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .helpers import get_media_link_type


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
                'date': self.date.value,
                'link': self.link.value,
                'description': self.description.value,
                'media': [media_link.value for media_link in self.media_links.elements if media_link.value]}

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
    items: list[Item]

    def __repr__(self):
        repr_str = f'Feed Title: {self.title}\n\n'
        for item in self.items:
            repr_str += repr(item)
        logging.info('Printing results to the user in regular format')
        return repr_str
