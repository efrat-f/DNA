from random import randrange
from typing import List

from Subject import Observer, Subject


class CLI(Subject):
    command = 0
    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    # def __init__(self):
    #     self.__processes = processes
    #
    # def get_command(self, command):
    #     self.__processes.run_command(command)
    #
    # def write_command(self, command):
    #     pass

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self, new_command) -> None:
        """
        Trigger an update in each subscriber.
        """
        self.command = new_command
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    # def some_business_logic(self) -> None:
    #     """
    #     Usually, the subscription logic is only a fraction of what a Subject can
    #     really do. Subjects commonly hold some important business logic, that
    #     triggers a notification method whenever something important is about to
    #     happen (or after it).
    #     """
    #
    #     print("\nSubject: I'm doing something important.")
    #     self._state = randrange(0, 10)
    #
    #     print(f"Subject: My state has just changed to: {self._state}")
    #     self.notify()
