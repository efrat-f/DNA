from random import randrange
from typing import List

from Subject import Observer, Subject


class CLI(Subject):
    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def __init__(self):
        super().__init__()
        self.command_arr = []

    # def get_command(self, command):
    #     self.__processes.run_command(command)
    #
    # def write_command(self, command):
    #     pass

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        print("Subject: Notifying observers...")
        for observer in self._observers:
            command_obj = observer.update(self)
            if command_obj is not None:
                self.command_arr.append(command_obj)

    def some_business_logic(self, new_command) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        if len(new_command) < 1:
            new_command.append(None)
        if len(new_command) >= 2:
            self.arguments = new_command[1:]
        else:
            self.arguments = []
        self.command = new_command[0]
        self.notify()

    def run_commands(self):
        for command_obj in self.command_arr:
            print(command_obj.execute())

