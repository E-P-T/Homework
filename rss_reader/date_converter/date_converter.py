
from datetime import datetime

from rss_reader.interfaces.idateconverter.idateconverter import IDateConverter


class DateConverter(IDateConverter):
    """Converts date."""

    @staticmethod
    def date_convert(date: str, format: str = '%Y%m%d') -> str:
        """Return the date part.

        :param date: Date in original state.
        :type date: str
        :param format: Substring selection format.
                        Example '%Y%m%d'.
        :type format: str
        :return: Date in the given format.
        :rtype: str
        """
        return datetime.strptime(date, format).date().__str__()
