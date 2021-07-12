from abc import ABC, abstractmethod

from data_batch import Data_batch
from data_dna import Data_dna


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """
    data_dna = Data_dna()
    data_batch = Data_batch()

    @abstractmethod
    def execute(self, *args) -> None:
        pass
