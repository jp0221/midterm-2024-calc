class CalculationHistory:
    def __init__(self):
        self.history = []
    
    def add_record(self, record):
        self.history.append(record)
    
    def clear_history(self):
        self.history.clear()
    
    def delete_record(self, index):
        if 0 <= index < len(self.history):
            del self.history[index]
    
    def get_history(self):
        return self.history