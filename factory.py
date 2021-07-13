from observer import Subject, Observer
from CLI.batch import Batch
from commands.commandsBatch.commandbatchlist import CommandBatchList
from commands.commandsBatch.commandbatchload import CommandBatchLoad
from commands.commandsBatch.commandbatchrun import CommandBatchRun
from commands.commandsBatch.commandbatchsave import CommandBatchSave
from commands.commandsBatch.commandbatchshow import CommandBatchShow
from commands.commandCreator.commanddup import CommandDup
from commands.command_findAll import CommandFindAll
from commands.commandCreator.commandnew import CommandNew
from commands.commandCreator.commandload import CommandLoad
from commands.commandreplace import CommandReplace
from commands.commandsave import CommandSave
from commands.commandslice import CommandSlice
from CLI.confirm import Confirm


class Factory(Observer):

    def __init__(self):
        """Factory Method"""
        self.__num_sequence = 0
        self.commands = {
            "new": CommandNew,
            "load": CommandLoad,
            "dup": CommandDup,
            "slice": CommandSlice,
            "replace": CommandReplace,
            "del": Confirm,
            "save": CommandSave,
            "findall": CommandFindAll,
            "batch": Batch,
            "run": CommandBatchRun,
            "batchlist": CommandBatchList,
            "batchshow": CommandBatchShow,
            "batchsave": CommandBatchSave,
            "batchload": CommandBatchLoad,
            "quit": Confirm
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
