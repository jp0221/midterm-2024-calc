from app.commands import Command
from app.history import CalculationHistory

class SaveHistoryCommand(Command):
    def __init__(self, calculation_history: CalculationHistory):
        self.calculation_history = calculation_history

    def execute(self):
        # Prompt the user for a filename, ensuring it ends with '.csv'
        filename = input("Please enter a filename to save as (include '.csv'): ")
        if not filename.endswith('.csv'):
            print("Error: Filename must end with '.csv'.")
            return

        # Save the DataFrame to the file specified by the user
        try:
            self.calculation_history.history.to_csv(filename, index=False, header=False)
            print(f"Calculation history saved to {filename}.")
        except Exception as e:
            print(f"Failed to save file: {e}")

