from decimal import Decimal
import logging
from app.commands import Command
from calculator import Calculator


class SubtractCommand(Command):
    def execute(self):
        a = Decimal(input("> First Number: "))
        b = Decimal(input("> Second Number: "))
        result = Calculator.subtract(a, b)
        logging.info(f"The result of {a} - {b} is {result}")
        print(f"The result of {a} - {b} is {result}")
        