# This program was created to simulate a bank account containing the name, account number, amount and interest rate.
# The test function at the end of the program tests the methods used by BankAcct using randomized values.


# Import random module. Used to randomize all values in the test function.
import random


class BankAcct:
    def __init__(self, name, acct_num, amount, interest_rate):
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.interest_rate = interest_rate

    # Adjusts the interest rate to a new rate.
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Withdraws specified amount from the account, unless funds are insufficient. Does not withdraw if insufficient.
    def withdraw(self, amount):
        if amount > self.amount:
            print("ERROR! Insufficient funds.")
            return None
        self.amount -= amount

    # Deposits specified amount into account.
    def deposit(self, amount):
        self.amount += amount

    # Returns current balance of account.
    def balance(self):
        return self.amount

    # Calculates interest based on amount, interest rate, and days passed.
    def calculate_interest(self, days):
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    # Returns string representation of account.
    def __str__(self):
        return (f"Account Holder: {self.name}\nAccount Number: {self.acct_num}\nAccount Balance: ${self.amount:.2f}"
                f"\nInterest Rate: {self.interest_rate:.2f}%")


# Test function for BankAcct. Essentially checks for successes and no errors.
def test_bank_acct():
    name = "Johan Santos"
    # Randomizes account number, initial balance, and initial interest rate.
    acct_num = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    initial_balance = random.uniform(1000, 4000)
    interest_rate = round(random.uniform(1.5, 3.5), 1)

    # Creates bank account instance.
    account = BankAcct(name, acct_num, initial_balance, interest_rate)

    print("Initial account details:")
    print(account)

    amount = random.uniform(200, 1000)
    account.deposit(amount)
    print(f"\nTest deposit of ${amount:.2f}: ")
    print(account)

    amount = random.uniform(200, account.balance())
    account.withdraw(amount)
    print(f"\nTest successful withdraw of ${amount:.2f}: ")
    print(account)

    after_successful_wd_balance = account.balance()
    amount = random.uniform(after_successful_wd_balance + 1, after_successful_wd_balance + 1500)
    print(f"\nTest failed withdrawal of ${amount:.2f}: ")
    account.withdraw(amount)
    print(account)

    interest = account.calculate_interest(30)
    print(f"\nTest interest calculation for 30 days at {account.interest_rate}%: ${interest:.2f}")

    # Loops for new interest rate to ensure the new interest rate doesn't stay the same.
    while True:
        new_rate = round(random.uniform(1.2, 4.0), 2)
        if new_rate != interest_rate:
            break
    account.adjust_interest_rate(new_rate)
    print(f"\nCalculate new interest for {new_rate}%: ")
    print(account)

    interest = account.calculate_interest(30)
    print(f"\nTest interest calculation for 30 days at {account.interest_rate}%: ${interest:.2f}")


def main():
    test_bank_acct()


if __name__ == "__main__":
    main()
