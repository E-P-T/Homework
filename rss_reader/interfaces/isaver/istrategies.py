"""This module contains a set of interfaces for HTML strategies."""

from abc import ABC, abstractmethod
from typing import List


class StrategySaveHTML(ABC):
    @abstractmethod
    def prepare_html(self, data: List[dict]) -> str:
        pass
