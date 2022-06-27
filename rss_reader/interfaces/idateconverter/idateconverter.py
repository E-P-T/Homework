
class IDateConverter(ABC):
    @staticmethod
    @abstractmethod
    def date_convert(date: str, format: str) -> str:
        pass
