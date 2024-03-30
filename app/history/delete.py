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
            display_history(self.calculation_history)  # Call the display function
        except ValueError:
            print("Invalid index.")
        
def display_history(calculation_history):
    if not calculation_history.history.empty:
        print("Calculation History:")
        for index, row in calculation_history.history.iterrows():
            print(f"{index}: {row['Record']}")
    else:
        print("Calculation history is empty.")