from commands.command import Command


class CommandSave(Command):

    def __init__(self, arguments):
        self.__seq = arguments[0]
        if len(arguments) < 2:
            self.__file_name = None
        else:
            self.__file_name = arguments[1]

    def write_file(self, dna_sequence):
        with open("files/" + self.__file_name + ".rawdna", 'w') as sequence_file:
            return sequence_file.write(dna_sequence.get_sequence())

    def execute(self):
        try:
            save_dna_sequence = None
            if self.__seq[0] == "@":
                save_dna_sequence = CommandSave.data_dna.get_names().get(self.__seq[1:])
            elif self.__seq[0] == "#":
                save_dna_sequence = CommandSave.data_dna.get_ids().get(int(self.__seq[1:]))
            if save_dna_sequence is None:
                raise Exception("seq not exist")
            if self.__file_name is None:
                self.__file_name = save_dna_sequence.get_name()
            self.write_file(save_dna_sequence)
        except IndexError:
            raise Exception("invalid seq")
