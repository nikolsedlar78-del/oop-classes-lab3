"""Задача 3.7 — клас Inventory."""

from ._validators import require_int, require_text


class Inventory:
    """Склад. Словник «товар → кількість» зберігається у приватному атрибуті."""

    def __init__(self):
        """Створює порожній склад."""
        self._stock = {}

    @staticmethod
    def _positive_qty(qty):
        qty = require_int(qty, "Кількість")
        if qty <= 0:
            raise ValueError("Кількість має бути додатною")
        return qty

    def add(self, name, qty):
        """Додає ``qty`` одиниць товару ``name``."""
        name = require_text(name, "Назва товару")
        qty = self._positive_qty(qty)
        self._stock[name] = self._stock.get(name, 0) + qty

    def remove(self, name, qty):
        """Забирає ``qty`` одиниць; більше, ніж є, забрати не можна."""
        name = require_text(name, "Назва товару")
        qty = self._positive_qty(qty)
        have = self._stock.get(name, 0)
        if qty > have:
            raise ValueError(f"На складі лише {have} од. товару {name!r}")
        if qty == have:
            del self._stock[name]
        else:
            self._stock[name] = have - qty

    def quantity(self, name):
        """Кількість товару (0, якщо товару немає)."""
        return self._stock.get(name, 0)

    def items(self):
        """Повертає копію словника «товар → кількість»."""
        return dict(self._stock)

    def __repr__(self):
        return f"Inventory({self._stock})"
