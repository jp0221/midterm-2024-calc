from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
    
    def execute_command(self, command_string: str):
        try:
            command_parts = command_string.split()
            command_name = command_parts[0]
            self.commands[command_name].execute(*command_parts[1:])
        except KeyError:
            print(f"No such command: {command_name}")