from CLI.batch import Batch
from commands.command import Command


class CommandBatchCreate(Command):

    def __init__(self, arguments):
        try:
            self.__batch_name = arguments[0]
        except IndexError:
            raise Exception("one or more of the arguments are missed")

    def execute(self):
        try:
            if Command.data_batch.get_names().get(self.__batch_name) is not None:
                raise Exception("batch already exist")
            batch = Batch(self.__batch_name)
            CommandBatchCreate.data_batch.add_data(batch)
            return batch
        except IndexError:
            raise Exception("invalid seq")
