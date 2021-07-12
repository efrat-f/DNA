from command import Command
from command_creator import Command_creator
from dna_sequence import dna_sequence


class Command_findAll(Command):

    def __init__(self, arguments):
        self.__seq = arguments[0]
        self.__sequence = arguments[1]

    def execute(self):
        try:
            findAll_dna_sequence = None
            to_findAll_dna_sequence = None
            if self.__seq[0] == "@":
                findAll_dna_sequence = Command_findAll.data_dna.get_names().get(self.__seq[1:]).get_sequence()
            elif self.__seq[0] == "#":
                findAll_dna_sequence = Command_findAll.data_dna.get_ids().get(int(self.__seq[1:])).get_sequence()
            if findAll_dna_sequence is None:
                raise Exception("seq to search not exist")
            if self.__sequence[0] == "@":
                to_findAll_dna_sequence = Command_findAll.data_dna.get_names().get(self.__sequence[1:]).get_sequence()
            elif self.__sequence[0] == "#":
                to_findAll_dna_sequence = Command_findAll.data_dna.get_ids().get(
                    int(self.__sequence[1:])).get_sequence()
            else:
                to_findAll_dna_sequence = self.__sequence
            if to_findAll_dna_sequence is None:
                raise Exception("seq to find not exist")
            all_indexs = "".join(f"{i} " for i in range(len(findAll_dna_sequence)) if
                           findAll_dna_sequence.startswith(to_findAll_dna_sequence, i))
            if all_indexs == "":
                return "not sub"
            return all_indexs
        except IndexError:
            raise Exception("invalid seq")
