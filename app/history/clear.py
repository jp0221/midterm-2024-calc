from app.commands import Command
from app.history import CalculationHistory

class ClearHistoryCommand(Command):
    def __init__(self, calculation_history: CalculationHistory):
        self.calculation_history = calculation_history

    def execute(self):
        self.calculation_history.clear_history()
        print("Calculation history cleared.")

