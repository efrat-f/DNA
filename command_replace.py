from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_replace(Command_creator):
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
            sequence_name = f"seq_r{Command_replace.__num_sequence_default_name}"
            Command_replace.__num_sequence_default_name += 1
        self.__seq = seq
        self.__index = int(arguments[1])
        self.__value = arguments[2]
        super().__init__(sequence_name)

    def execute(self):
        try:
            replace_dna_sequence = None
            if self.__seq[0] == "@":
                replace_dna_sequence = Command_replace.data_dna.get_names().get(self.__seq[1:])
            elif self.__seq[0] == "#":
                replace_dna_sequence = Command_replace.data_dna.get_ids().get(int(self.__seq[1:]))
            if replace_dna_sequence is None:
                raise Exception("seq not exist")
            if self.__create_new == True:
                self.exist_dna_sequence()
                sequence = replace_dna_sequence.get_sequence()
                new_dna_sequence = dna_sequence(sequence[:self.__index] + self.__value + sequence[self.__index:],
                                                len(Command_replace.data_dna), self.sequence_name)
                return self.add_to_db(new_dna_sequence)
            else:
                replace_dna_sequence.insert(self.__value, self.__index)
                return "ijo"
        except IndexError:
            raise Exception("invalid seq")
