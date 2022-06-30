"""This module contains a set of interfaces for HTML strategies."""


class StrategySaveHTML(ABC):
    @abstractmethod
    def prepare_html(self, data: List[dict]) -> str:
        pass
