from command import Command
from dna_sequence import dna_sequence


class Command_new(Command):
    __num_sequence_default_name = 0

    def __init__(self, sequence, sequence_name=None):
        self.__sequence = sequence
        self.__sequence_name = sequence_name

    def execute(self, num_sequence):
        if self.__sequence_name is None:
            sequence_name = f"seq{self.__num_sequence_default_name}"
            self.__num_sequence_default_name += 1
        return dna_sequence(self.__sequence, num_sequence, self.__sequence_name)
