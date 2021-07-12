from command import Command
from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_del(Command):

    def __init__(self, arguments):
        try:
            self.__seq = arguments[0]
            if self.__seq[0] == "@":
                self.del_dna_sequence = Command.data_dna.get_names().get(self.__seq[1:])
            elif self.__seq[0] == "#":
                self.del_dna_sequence = Command.data_dna.get_ids().get(int(self.__seq[1:]))
            if self.del_dna_sequence is None:
                raise Exception("seq not exist")
        except IndexError:
            raise Exception("one or more of the arguments are missed")

    def execute(self):
        try:
            Command.data_dna.delete_obj(self.del_dna_sequence)
            return f"Deleted: [{self.del_dna_sequence.get_id()}] {self.del_dna_sequence.get_name()}: {self.del_dna_sequence.get_sequence()}"

        except IndexError:
            raise Exception("invalid seq")

    def get_seq(self):
        return self.__seq