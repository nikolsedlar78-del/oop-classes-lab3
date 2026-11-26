"""Спільні функції перевірки значень. Усі помилки — ``ValueError``."""

import math


def require_number(value, name="Значення"):
    """Повертає ``value``, якщо це скінченне число (не ``bool``), інакше ``ValueError``."""
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name} має бути скінченним числом")
    return value


def require_int(value, name="Значення"):
    """Повертає ``value``, якщо це ціле число (не ``bool``), інакше ``ValueError``."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} має бути цілим числом")
    return value


def require_text(value, name="Значення"):
    """Повертає рядок без пробілів по краях; порожній або не-рядок — ``ValueError``."""
    if not isinstance(value, str):
        raise ValueError(f"{name} має бути рядком")
    value = value.strip()
    if not value:
        raise ValueError(f"{name} не може бути порожнім")
    return value
