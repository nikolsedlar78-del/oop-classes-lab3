"""Демонстрація роботи всіх десяти класів лабораторної 3."""

from oop_tasks import (BankAccount, Temperature, Person, Password, Rectangle,
                       Thermostat, Inventory, Student, Circle, Email)


def header(title):
    print(f"\n=== {title} ===")


def attempt(label, action):
    """Виконує дію і показує, чи її відхилено."""
    try:
        result = action()
    except (ValueError, AttributeError) as error:
        print(f"  ✗ {label}: {type(error).__name__}: {error}")
    else:
        print(f"  ✓ {label}" + (f" -> {result}" if result is not None else ""))


def demo_bank_account():
    header("3.1 BankAccount")
    a, b = BankAccount("Іван", 100), BankAccount("Олена")
    a.deposit(50)
    a.withdraw(30)
    b.deposit(500)
    print(a, "|", b)
    print("Історія Івана:", a.history())
    attempt("зняти більше, ніж є", lambda: a.withdraw(1000))

    def set_balance():
        a.balance = 10 ** 6
    attempt("a.balance = 1000000", set_balance)
    a.history().append(("hack", 1))
    print("Історія після спроби змінити копію:", a.history())


def demo_temperature():
    header("3.2 Temperature")
    t1, t2, t3 = Temperature(25), Temperature(), Temperature(-273.15)
    print(f"{t1.celsius} °C = {t1.fahrenheit} °F")
    t2.fahrenheit = 212
    print(f"Присвоїли 212 °F -> {t2.celsius} °C")
    print("Абсолютний нуль:", t3.celsius, "°C")

    def too_cold():
        t1.celsius = -300
    attempt("celsius = -300", too_cold)


def demo_person():
    header("3.3 Person")
    p1, p2, p3 = Person("  Іван ", 30), Person("Марія", 17), Person("Петро", 0)
    for p in (p1, p2, p3):
        print(p, "| повнолітній:", p.is_adult)
    attempt("Person('', 20)", lambda: Person("", 20))
    attempt("Person('A', 151)", lambda: Person("A", 151))

    def set_adult():
        p2.is_adult = True
    attempt("p2.is_adult = True", set_adult)


def demo_password():
    header("3.4 Password")
    p1, p2 = Password("secret123"), Password("secret123")
    print(p1, "| правильний:", p1.check("secret123"), "| хибний:", p1.check("wrong"))
    print("Однакові паролі — різні хеші (сіль):", p1._hash_value != p2._hash_value)
    attempt("set('short')", lambda: p1.set("short"))
    p1.set("newpassword")
    print("Після зміни: старий:", p1.check("secret123"), "| новий:", p1.check("newpassword"))


def demo_rectangle():
    header("3.5 Rectangle")
    r1, r2 = Rectangle(3, 4), Rectangle(2.5, 2)
    for r in (r1, r2):
        print(r, "площа:", r.area, "периметр:", r.perimeter)
    r1.width = 10
    print("Після width = 10:", r1.area, "| r2 не змінився:", r2.area)
    attempt("Rectangle(0, 5)", lambda: Rectangle(0, 5))


def demo_thermostat():
    header("3.6 Thermostat")
    t1, t2 = Thermostat(10, 30), Thermostat(18, 24)
    t1.target = 100
    t2.target = 5
    print("t1 (10–30), задали 100 ->", t1.target)
    print("t2 (18–24), задали 5 ->", t2.target)
    print("heating_needed(15) для t1:", t1.heating_needed(15), "| для t2:", t2.heating_needed(25))
    attempt("Thermostat(30, 10)", lambda: Thermostat(30, 10))


def demo_inventory():
    header("3.7 Inventory")
    a, b = Inventory(), Inventory()
    a.add("яблука", 10)
    a.add("груші", 5)
    b.add("яблука", 1)
    a.remove("яблука", 4)
    print("a:", a.items(), "| b:", b.items())
    a.items()["хакер"] = 1
    print("Після зміни копії a:", a.items())
    attempt("remove('груші', 99)", lambda: a.remove("груші", 99))


def demo_student():
    header("3.8 Student")
    s1, s2 = Student(1, "Марія"), Student(2, "  Іван ")
    for g in (90, 75, 100):
        s1.add_grade(g)
    s2.add_grade(60)
    print(s1, "| середня:", s1.average())
    print(s2, "| середня:", s2.average())

    def hack_grades():
        s1.grades.append(100)
    attempt("s1.grades.append(100)", hack_grades)

    def change_id():
        s1.id = 99
    attempt("s1.id = 99", change_id)
    attempt("add_grade(101)", lambda: s1.add_grade(101))


def demo_circle():
    header("3.9 Circle")
    c1, c2 = Circle(1), Circle(2)
    c1.area, c1.area, c1.area
    print(f"c1: площа {c1.area:.4f}, обчислень: {c1.compute_count} (кеш працює)")
    c1.radius = 3
    print(f"c1 після radius=3: площа {c1.area:.4f}, обчислень: {c1.compute_count}")
    print(f"c2: обчислень ще {c2.compute_count} — площу не просили")
    attempt("Circle(-1)", lambda: Circle(-1))


def demo_email():
    header("3.10 Email")
    e1, e2 = Email("ivan@example.com"), Email("  maria.k@mail.example.ua ")
    for e in (e1, e2):
        print(e, "| user:", e.user, "| domain:", e.domain)
    for bad in ("ivan.example.com", "a@@b.com", "a@localhost", "@b.com"):
        attempt(f"Email({bad!r})", lambda bad=bad: Email(bad))

    def set_user():
        e1.user = "x"
    attempt("e1.user = 'x'", set_user)


if __name__ == "__main__":
    for demo in (demo_bank_account, demo_temperature, demo_person, demo_password, demo_rectangle,
                 demo_thermostat, demo_inventory, demo_student, demo_circle, demo_email):
        demo()
