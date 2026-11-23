# test_expense_calc.py
# Tests for expense_calc.py
import pytest
from expense_calc import add_expense, total_with_tax, save_to_file, load_from_file


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