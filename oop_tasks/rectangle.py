"""Задача 3.5 — клас Rectangle."""

from ._validators import require_number


class Rectangle:
    """Прямокутник із додатними сторонами та обчислюваними площею й периметром."""

    def __init__(self, width, height):
        """Створює прямокутник; сторони мають бути додатними числами."""
        self.width = width
        self.height = height

    @staticmethod
    def _positive(value, name):
        value = require_number(value, name)
        if value <= 0:
            raise ValueError(f"{name} має бути додатною")
        return value

    @property
    def width(self):
        """Ширина (``> 0``)."""
        return self._width

    @width.setter
    def width(self, value):
        self._width = self._positive(value, "Ширина")

    @property
    def height(self):
        """Висота (``> 0``)."""
        return self._height

    @height.setter
    def height(self, value):
        self._height = self._positive(value, "Висота")

    @property
    def area(self):
        """Площа (лише читання)."""
        return self._width * self._height

    @property
    def perimeter(self):
        """Периметр (лише читання)."""
        return 2 * (self._width + self._height)

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"
