from CLI.CLI import CLI


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
                run = self.run_last_command()
                if run is not None:
                    print(run)
                if run == "Goodbye!":
                    break
            except Exception as e:
                print(f"ERROR: {e}")

