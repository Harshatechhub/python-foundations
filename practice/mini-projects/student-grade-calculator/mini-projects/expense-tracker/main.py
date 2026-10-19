# Expense Tracker
# Mini Project 02 - Python Foundations

expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expenses ---")

    for expense in expenses:
        print(expense["name"], ":", expense["amount"])


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses:", total)


print("=== Expense Tracker ===")

add_expense()
show_expenses()
calculate_total()
