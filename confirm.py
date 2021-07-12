from CLI import CLI
from command import Command
from command_del import Command_del


class Confirm(CLI, Command):

    def __init__(self, command, arguments):
        self.commands = {
            "del": Command_del
        }
        super().__init__()
        self.command = command
        self.arguments = arguments

    def execute(self, *args):
        command_obj = self.commands[self.command](self.arguments)
        if command_obj is not None:
            self.command_arr.append(command_obj)
        print(
            f"Do you really want to {self.command} command: {self.command_arr[-1].del_dna_sequence.get_sequence()}? "
            "Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
        while (True):
            confirm = input("> confirm >>>")
            if confirm == "N" or confirm == "n":
                return f"canceled {self.command}"
            elif confirm == "Y" or confirm == "y":
                return self.run_commands()
            print("You have typed an invalid response. Please either confirm by 'y'/'Y', or"
                  "cancel by 'n'/'N'.")

    def run_commands(self):
        return self.command_arr[-1].execute()
