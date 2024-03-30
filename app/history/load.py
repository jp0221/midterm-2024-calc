from app.commands import Command
from app.history import CalculationHistory

class LoadHistoryCommand(Command):
    def __init__(self, calculation_history: CalculationHistory):
        self.calculation_history = calculation_history

    def execute(self):
        try:
            with open("calculation_history.txt", "r") as file:
                self.calculation_history.clear_history()  # Clear current history first
                for line in file:
                    self.calculation_history.add_record(line.strip())
            print("Calculation history loaded.")
        except FileNotFoundError:
            print("No saved history found.")

