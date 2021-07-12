from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_slice(Command_creator):
    __num_sequence_default_name = 0

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
        if sequence_name is None or sequence_name == "@":
            sequence_name = f"seq_s{Command_slice.__num_sequence_default_name}"
            Command_slice.__num_sequence_default_name += 1
        self.__seq = seq
        self.__from_id = int(arguments[1])
        self.__to_id = int(arguments[2])
        super().__init__(sequence_name)

    def execute(self):
        try:
            slice_dna_sequence = None
            if self.__seq[0] == "@":
                slice_dna_sequence = Command_slice.data_dna.get_names().get(self.__seq[1:])
            elif self.__seq[0] == "#":
                slice_dna_sequence = Command_slice.data_dna.get_ids().get(int(self.__seq[1:]))
            if slice_dna_sequence is None:
                raise Exception("seq not exist")
            if self.__create_new == True:
                self.exist_dna_sequence()
                new_dna_sequence = dna_sequence(slice_dna_sequence.get_sequence()[self.__from_id:self.__to_id], len(Command_slice.data_dna), self.sequence_name)
                return self.add_to_db(new_dna_sequence)
            else:
                slice_dna_sequence.set_sequence(slice_dna_sequence.get_sequence()[self.__from_id:self.__to_id])
                return "ijo"
        except IndexError:
            raise Exception("invalid seq")
