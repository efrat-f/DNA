from commands.commandCreator.commandcreator import CommandCreator
from db.dna_sequence import dna_sequence


class CommandReplace(CommandCreator):
    counter = 0
    sign = "_r"

    def __init__(self, arguments):
        index = len(arguments)
        if ":" in arguments:
            index = arguments.index(":")
        sequence_name = None
        self.__seq = arguments[0]
        self.__create_new = False
        if index == len(arguments) - 2:
            sequence_name = arguments[-1]
        if ":" in arguments:
            self.__create_new = True
        self.__index = arguments[1:index:2]
        self.__value = arguments[2:index:2]
        super().__init__(sequence_name)

    def execute(self):
        try:
            replace_dna_sequence = None
            if self.__seq[0] == "@":
                replace_dna_sequence = CommandReplace.data_dna.get_names().get(self.__seq[1:])
            elif self.__seq[0] == "#":
                replace_dna_sequence = CommandReplace.data_dna.get_ids().get(int(self.__seq[1:]))
            if replace_dna_sequence is None:
                raise Exception("seq not exist")
            if self.__create_new == True:
                if self.sequence_name is None or self.sequence_name == "@":
                    self.determine_name()
                elif self.exist_dna_sequence():
                    raise Exception("seq already exist")
                sequence = replace_dna_sequence.get_sequence()
                try:
                    for i in range(len(self.__index)):
                        sequence = sequence[:int(self.__index[i])] + self.__value[i] + sequence[int(self.__index[i]):]
                except IndexError:
                    raise Exception("num values not equal to num indexes")
                new_dna_sequence = dna_sequence(sequence, len(CommandReplace.data_dna), self.name)
                return self.add_to_db(new_dna_sequence)
            else:
                try:
                    for i in range(len(self.__index)):
                        replace_dna_sequence.insert(self.__value[i], int(self.__index[i]))
                except IndexError:
                    raise Exception("num values not equal to num indexes")
                return
        except IndexError:
            raise Exception("invalid seq")
