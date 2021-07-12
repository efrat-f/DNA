from CLI import CLI
from command_del import Command_del


class CMD(CLI):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            try:
                command = input("> cmd >>>")
                if command == "exit":
                    break
                self.some_business_logic(command.split())
                self.run_commands()
            except Exception as e:
                print(f"ERROR: {e}")

    def run_commands(self):
        print(self.command_arr[-1].execute())