import pandas as pd

class CalculationHistory:
    def __init__(self):
        # Initialize an empty DataFrame with a specified column
        self.history = pd.DataFrame(columns=['Record'])
    
    def add_record(self, record):
        # Append a new record to the DataFrame
        self.history = self.history._append({'Record': record}, ignore_index=True)
    
    def clear_history(self):
        # Clear the DataFrame
        self.history = pd.DataFrame(columns=['Record'])
    
    def delete_record(self, index):
        # Delete a record by index if it exists
        if 0 <= index < len(self.history):
            self.history = self.history.drop(index).reset_index(drop=True)
    
    def get_history(self):
        # Return the history DataFrame
        return self.history
