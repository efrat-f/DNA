from command import Command


class Command_batch_list(Command):

    def __init__(self, arguments):
        pass

    def execute(self):
        try:
            batch_list = "".join(name + " " for name in Command.data_batch.get_names().keys())
            if batch_list == "":
                return "there are no batches"
            return batch_list
        except IndexError:
            raise Exception("invalid batch")
