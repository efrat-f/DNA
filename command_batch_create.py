from batch import Batch
from command import Command
from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_batch_create(Command):

    def __init__(self, arguments):
        try:
            self.__batch_name = arguments[0]
        except IndexError:
            raise Exception("one or more of the arguments are missed")

    def execute(self):
        try:
            batch = Batch(self.__batch_name)
            Command_batch_create.data_batch.add_data(batch)
            return batch
        except IndexError:
            raise Exception("invalid seq")
