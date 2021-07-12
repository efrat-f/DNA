from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_new(Command_creator):
    __num_sequence_default_name = 0

    def __init__(self, arguments):
        [sequence, sequence_name] = self.parser_arguments(arguments)
        if sequence_name is None:
            sequence_name = f"seq{Command_new.__num_sequence_default_name}"
            Command_new.__num_sequence_default_name += 1
        self.__sequence = sequence
        super().__init__(sequence_name)

    def execute(self):
        self.exist_dna_sequence()
        new_dna_sequence = dna_sequence(self.__sequence, len(Command_new.data_dna), self.sequence_name)
        return self.add_to_db(new_dna_sequence)
