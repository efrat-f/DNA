from command import Command
from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_load(Command_creator):
    __num_files_default = {}

    def __init__(self, arguments):
        [file_name, sequence_name] = self.parser_arguments(arguments)
        if sequence_name is None:
            num_sequence_default_name = self.__num_files_default.get(file_name)
            if num_sequence_default_name is None:
                self.__num_files_default[file_name] = 0
            sequence_name = f"{file_name}{self.__num_files_default[file_name]}"
            self.__num_files_default[file_name] += 1
        self.__file_name = file_name
        super().__init__(sequence_name)

    def __load_file(self):
        with open(self.__file_name, 'r') as sequence_file:
            return sequence_file.read()

    def execute(self):
        self.exist_dna_sequence()
        new_dna_sequence = dna_sequence(self.__load_file(), len(Command.data_dna), self.sequence_name)
        return self.add_to_db(new_dna_sequence)
