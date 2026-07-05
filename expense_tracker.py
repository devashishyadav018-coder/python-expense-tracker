import csv
import os

FILE_NAME = "expenses.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])

    print("Expense added successfully.\n")

def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\nExpenses")
        print("-" * 30)
        found = False

        for row in reader:
            print(f"{row[0]:20} ₹{row[1]}")
            found = True

        if not found:
            print("No expenses found.")
        print()

def total_spent():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[1])

    print(f"\nTotal Spent: ₹{total}\n")

def main():
    create_file()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()