"""This module contains a set of interfaces for HTML strategies."""

from abc import ABC, abstractmethod
from typing import List


class StrategySaveHTML(ABC):
    """Strategy interface."""
    @abstractmethod
    def prepare_html(self, data: List[dict]) -> str:
        """Prepare html page.

        The operation of preparing a page according to a specific algorithm.
        Each specific strategy defines its own page creation logic.

        :param data: Initial data intended for display on the html page.
        :type data: List[dict]
        :return: Generated html page according to a certain algorithm.
        :rtype: str
        """
        pass
