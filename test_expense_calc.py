# test_expense_calc.py
# Tests for expense_calc.py
import pytest

from expense_calc import add_expense, load_from_file, save_to_file, total_with_tax


def test_add_expense():
    # After adding, the list has 1 item
    expenses = []
    add_expense(expenses, "lunch", 100, "food")
    assert len(expenses) == 1


def test_total_with_tax():
    # food 100 * 1.05 + transport 50 * 1.10 = 105 + 55 = 160
    expenses = []
    add_expense(expenses, "lunch", 100, "food")
    add_expense(expenses, "bus", 50, "transport")
    assert total_with_tax(expenses) == pytest.approx(160.0)


def test_save_and_load(tmp_path):
    # tmp_path is a temporary folder that pytest gives us
    expenses = []
    add_expense(expenses, "lunch", 100, "food")
    file_path = tmp_path / "test.json"
    save_to_file(expenses, str(file_path))
    assert load_from_file(str(file_path)) == expenses


def test_all_categories_tax():
    # food 105 + transport 110 + entertainment 120 + other 100 = 435
    expenses = []
    add_expense(expenses, "lunch", 100, "food")
    add_expense(expenses, "bus", 100, "transport")
    add_expense(expenses, "cinema", 100, "entertainment")
    add_expense(expenses, "book", 100, "other")
    assert total_with_tax(expenses) == pytest.approx(435.0)


