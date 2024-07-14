# This program rewrites the BankAcct class from assignment 9A and inherits from the Money
# class from assignment 10A. It replaces BankAcct's deposit and withdraw methods with add
# and subtract from the Money class. It then tests the class using a test function at the end.

from decimal import Decimal
import random


class Money(Decimal):
    def __new__(cls, v, units='USD'):
        obj = super(Money, cls).__new__(cls, v)
        obj.units = units
        return obj

    def __add__(self, other):
        # As stated in previous assignment, If-Else statements fixes a bug that returned an error.
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


class BankAcct:
    def __init__(self, name, acct_num, amount, interest_rate, units='USD'):
        self.name = name
        self.acct_num = acct_num
        self.amount = Money(str(amount), units)
        self.interest_rate = interest_rate

    # Adjusts the interest rate to a new rate.
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Withdraws specified amount from the account, unless funds are insufficient. Does not withdraw if insufficient.
    def withdraw(self, amount):
        amount_to_withdraw = Money(str(amount), self.amount.units)
        if amount_to_withdraw > self.amount:
            print("ERROR! Insufficient funds.")
            return None
        self.amount -= amount_to_withdraw

    # Deposits specified amount into account.
    def deposit(self, amount):
        amount_to_deposit = Money(str(amount), self.amount.units)
        self.amount += amount_to_deposit

    # Returns current balance of account.
    def balance(self):
        return self.amount

    # Calculates interest based on amount, interest rate, and days passed.
    def calculate_interest(self, days):
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    # Returns string representation of account.
    def __str__(self):
        return (f"Account Holder: {self.name}\nAccount Number: {self.acct_num}\nAccount Balance: {self.amount}"
                f"\nInterest Rate: {self.interest_rate:.2f}%")


# Test function for BankAcct. Essentially checks for successes and no errors.
def test_bank_acct():
    name = "Johan Santos"

    # Randomizes account number, initial balance, and initial interest rate.
    acct_num = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    initial_balance = round(random.uniform(1000, 4000), 2)
    interest_rate = round(random.uniform(1.5, 3.5), 1)

    # Creates bank account instance.
    account = BankAcct(name, acct_num, initial_balance, interest_rate)

    print("Initial account details:")
    print(account)

    amount = round(random.uniform(200, 1000), 2)
    account.deposit(amount)
    print(f"\nTest deposit of {amount:.2f} {account.amount.units}: ")
    print(account)

    amount = round(random.uniform(200, float(account.balance())), 2)
    account.withdraw(amount)
    print(f"\nTest successful withdraw of {amount:.2f} {account.amount.units}: ")
    print(account)

    after_successful_wd_balance = account.balance()
    amount = round(random.uniform(float(after_successful_wd_balance) + 1, float(after_successful_wd_balance) + 1500), 2)
    print(f"\nTest failed withdrawal of {amount:.2f} {account.amount.units}: ")
    account.withdraw(amount)
    print(account)

    interest = account.calculate_interest(30)
    print(f"\nTest interest calculation for 30 days at {account.interest_rate}%: {interest:.2f} {account.amount.units}")

    # Loops for new interest rate to ensure the new interest rate doesn't stay the same.
    while True:
        new_rate = round(random.uniform(1.2, 4.0), 2)
        if new_rate != interest_rate:
            break
    account.adjust_interest_rate(new_rate)
    print(f"\nCalculate new interest for {new_rate}%: ")
    print(account)

    interest = account.calculate_interest(30)
    print(f"\nTest interest calculation for 30 days at {account.interest_rate}%: {interest:.2f} {account.amount.units}")


test_bank_acct()
