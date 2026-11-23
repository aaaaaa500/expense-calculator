# expense_calc.py
# Simple expense calculator 
import json


def add_expense(expenses, name, amount, category):
    # Add one expense to the list
    expenses.append({"name": name, "amount": amount, "category": category})


def total_with_tax(expenses):
    # Sum of all expenses, each category has its own tax rate
    total = 0
    for e in expenses:
        if e["category"] == "food":
            total += e["amount"] * 1.05
        elif e["category"] == "transport":
            total += e["amount"] * 1.10
        elif e["category"] == "entertainment":
            total += e["amount"] * 1.20
        else:
            total += e["amount"]
    return total


def save_to_file(expenses, path="expenses.json"):
    # Save the list to a JSON file
    with open(path, "w") as f:
        json.dump(expenses, f)


def load_from_file(path="expenses.json"):
    # Read the list back from a JSON file
    with open(path) as f:
        return json.load(f)


def main():
    # Small demo run 
    expenses = []
    add_expense(expenses, "lunch", 100, "food")
    add_expense(expenses, "bus", 50, "transport")
    add_expense(expenses, "cinema", 200, "entertainment")
    print("Total with tax:", total_with_tax(expenses))
    save_to_file(expenses)


if __name__ == "__main__":
    main()