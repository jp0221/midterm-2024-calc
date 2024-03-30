from app.commands import Command
from app.history import CalculationHistory

class DeleteHistoryCommand(Command):
    def __init__(self, calculation_history: CalculationHistory):
        self.calculation_history = calculation_history

    def execute(self):
        try:
            index = int(input("Enter the index of the record to delete: "))
            self.calculation_history.delete_record(index)
            print(f"Record at index {index} deleted.")
        except ValueError:
            print("Invalid index.")
