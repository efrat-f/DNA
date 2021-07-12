from command import Command
from data_dna import Data_dna


class Command_creator(Command):
    def __init__(self, sequence_name):
        self.sequence_name = sequence_name

    def parser_arguments(self, arguments):
        if len(arguments) > 1:
            if arguments[1][-1] in [chr(i) for i in range(10)]:
                raise Exception("name not valid(name can't include number at the end")
            if arguments[1][0] != "@":
                raise Exception("incorrect sequence args(sequence name need start whit @)")
            arguments[1] = arguments[1][1:]
            if arguments[1] == "":
                raise Exception("invalid sequence name")
        else:
            arguments.append(None)
        return [arguments[0], arguments[1]]

    def execute(self, *args) -> None:
        pass

    def add_to_db(self, new_dna_sequence):
        Command.data_dna.add_dna_sequence(new_dna_sequence)
        return f"[{new_dna_sequence.get_id()}] {new_dna_sequence.get_name()}: {new_dna_sequence.get_sequence()}"

    def exist_dna_sequence(self):
        if Command.data_dna.get_names().get(self.sequence_name) is not None:
            raise Exception("seq already exist")
