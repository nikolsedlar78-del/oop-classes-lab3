# Лабораторна 3 — ООП у Python: захист стану об'єкта

Приватні атрибути (`_x`), `@property`, валідація в сеттерах. Десять класів, демонстрація та тести на `pytest`.

## Структура

```
oop-classes-lab3/
├── oop_tasks/
│   ├── _validators.py   # спільні перевірки (число, ціле, непорожній рядок) → ValueError
│   ├── bank_account.py  # 3.1  BankAccount — баланс лише для читання, history() — копія
│   ├── temperature.py   # 3.2  Temperature — celsius (>= -273.15), fahrenheit (читання/запис)
│   ├── person.py        # 3.3  Person      — ім'я, вік 0..150, is_adult
│   ├── password.py      # 3.4  Password    — зберігає сіль і хеш (PBKDF2), не пароль
│   ├── rectangle.py     # 3.5  Rectangle   — width/height > 0, area, perimeter
│   ├── thermostat.py    # 3.6  Thermostat  — clamp цільової температури
│   ├── inventory.py     # 3.7  Inventory   — приватний словник, items() — копія
│   ├── student.py       # 3.8  Student     — незмінний id, grades — кортеж
│   ├── circle.py        # 3.9  Circle      — кешована площа, compute_count
│   └── email.py         # 3.10 Email       — валідація адреси, user/domain лише читання
├── tests/               # по одному файлу на клас
├── demo.py              # демонстрація для 2–3 об'єктів, включно зі спробами порушити захист
├── pytest.ini
└── .gitignore
```

## Запуск

```bash
pip install pytest
python demo.py
python -m pytest -v
```

## Рішення, які варто знати

- Усі внутрішні дані мають префікс `_`; публічний доступ — через `@property`.
- Некоректні значення (включно з неправильним типом, `bool`, `NaN`, `inf`) дають `ValueError`.
  Спроба присвоїти властивості без сеттера дає `AttributeError` — це стандартна поведінка Python.
- Невдале присвоєння не змінює стан: старе значення зберігається.
- `Thermostat.target` не кидає помилку, а обрізає значення до `[min_t, max_t]`; кидає лише для не-числа.
- `Password`: PBKDF2-HMAC-SHA256, випадкова сіль на кожну установку пароля, порівняння через
  `hmac.compare_digest`. `check()` з не-рядком повертає `False`.
- `Circle.radius = те саме значення` кеш не скидає; площа рахується лише за запитом.
- Оцінки `Student` — від 0 до 100; додатково є `average()`.
- Приватність у Python — домовленість, а не жорсткий захист: `obj._x` технічно доступний.
