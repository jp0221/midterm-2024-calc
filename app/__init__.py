import os
import inspect
import pkgutil
import importlib
import sys
from app.commands import CommandHandler, Command, ListCommandsCommand
from dotenv import load_dotenv
import logging
import logging.config
from app.history import CalculationHistory
from app.history.load import LoadHistoryCommand
from app.history.clear import ClearHistoryCommand
from app.history.delete import DeleteHistoryCommand
from app.history.save import SaveHistoryCommand

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_enviornment_variables()
        self.settings.setdefault('ENVIORNMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.calculation_history = CalculationHistory()

        self.command_handler.register_command("menu", ListCommandsCommand(self.command_handler))
    
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured")
    
    def load_enviornment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Enviornment variables loaded.")
        return settings
    
    def get_enviornment_variable(self, env_var: str = 'ENVIORNMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            # Check if the item is a Command subclass and not Command itself
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                try:
                    # Use inspect to safely check the parameters of the __init__ method
                    params = inspect.signature(item.__init__).parameters
                    if 'calculation_history' in params:
                        command_instance = item(self.calculation_history)
                    else:
                        command_instance = item()
                    self.command_handler.register_command(plugin_name.lower(), command_instance)
                    logging.info(f"Command '{item_name}' from plugin '{plugin_name}' registered.")
                except TypeError as e:
                    logging.error(f"Failed to instantiate command '{item_name}' from plugin '{plugin_name}': {e}")
                except ValueError as e:  # Handle cases where inspect cannot get the signature
                    logging.error(f"Cannot inspect command '{item_name}' from plugin '{plugin_name}': {e}")
   
    
    def register_history_commands(self):
        self.command_handler.register_command("clear", ClearHistoryCommand(self.calculation_history))
        self.command_handler.register_command("save", SaveHistoryCommand(self.calculation_history))
        self.command_handler.register_command("load", LoadHistoryCommand(self.calculation_history))
        self.command_handler.register_command("delete", DeleteHistoryCommand(self.calculation_history))
    
    def start(self):
        self.load_plugins()
        self.register_history_commands()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)  # Use sys.exit(0) for a clean exit, indicating success.
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError:  # Assuming execute_command raises KeyError for unknown commands
                    logging.error(f"Unknown command: {cmd_input}")
                    sys.exit(1)  # Use a non-zero exit code to indicate failure or incorrect command.
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            logging.info("Application shutdown.")


if __name__ == "__main__":
    app = App()
    app.start()