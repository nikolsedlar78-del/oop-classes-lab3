"""Задача 3.9 — клас Circle."""

import math

from ._validators import require_number


class Circle:
    """Коло з кешованою площею; ``compute_count`` показує, скільки разів площу рахували."""

    def __init__(self, radius):
        """Створює коло з додатним радіусом."""
        self._area = None
        self._compute_count = 0
        self._radius = None
        self.radius = radius

    @property
    def radius(self):
        """Радіус (``> 0``). Зміна радіуса скидає кеш площі."""
        return self._radius

    @radius.setter
    def radius(self, value):
        value = require_number(value, "Радіус")
        if value <= 0:
            raise ValueError("Радіус має бути додатним")
        if value != self._radius:
            self._radius = value
            self._area = None

    @property
    def area(self):
        """Площа кола; перераховується лише якщо радіус змінився."""
        if self._area is None:
            self._area = math.pi * self._radius ** 2
            self._compute_count += 1
        return self._area

    @property
    def compute_count(self):
        """Скільки разів площа реально обчислювалась (лише читання)."""
        return self._compute_count

    def __repr__(self):
        return f"Circle(radius={self._radius})"
