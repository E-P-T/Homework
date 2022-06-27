

class IComponent(ABC):

    @abstractmethod
    def operation(self, data: DataFrame) -> DataFrame:
        pass