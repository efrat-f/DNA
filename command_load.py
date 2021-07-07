from command import Command
from dna_sequence import dna_sequence


class Command_load(Command):
    __num_sequence_default_name = 0

    def __init__(self, file_name, sequence_name):
        self.__file_name = file_name
        self.__sequence_name = sequence_name

    def __load_file(self):
        with open(self.__file_name, 'r') as sequence_file:
            return sequence_file.read()

    def execute(self, num_sequence):
        if self.__sequence_name is None:
            self.__sequence_name = f"{self.__file_name}{self.__num_sequence_default_name}"
            self.__num_sequence_default_name += 1
        return dna_sequence(self.__load_file(), num_sequence, self.__sequence_name)
