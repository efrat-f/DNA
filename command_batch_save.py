from command import Command


class Command_batch_save(Command):

    def __init__(self, arguments):
        try:
            if arguments[0][0] != "@":
                raise Exception("invalid name batch(name need start at '@')")
            self.__batch_name = arguments[0][1:]
            if len(arguments) < 2:
                self.__file_name = None
            else:
                self.__file_name = arguments[1]
        except IndexError:
            raise Exception("one or more of the arguments are missed")

    def __write_file(self, batch):
        with open("DNA_files/" + self.__file_name + ".rawbatch", 'w') as batch_file:
            return batch_file.write(batch.get_content())

    def execute(self):
        batch = Command_batch_save.data_batch.get_names().get(self.__batch_name)
        if batch is None:
            raise Exception("batch not exist")
        if self.__file_name is None:
            self.__file_name = batch.get_name()
        self.__write_file(batch)
        return "success"
