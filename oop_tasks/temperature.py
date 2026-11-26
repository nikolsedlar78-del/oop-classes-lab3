"""Задача 3.2 — клас Temperature."""

from ._validators import require_number

ABSOLUTE_ZERO = -273.15


class Temperature:
    """Температура зі шкалами Цельсія та Фаренгейта."""

    def __init__(self, celsius=0):
        """Створює температуру в градусах Цельсія."""
        self.celsius = celsius

    @property
    def celsius(self):
        """Температура в °C. Сеттер забороняє значення нижче -273.15."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        value = require_number(value, "Температура")
        if value < ABSOLUTE_ZERO:
            raise ValueError("Температура нижча за абсолютний нуль")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Температура в °F (обчислюється з °C; можна й присвоїти)."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        value = require_number(value, "Температура")
        self.celsius = round((value - 32) * 5 / 9, 10)

    def __repr__(self):
        return f"Temperature({self._celsius})"
