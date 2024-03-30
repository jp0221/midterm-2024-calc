from app.commands import Command
from app.history import CalculationHistory

class SaveHistoryCommand(Command):
    def __init__(self, calculation_history: CalculationHistory):
        self.calculation_history = calculation_history

    def execute(self):
        with open("calculation_history.txt", "w") as file:
            for record in self.calculation_history.get_history():
                file.write(record + "\n")
        print("Calculation history saved.")
