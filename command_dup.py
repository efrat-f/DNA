from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_dup(Command_creator):
    __num_sequence_default_name = 0

    def __init__(self, arguments):
        [seq, sequence_name] = self.parser_arguments(arguments)
        if sequence_name is None:
            sequence_name = f"seq_{self.__num_sequence_default_name}"
            self.__num_sequence_default_name += 1
        self.__seq = seq
        super().__init__(sequence_name)

    def execute(self):
        try:
            dup_dna_sequence = None
            if self.__seq[0] == "@":
                dup_dna_sequence = Command_dup.data_dna.get_names().get(self.__seq[1:])
            elif self.__seq[0] == "#":
                dup_dna_sequence = Command_dup.data_dna.get_ids().get(int(self.__seq[1:]))
            if dup_dna_sequence is None:
                raise Exception("seq not exist")
            self.exist_dna_sequence()
            new_dna_sequence = dna_sequence(dup_dna_sequence.get_sequence(), len(Command_dup.data_dna), self.sequence_name)
            return self.add_to_db(new_dna_sequence)
        except IndexError:
            raise Exception("invalid seq")
