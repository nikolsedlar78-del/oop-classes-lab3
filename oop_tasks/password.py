"""Задача 3.4 — клас Password."""

import hashlib
import hmac
import os


class Password:
    """Зберігає лише сіль і хеш пароля (PBKDF2-SHA256), сам пароль — ніколи."""

    MIN_LENGTH = 8
    ITERATIONS = 100_000

    def __init__(self, password):
        """Створює об'єкт із початковим паролем (мінімум 8 символів)."""
        self.set(password)

    @classmethod
    def _hash(cls, password, salt):
        return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, cls.ITERATIONS)

    def set(self, new):
        """Встановлює новий пароль: рядок довжиною не менше 8 символів."""
        if not isinstance(new, str):
            raise ValueError("Пароль має бути рядком")
        if len(new) < self.MIN_LENGTH:
            raise ValueError(f"Пароль має містити щонайменше {self.MIN_LENGTH} символів")
        salt = os.urandom(16)
        self._salt = salt
        self._hash_value = self._hash(new, salt)

    def check(self, candidate):
        """Повертає ``True``, якщо ``candidate`` збігається з паролем."""
        if not isinstance(candidate, str):
            return False
        return hmac.compare_digest(self._hash(candidate, self._salt), self._hash_value)

    def __repr__(self):
        return "Password(****)"
