"""Задача 3.1 — клас BankAccount."""

from ._validators import require_number, require_text


class BankAccount:
    """Банківський рахунок. Баланс можна змінити лише через ``deposit``/``withdraw``."""

    def __init__(self, owner, balance=0):
        """Створює рахунок із власником і початковим балансом (``>= 0``)."""
        self._owner = require_text(owner, "Власник")
        balance = require_number(balance, "Баланс")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self._balance = balance
        self._history = []

    @property
    def owner(self):
        """Власник рахунку (лише читання)."""
        return self._owner

    @property
    def balance(self):
        """Поточний баланс (лише читання)."""
        return self._balance

    def deposit(self, amount):
        """Поповнює рахунок на додатну суму; повертає новий баланс."""
        amount = require_number(amount, "Сума")
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною")
        self._balance = round(self._balance + amount, 2)
        self._history.append(("deposit", amount))
        return self._balance

    def withdraw(self, amount):
        """Знімає кошти; баланс не може стати нижчим за 0. Повертає новий баланс."""
        amount = require_number(amount, "Сума")
        if amount <= 0:
            raise ValueError("Сума зняття має бути додатною")
        if amount > self._balance:
            raise ValueError("Недостатньо коштів")
        self._balance = round(self._balance - amount, 2)
        self._history.append(("withdraw", amount))
        return self._balance

    def history(self):
        """Повертає копію списку операцій ``[(тип, сума), ...]``."""
        return list(self._history)

    def __repr__(self):
        return f"BankAccount(owner={self._owner!r}, balance={self._balance})"
