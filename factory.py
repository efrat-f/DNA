from Subject import Subject, Observer
from batch import Batch
from command_batch_create import Command_batch_create
from command_batch_list import Command_batch_list
from command_batch_load import Command_batch_load
from command_batch_run import Command_batch_run
from command_batch_save import Command_batch_save
from command_batch_show import Command_batch_show
from command_creator import Command_creator
from command_del import Command_del
from command_dup import Command_dup
from command_findAll import Command_findAll
from command_new import Command_new
from command_load import Command_load
from command_replace import Command_replace
from command_save import Command_save
from command_slice import Command_slice
from confirm import Confirm


class Factory(Observer):

    def __init__(self):
        """Factory Method"""
        self.__num_sequence = 0
        self.commands = {
            "new": Command_new,
            "load": Command_load,
            "dup": Command_dup,
            "slice": Command_slice,
            "replace": Command_replace,
            "del": Confirm,
            "save": Command_save,
            "findall": Command_findAll,
            "batch": Batch,
            "run": Command_batch_run,
            "batchlist": Command_batch_list,
            "batchshow": Command_batch_show,
            "batchsave": Command_batch_save,
            "batchload": Command_batch_load
        }

    def update(self, subject: Subject):
        try:
            command = subject.command
            arguments = subject.arguments
            if self.commands[command] == Confirm:
                return self.commands[command](command, arguments)
            return self.commands[command](arguments)
        except KeyError:
            raise Exception("command not found")
        except IndexError:
            raise Exception("one or more of the arguments are missed")
        except Exception as e:
            raise Exception(e)
    # def separate_and_execute(self, command):
    #     separate_command =
    #     execute(separate_command)
