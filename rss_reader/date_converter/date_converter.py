
from rss_reader.interfaces.idateconverter.idateconverter import IDateConverter


class DateConverter(IDateConverter):
    @staticmethod
    def date_convert(date: str, format: str = '%Y%m%d') -> str:
        return datetime.strptime(date, format).date().__str__()
