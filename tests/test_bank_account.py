import pytest

from oop_tasks import BankAccount


def test_initial_state():
    acc = BankAccount("Іван")
    assert acc.owner == "Іван"
    assert acc.balance == 0
    assert acc.history() == []


def test_deposit_and_withdraw():
    acc = BankAccount("Іван", 100)
    assert acc.deposit(50) == 150
    assert acc.withdraw(30) == 120
    assert acc.balance == 120


def test_withdraw_entire_balance_is_allowed():
    acc = BankAccount("Іван", 100)
    acc.withdraw(100)
    assert acc.balance == 0


def test_withdraw_more_than_balance_rejected():
    acc = BankAccount("Іван", 100)
    with pytest.raises(ValueError):
        acc.withdraw(100.01)
    assert acc.balance == 100


def test_balance_is_read_only():
    acc = BankAccount("Іван", 100)
    with pytest.raises(AttributeError):
        acc.balance = 1_000_000
    assert acc.balance == 100


def test_history_records_operations():
    acc = BankAccount("Іван")
    acc.deposit(100)
    acc.withdraw(40)
    assert acc.history() == [("deposit", 100), ("withdraw", 40)]


def test_history_returns_copy():
    acc = BankAccount("Іван")
    acc.deposit(10)
    acc.history().append(("hack", 999))
    assert acc.history() == [("deposit", 10)]


def test_non_positive_amounts_rejected():
    acc = BankAccount("Іван", 100)
    for bad in (0, -5, "10", None, True):
        with pytest.raises(ValueError):
            acc.deposit(bad)
        with pytest.raises(ValueError):
            acc.withdraw(bad)


def test_failed_operations_not_in_history():
    acc = BankAccount("Іван", 10)
    with pytest.raises(ValueError):
        acc.withdraw(100)
    assert acc.history() == []


def test_invalid_constructor_data():
    with pytest.raises(ValueError):
        BankAccount("  ")
    with pytest.raises(ValueError):
        BankAccount("Іван", -1)
    with pytest.raises(ValueError):
        BankAccount(123)
