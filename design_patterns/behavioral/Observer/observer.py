from abc import ABC, abstractmethod
from typing import Optional, TextIO, DefaultDict, List
from collections import defaultdict


# Subscriber interface
class Listener(ABC):
    @abstractmethod
    def update(self, data: str):
        pass


# Event manager (publisher)
class EventManager:
    def __init__(self):
        self.listeners: DefaultDict[str, List[Listener]] = defaultdict(list)

    def subscribe(self, eventType: str, listener: Listener):
        self.listeners[eventType].append(listener)

    def unsubscribe(self, eventType: str, listener: Listener):
        self.listeners[eventType].remove(listener)

    def notify(self, eventType: str, data: str):
        for listener in self.listeners[eventType]:
            listener.update(data)


# Editor (business logic class using composition for EventManager)
class Editor:
    def __init__(self):
        self.events = EventManager()
        self.__file: Optional[TextIO] = None
        self.__file_path: Optional[str] = None

    def openFile(self, path: str):
        self.__file = open(path, "w")
        self.__file_path = path
        self.events.notify("open", path)

    def saveFile(self):
        if self.__file:
            self.__file.write("Saving some changes...\n")
            self.__file.flush()
            self.events.notify("save", self.__file_path)


# Concrete subscribers
class LoggingListener(Listener):
    def __init__(self, log_filename: str, message: str):
        self.log: TextIO = open(log_filename, "a")
        self.message = message

    def update(self, filename: str):
        formatted_message = self.message.replace('%s', filename)
        self.log.write(formatted_message + "\n")
        self.log.flush()


class EmailAlertsListener(Listener):
    def __init__(self, email: str, message: str):
        self.email = email
        self.message = message

    def update(self, filename: str):
        formatted_message = self.message.replace('%s', filename)
        # In real life, this would be an email. For now, print.
        print(f"Email to {self.email}: {formatted_message}")


# Application config
class Application:
    def config(self):
        editor = Editor()

        logger = LoggingListener(
            "log.txt",
            "Someone has opened the file: %s"
        )
        editor.events.subscribe("open", logger)

        emailAlerts = EmailAlertsListener(
            "admin@example.com",
            "Someone has changed the file: %s"
        )
        editor.events.subscribe("save", emailAlerts)

        # Simulate file operations
        editor.openFile("test.txt")
        editor.saveFile()
        editor.events.unsubscribe("save", emailAlerts)


# Run the application config
if __name__ == "__main__":
    app = Application()
    app.config()
