from CLI.batch import Batch
from commands.commandCreator.commandcreator import CommandCreator


class CommandBatchLoad(CommandCreator):

    def __init__(self, arguments):
        [file_name, batch_name] = self.parser_arguments(arguments)
        if batch_name is None:
            batch_name = file_name
        self.__file_name = file_name
        super().__init__(batch_name)

    def __load_file(self):
        with open("files/" + self.__file_name, 'r') as batch_file:
            return batch_file.readlines()

    def execute(self):
        if type(self).data_batch.get_names().get(self.name) is not None:
            raise Exception("batch already exist")
        batch = Batch([self.sequence_name])
        batch.add_commands(self.__load_file())
        return batch
