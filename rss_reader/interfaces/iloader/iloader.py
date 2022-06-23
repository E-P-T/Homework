
from abc import ABC, abstractmethod


class IHandler(ABC):

    def get_data(self, tag_name: str,
                 title_tag: str,
                 source: str,
                 limit: int) -> dict:
        pass
