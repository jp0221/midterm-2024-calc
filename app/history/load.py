from app.commands import Command
from app.history import CalculationHistory
import pandas as pd

class LoadHistoryCommand(Command):
    def __init__(self, calculation_history: CalculationHistory):
        self.calculation_history = calculation_history

    def execute(self):
        display_history(self.calculation_history)

def display_history(calculation_history):
    history_df = calculation_history.get_history()
    if not history_df.empty:
        print("Calculation History:")
        for index, row in history_df.iterrows():
            print(f"{index}: {row['Record']}")
    else:
        print("Calculation history is empty.")

