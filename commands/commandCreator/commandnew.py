from commands.commandCreator.commandcreator import CommandCreator
from db.dna_sequence import dna_sequence


class CommandNew(CommandCreator):
    counter = 0
    sign = ""

    def __init__(self, arguments):
        [self.__sequence, sequence_name] = self.parser_arguments(arguments)
        super().__init__(sequence_name)

    def execute(self):
        if self.sequence_name is None:
            self.determine_name()
        elif self.exist_dna_sequence():
            raise Exception("seq already exist")
        new_dna_sequence = dna_sequence(self.__sequence, len(CommandNew.data_dna), self.name)
        return self.add_to_db(new_dna_sequence)
