import csv
from datetime import datetime


class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        self.expenses = self.loadExpenses()

    def loadExpenses(self):
        """Load expenses from a CSV file."""
        expenses = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['amount'] = float(row['amount'])  # Convert amount to float
                    row['date'] = row['date']  # Keep date as string
                    expenses.append(row)
        except FileNotFoundError:
            # File doesn't exist, return an empty list
            return []
        return expenses

    def save_expenses(self):
        rupee= chr(8377)
        """Save expenses to a CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['date', 'description', 'amount', 'category']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)

    def add_expense(self, amount, description, category):
        """Add a new expense."""
        expense = {
            'amount': amount,
            'description': description,
            'category': category,
            'date': datetime.now().isoformat()
        }
        self.expenses.append(expense)
        self.save_expenses()

    def get_monthly_summary(self):
        """Get a summary of expenses for the current month."""
        current_month = datetime.now().month
        monthly_summary = {}

        for expense in self.expenses:
            expense_date = datetime.fromisoformat(expense['date'])
            if expense_date.month == current_month:
                category = expense['category']
                monthly_summary[category] = monthly_summary.get(category, 0) + expense['amount']

        return monthly_summary

    def get_category_summary(self):
        """Get a summary of expenses by category."""
        category_summary = {}

        for expense in self.expenses:
            category = expense['category']
            category_summary[category] = category_summary.get(category, 0) + expense['amount']

        return category_summary

    def display_Expenses(self):
        """Display all expenses."""
        rupee = chr(8377)
        total_expense = 0
        for expense in self.expenses:
            print(f"{expense['date']}: {expense['description']} - {rupee}{expense['amount']} [{expense['category']}]")
            total_expense += expense['amount']
            print(total_expense)


def main():
    tracker = ExpenseTracker()
    rupee = chr(8377)

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Display All Expenses")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            try:
                amount = float(input(f"Enter amount spent: {rupee}"))
                description = input("Enter a brief description: ")
                category = input("Enter category (e.g., food, transportation, entertainment): ")
                tracker.add_expense(amount, description, category)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")

        elif choice == '2':
            summary = tracker.get_monthly_summary()
            print("\nMonthly Summary:")
            for category, total in summary.items():
                print(f"{category}: {rupee}{total}")

        elif choice == '3':
            summary = tracker.get_category_summary()
            print("\nCategory Summary:")
            for category, total in summary.items():
                print(f"{category}: {rupee}{total}")

        elif choice == '4':
            print("\nAll Expenses:")
            tracker.display_Expenses()

        elif choice == '5':
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
