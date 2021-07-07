from Subject import Subject, Observer
from command_dup import Command_dup
from command_new import Command_new
from command_load import Command_load


class Factory(Observer):

    def __init__(self):
        """Factory Method"""
        self.__num_sequence = 0
        self.localizers = {
            "new": Command_new,
            "load": Command_load,
            "dup": Command_dup,
        }

    def update(self, subject: Subject) -> None:
        command = subject.command
        if len(command) < 3:
            command.append(None)
        command_obj = self.localizers[command[0]](command[1], command[2])
        command_obj.execute(self.__num_sequence)
        self.__num_sequence += 1

    # def separate_and_execute(self, command):
    #     separate_command =
    #     execute(separate_command)
