# Comments.

# Import reduce method.
from functools import reduce

# Gather expenses from user and sort into a list.
def get_expenses():
    expenses = []

    # Loop to gather expenses. Breaks when user inputs 'done'.
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            expense_amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, expense_amount))
        except ValueError: # If user inputs a non-number, print error message.
            print("Please input a valid number for the amount.")
    return expenses

# Function to calculate highest, lowest, and total expenses.
def calculate_expenses(expenses):
    if not expenses: # If no expenses were entered, return 0 and None.
        return 0, None, None

    # Uses reduce method to calculate total, highest, and lowest expenses.
    highest_expense = reduce(lambda acc, expense: expense if expense[1] > acc[1] else acc, expenses)
    lowest_expense = reduce(lambda acc, expense: expense if expense[1] < acc[1] else acc, expenses)
    total_expense = reduce(lambda acc, expense: acc + expense[1], expenses, 0)

    return total_expense, highest_expense, lowest_expense

# Main function to run the program.
def main():
    expenses = get_expenses()
    total, highest, lowest = calculate_expenses(expenses)

    if expenses:
        print(f"\nTotal expense amount: ${total:.2f}")
        print(f"Highest expense: {highest[0]} at ${highest[1]:.2f}")
        print(f"Lowest expense: {lowest[0]} at ${lowest[1]:.2f}")
    else:
        print("\nNo input was entered.")

if __name__ == "__main__":
    main()