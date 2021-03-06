from commands.command import Command


class CommandBatchRun(Command):

    def __init__(self, arguments):
        try:
            if arguments[0][0] != "@":
                raise Exception("invalid name batch(name need start at '@')")
            self.__batch_name = arguments[0][1:]
        except IndexError:
            raise Exception("one or more of the arguments are missed")

    def execute(self):
        try:
            batch = Command.data_batch.get_names().get(self.__batch_name)
            return batch.run_commands()
        except IndexError:
            raise Exception("invalid batch")
