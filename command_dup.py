from dna_sequence import dna_sequence


class Command_dup:
    __num_sequence_default_name = 0

    def __init__(self, command):
        self.__command = command

    @staticmethod
    def __load_file(file_name):
        with open(file_name, 'r') as sequence_file:
            return sequence_file.read()

    def execute(self, num_sequence):
        file_name = self.__command[0]
        sequence_name = self.__command[1]
        if sequence_name is None:
            sequence_name = f"{file_name}{self.__num_sequence_default_name}"
            self.__num_sequence_default_name += 1
        return dna_sequence(self.__load_file(file_name), num_sequence, sequence_name)
