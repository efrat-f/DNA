from batch import Batch
from command import Command
from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_batch_load(Command_creator):

    def __init__(self, arguments):
        [file_name, batch_name] = self.parser_arguments(arguments)
        if batch_name is None:
            batch_name = file_name
        self.__file_name = file_name
        super().__init__(batch_name)

    def __load_file(self):
        with open("DNA_files/" + self.__file_name, 'r') as batch_file:
            return batch_file.readlines()

    def execute(self):
        batch = Batch([self.sequence_name])
        batch.add_commands(self.__load_file())
        return batch
