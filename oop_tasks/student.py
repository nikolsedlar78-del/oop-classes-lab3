"""Задача 3.8 — клас Student."""

from ._validators import require_int, require_number, require_text


class Student:
    """Студент із незмінним ``id``, іменем та оцінками (0..100)."""

    MIN_GRADE = 0
    MAX_GRADE = 100

    def __init__(self, student_id, name):
        """Створює студента; ``student_id`` — додатне ціле, ім'я — непорожнє."""
        student_id = require_int(student_id, "id")
        if student_id <= 0:
            raise ValueError("id має бути додатним")
        self._id = student_id
        self.name = name
        self._grades = []

    @property
    def id(self):
        """Ідентифікатор (лише читання)."""
        return self._id

    @property
    def name(self):
        """Ім'я студента (непорожнє)."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = require_text(value, "Ім'я")

    @property
    def grades(self):
        """Оцінки у вигляді кортежу (змінити ззовні неможливо)."""
        return tuple(self._grades)

    def add_grade(self, grade):
        """Додає оцінку від 0 до 100."""
        grade = require_number(grade, "Оцінка")
        if not self.MIN_GRADE <= grade <= self.MAX_GRADE:
            raise ValueError(f"Оцінка має бути від {self.MIN_GRADE} до {self.MAX_GRADE}")
        self._grades.append(grade)

    def average(self):
        """Середня оцінка або ``None``, якщо оцінок ще немає."""
        if not self._grades:
            return None
        return sum(self._grades) / len(self._grades)

    def __repr__(self):
        return f"Student(id={self._id}, name={self._name!r}, grades={self.grades})"
