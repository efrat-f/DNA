from commands.command import Command


class CommandCreator(Command):

    sign = 0
    counter = ""

    def __init__(self, sequence_name):
        self.sequence_name = sequence_name
        self.name = sequence_name

    def determine_name(self):
        while True:
            self.name = f"seq{type(self).sign}{type(self).counter}"
            type(self).counter += 1
            if not self.exist_dna_sequence():
                break

    def parser_arguments(self, arguments):
        if len(arguments) > 1:
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
        Command.data_dna.add_data(new_dna_sequence)
        return f"[{new_dna_sequence.get_id()}] {new_dna_sequence.get_name()}: {new_dna_sequence.get_sequence()}"

    def exist_dna_sequence(self):
        if Command.data_dna.get_names().get(self.name) is None:
            return False
        return True
