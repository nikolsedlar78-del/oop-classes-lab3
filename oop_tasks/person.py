"""Задача 3.3 — клас Person."""

from ._validators import require_int, require_text


class Person:
    """Людина з перевіреними ім'ям та віком."""

    MIN_AGE = 0
    MAX_AGE = 150
    ADULT_AGE = 18

    def __init__(self, name, age):
        """Створює людину; некоректні дані — ``ValueError``."""
        self.name = name
        self.age = age

    @property
    def name(self):
        """Ім'я: непорожній рядок, пробіли по краях відкидаються."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = require_text(value, "Ім'я")

    @property
    def age(self):
        """Вік: ціле число від 0 до 150."""
        return self._age

    @age.setter
    def age(self, value):
        value = require_int(value, "Вік")
        if not self.MIN_AGE <= value <= self.MAX_AGE:
            raise ValueError(f"Вік має бути від {self.MIN_AGE} до {self.MAX_AGE}")
        self._age = value

    @property
    def is_adult(self):
        """``True``, якщо вік не менший за 18 (лише читання)."""
        return self._age >= self.ADULT_AGE

    def __repr__(self):
        return f"Person(name={self._name!r}, age={self._age})"
