"""Задача 3.6 — клас Thermostat."""

from ._validators import require_number


class Thermostat:
    """Термостат: цільова температура обмежується (clamp) діапазоном ``[min_t, max_t]``."""

    DEFAULT_TARGET = 20

    def __init__(self, min_t=10, max_t=30, target=DEFAULT_TARGET):
        """Створює термостат. Має бути ``min_t < max_t``."""
        min_t = require_number(min_t, "min_t")
        max_t = require_number(max_t, "max_t")
        if min_t >= max_t:
            raise ValueError("min_t має бути меншим за max_t")
        self._min_t = min_t
        self._max_t = max_t
        self.target = target

    @property
    def min_t(self):
        """Нижня межа діапазону (лише читання)."""
        return self._min_t

    @property
    def max_t(self):
        """Верхня межа діапазону (лише читання)."""
        return self._max_t

    @property
    def target(self):
        """Цільова температура. Сеттер не кидає помилку, а обрізає значення до діапазону."""
        return self._target

    @target.setter
    def target(self, value):
        value = require_number(value, "Цільова температура")
        self._target = max(self._min_t, min(self._max_t, value))

    def heating_needed(self, current):
        """``True``, якщо поточна температура нижча за цільову."""
        return require_number(current, "Поточна температура") < self._target

    def __repr__(self):
        return f"Thermostat(min_t={self._min_t}, max_t={self._max_t}, target={self._target})"
