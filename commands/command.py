from abc import ABC, abstractmethod

from db.databatch import DataBatch
from db.datadna import DataDNA


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """
    data_dna = DataDNA()
    data_batch = DataBatch()

    @abstractmethod
    def execute(self, *args) -> None:
        pass
