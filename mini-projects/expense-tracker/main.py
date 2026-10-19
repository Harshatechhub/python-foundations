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

    print("\n--- All Expenses ---")

    for expense in expenses:
        print(f"{expense['name']}: ₹{expense['amount']}")


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal expenses: ₹{total}")


while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
