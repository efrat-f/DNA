from CLI.CLI import CLI
from commands.command import Command
from commands.commandsConfirm.commanddel import CommandDel
from commands.command_quit import Command_quit


class Confirm(CLI, Command):

    def __init__(self, command, arguments):
        self.commands = {
            "del": CommandDel,
            "quit": Command_quit
        }
        super().__init__()
        self.command = command
        self.arguments = arguments

    def execute(self, *args):
        command_obj, message = self.commands[self.command](self.arguments)
        if command_obj is not None:
            self.command_arr.append(command_obj)
        print(
            f"{command_obj.confirm()}")
        while True:
            confirm = input("> confirm >>>")
            if confirm == "N" or confirm == "n":
                return f"canceled {self.command}"
            elif confirm == "Y" or confirm == "y":
                return self.run_last_command()
            print("You have typed an invalid response. Please either confirm by 'y'/'Y', or"
                  "cancel by 'n'/'N'.")
