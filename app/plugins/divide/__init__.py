from decimal import Decimal
import logging
from app.commands import Command
from calculator import Calculator
from app.history import CalculationHistory


class DivideCommand(Command):
    def __init__(self, calculation_history: CalculationHistory):
        self.calculation_history = calculation_history

    def execute(self):
        a = Decimal(input("> First Number: "))
        b = Decimal(input("> Second Number: "))
        result = Calculator.divide(a, b)
        logging.info(f"The result of {a} / {b} is {result}")
        print(f"The result of {a} / {b} is {result}")
        self.calculation_history.add_record(f"{a} / {b} = {result}")
        