# expense_calc.py
# Simple expense calculator / Простой калькулятор расходов
import json
from collections.abc import Callable

# A tax strategy is a function: takes an amount, returns amount with tax
# Стратегия налога это функция: берёт сумму, возвращает сумму с налогом
TaxStrategy = Callable[[float], float]


def with_multiplier(multiplier: float) -> TaxStrategy:
    # Build a strategy that multiplies the amount (1.05 = +5%)
    # Создаём стратегию, которая умножает сумму (1.05 = +5%)
    def apply(amount: float) -> float:
        return amount * multiplier

    return apply


def no_tax(amount: float) -> float:
    # Strategy for unknown categories: amount stays the same
    # Стратегия для неизвестных категорий: сумма не меняется
    return amount


# Category name -> its tax strategy. To add a category, add one line here.
# Название категории -> её стратегия. Новая категория это одна строка здесь.
TAX_STRATEGIES: dict[str, TaxStrategy] = {
    "food": with_multiplier(1.05),
    "transport": with_multiplier(1.10),
    "entertainment": with_multiplier(1.20),
}


def add_expense(expenses, name, amount, category):
    # Add one expense to the list
    # Добавляем один расход в список
    expenses.append({"name": name, "amount": amount, "category": category})


def total_with_tax(expenses):
    # Sum of all expenses, tax is chosen by category strategy
    # Сумма всех расходов, налог выбирается стратегией по категории
    total = 0
    for e in expenses:
        strategy = TAX_STRATEGIES.get(e["category"], no_tax)
        total += strategy(e["amount"])
    return total


def save_to_file(expenses, path="expenses.json"):
    # Save the list to a JSON file
    # Сохраняем список в JSON-файл
    with open(path, "w") as f:
        json.dump(expenses, f)


def load_from_file(path="expenses.json"):
    # Read the list back from a JSON file
    # Читаем список обратно из JSON-файла
    with open(path) as f:
        return json.load(f)


def main():
    # Small demo run / Небольшой демо-запуск
    expenses = []
    add_expense(expenses, "lunch", 100, "food")
    add_expense(expenses, "bus", 50, "transport")
    add_expense(expenses, "cinema", 200, "entertainment")
    print("Total with tax:", total_with_tax(expenses))
    save_to_file(expenses)


if __name__ == "__main__":
    main()