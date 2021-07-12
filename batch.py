from CLI import CLI
from command import Command


class Batch(CLI, Command):

    def __init__(self, arguments):
        try:
            self.__name = arguments[0]
        except IndexError:
            raise Exception("one or more of the arguments are missed")
        self.__content = ""
        Batch.data_batch.add_data(self)
        super().__init__()

    def get_name(self):
        return self.__name

    def execute(self) -> None:
        while True:
            try:
                command = input("> batch >>>")
                if command == "end":
                    break
                self.add_command(command)
            except Exception as e:
                print(f"ERROR: {e}")

    def get_content(self):
        return self.__content

    def add_command(self, command):
        self.__content += command + "\n"
        self.some_business_logic(command.split())

    def add_commands(self, commands):
        list(map(lambda command: self.add_command(command), commands))

