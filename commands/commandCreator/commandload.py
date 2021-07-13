from commands.commandCreator.commandcreator import CommandCreator
from db.dna_sequence import dna_sequence


class CommandLoad(CommandCreator):
    __num_files_default = {}

    def __init__(self, arguments):
        [file_name, sequence_name] = self.parser_arguments(arguments)
        self.__file_name = file_name
        super().__init__(sequence_name)

    def __load_file(self):
        with open("files/" + self.__file_name, 'r') as sequence_file:
            return sequence_file.read()

    def determine_name(self):
        num_sequence_default_name = self.__num_files_default.get(self.__file_name)
        if num_sequence_default_name is None:
            self.__num_files_default[self.__file_name] = 0
        while True:
            self.name = f"{self.__file_name}{self.__num_files_default[self.__file_name]}"
            self.__num_files_default[self.__file_name] += 1
            if not self.exist_dna_sequence():
                break

    def execute(self):
        if self.sequence_name is None:
            self.determine_name()
        elif self.exist_dna_sequence():
            raise Exception("seq already exist")
        new_dna_sequence = dna_sequence(self.__load_file(), len(type(self).data_dna), self.name)
        return self.add_to_db(new_dna_sequence)
