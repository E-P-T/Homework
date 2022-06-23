
from abc import ABC, abstractmethod


class IParser(ABC):
    @abstractmethod
    def create_parser(self, markup: bytes, features: str = 'xml') -> None:
        pass

    @abstractmethod
    def get_tags_text(self,
                      selector: str,
                      limit_elms: int = None) -> Generator[str, None, None]:
        pass

    @abstractmethod
    def get_items(self,
                  template: dict,
                  name: str,
                  limit_elms: int = None) -> List[dict]:
        pass
