import json
import os
from datetime import datetime

# File to store expense data
EXPENSE_FILE = 'expense_data.json'

def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    else:
        return {'expenses': []}

def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=2)

def record_expense(expenses, category, amount):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expense_entry = {'timestamp': timestamp, 'category': category, 'amount': amount}
    expenses['expenses'].append(expense_entry)
    save_expenses(expenses)

def show_summary(expenses):
    categories = {}
    total_expense = 0

    for entry in expenses['expenses']:
        category = entry['category']
        amount = entry['amount']
        
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

        total_expense += amount

    print("\nExpense Summary:")
    print("Total Expenses: ${}".format(total_expense))
    print("Category-wise Expenses:")
    
    for category, amount in categories.items():
        print("{}: ${}".format(category, amount))

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Record Expense")
        print("2. Show Expense Summary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            record_expense(expenses, category, amount)
            print("Expense recorded successfully!")

        elif choice == '2':
            show_summary(expenses)

        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
