from commands.command import Command


class Command_quit(Command):
    def __init__(self, arguments):
        pass

    def execute(self, *args):
        return "good bye!"
