# This program uses the inheritance approach from "Money and Inheritance" and completes it
# by adding addition, multiplication, and subtraction support. It then tests the class using
# a test function at the end.

from decimal import Decimal
import random


class Money(Decimal):
    def __new__(cls, v, units='USD'):
        obj = super(Money, cls).__new__(cls, v)
        obj.units = units
        return obj

    def __add__(self, other):
        # If-Else statements fixes a bug that returned an attribute error.

        # Basically, it determines how the operation should be performed, based on the type of object
        # being added/subtracted/multiplied.
        if isinstance(other, Money):
            return Money(super().__add__(other), self.units)
        else:
            return Money(super().__add__(Decimal(other)), self.units)

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(super().__sub__(other), self.units)
        else:
            return Money(super().__sub__(Decimal(other)), self.units)

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(super().__mul__(other), self.units)
        else:
            return Money(super().__mul__(Decimal(other)), self.units)

    def __repr__(self):
        return f"{super().__repr__()} {self.units}"


# Function that tests operations in Money class.
def test_money_operations():
    # Random values assigned to money variables.
    value1 = round(random.uniform(1, 100), 2)
    value2 = round(random.uniform(1, 100), 2)

    # Random value to test multiplication.
    multiply_factor = round(random.uniform(1, 10), 2)

    money1 = Money(str(value1), 'USD')
    money2 = Money(str(value2), 'USD')

    # Perform operations.
    add_result = money1 + money2
    sub_result = money1 - money2
    mul_result = money1 * multiply_factor

    # Print results.
    print(f"{money1} added to {money2} result: {add_result} {add_result.units}")
    print(f"{money1} subtracted by {money2} result: {sub_result} {sub_result.units}")
    print(f"{money1} multiplied by {multiply_factor} result:"
          f" {mul_result.quantize(Decimal('0.01'))} {mul_result.units}")


test_money_operations()
