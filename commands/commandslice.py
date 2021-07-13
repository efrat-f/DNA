from commands.commandCreator.commandcreator import CommandCreator
from db.dna_sequence import dna_sequence


class CommandSlice(CommandCreator):
    counter = 0
    sign = "_s"

    def __init__(self, arguments):
        sequence_name, seq = None, None
        if len(arguments) == 0:
            arguments.append(None)
        if len(arguments) < 4:
            self.__create_new = False
            [seq, sequence_name] = self.parser_arguments([arguments[0]])
        else:
            self.__create_new = True
            if len(arguments) < 5:
                [seq, sequence_name] = self.parser_arguments([arguments[0]])
            else:
                [seq, sequence_name] = self.parser_arguments([arguments[0], arguments[4]])
        self.__seq = seq
        self.__from_id = int(arguments[1])
        self.__to_id = int(arguments[2])
        super().__init__(sequence_name)

    def execute(self):
        try:
            slice_dna_sequence = None
            if self.__seq[0] == "@":
                slice_dna_sequence = CommandSlice.data_dna.get_names().get(self.__seq[1:])
            elif self.__seq[0] == "#":
                slice_dna_sequence = CommandSlice.data_dna.get_ids().get(int(self.__seq[1:]))
            if slice_dna_sequence is None:
                raise Exception("seq not exist")
            if self.__create_new == True:
                if self.sequence_name is None or self.sequence_name == "@":
                    self.determine_name()
                elif self.exist_dna_sequence():
                    raise Exception("seq already exist")
                new_dna_sequence = dna_sequence(slice_dna_sequence.get_sequence()[self.__from_id:self.__to_id], len(CommandSlice.data_dna), self.name)
                return self.add_to_db(new_dna_sequence)
            else:
                slice_dna_sequence.set_sequence(slice_dna_sequence.get_sequence()[self.__from_id:self.__to_id])
                return
        except IndexError:
            raise Exception("invalid seq")
