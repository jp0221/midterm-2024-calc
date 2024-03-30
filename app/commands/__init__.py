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
    
    def list_commands(self):
        print("Available commands:")
        for command_name in self.commands.keys():
            print(f"- {command_name}")

class ListCommandsCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        self.command_handler.list_commands()
