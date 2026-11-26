"""Задача 3.10 — клас Email."""


class Email:
    """Адреса електронної пошти з валідацією у сеттері."""

    def __init__(self, address):
        """Створює адресу; некоректна — ``ValueError``."""
        self.address = address

    @staticmethod
    def _validate(address):
        if not isinstance(address, str):
            raise ValueError("Адреса має бути рядком")
        address = address.strip()
        if address.count("@") != 1:
            raise ValueError("Адреса має містити рівно один символ @")
        if any(ch.isspace() for ch in address):
            raise ValueError("Адреса не може містити пробілів")
        user, domain = address.split("@")
        if not user:
            raise ValueError("Частина до @ не може бути порожньою")
        if not domain:
            raise ValueError("Частина після @ не може бути порожньою")
        if "." not in domain or domain.startswith(".") or domain.endswith(".") or ".." in domain:
            raise ValueError("Домен має містити крапку між непорожніми частинами")
        return address

    @property
    def address(self):
        """Повна адреса. Сеттер перевіряє формат."""
        return self._address

    @address.setter
    def address(self, value):
        self._address = self._validate(value)

    @property
    def user(self):
        """Частина до ``@`` (лише читання)."""
        return self._address.split("@")[0]

    @property
    def domain(self):
        """Частина після ``@`` (лише читання)."""
        return self._address.split("@")[1]

    def __str__(self):
        return self._address

    def __repr__(self):
        return f"Email({self._address!r})"
