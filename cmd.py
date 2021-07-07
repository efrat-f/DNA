from CLI import CLI


class CMD(CLI):

    def run(self):
        while True:
            command = input("> cmd >>>")
            if command == "exit":
                break
            self.notify(command.split())

