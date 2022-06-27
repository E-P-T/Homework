
from abc import abstractmethod


class ICreateFile(ABC):

    @abstractmethod
    def create_file(self, file: str) -> None:
        pass
