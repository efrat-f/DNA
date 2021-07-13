from commands.commandCreator.commandcreator import CommandCreator
from db.dna_sequence import dna_sequence


class CommandDup(CommandCreator):
    counter = 0
    sign = "_"

    def __init__(self, arguments):
        [seq, sequence_name] = self.parser_arguments(arguments)
        self.__seq = seq
        super().__init__(sequence_name)

    def execute(self):
        try:
            dup_dna_sequence = None
            if self.__seq[0] == "@":
                dup_dna_sequence = CommandDup.data_dna.get_names().get(self.__seq[1:])
            elif self.__seq[0] == "#":
                dup_dna_sequence = CommandDup.data_dna.get_ids().get(int(self.__seq[1:]))
            if dup_dna_sequence is None:
                raise Exception("seq not exist")
            if self.sequence_name is None:
                self.determine_name()
            elif self.exist_dna_sequence():
                raise Exception("seq already exist")
            new_dna_sequence = dna_sequence(dup_dna_sequence.get_sequence(), len(CommandDup.data_dna), self.name)
            return self.add_to_db(new_dna_sequence)
        except IndexError:
            raise Exception("invalid seq")
