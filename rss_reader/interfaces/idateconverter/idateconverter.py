"""This module contains classes that work with dates."""


class IDateConverter(ABC):
    """Converts date."""

    @staticmethod
    @abstractmethod
    def date_convert(date: str, format: str) -> str:
        """Return the textual representation of the substring.

        :param date: Date in original state.
        :type date: str
        :param format: Substring selection format.
                        Example '%Y%m%d'.
        :type format: str
        :return: Date in the given format.
        :rtype: str
        """
        pass
