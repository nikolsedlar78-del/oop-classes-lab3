import pytest

from oop_tasks import Person


def test_creation():
    p = Person("Іван", 30)
    assert (p.name, p.age) == ("Іван", 30)


def test_name_is_stripped():
    assert Person("  Іван  ", 30).name == "Іван"


def test_empty_name_rejected():
    for bad in ("", "   ", None, 5):
        with pytest.raises(ValueError):
            Person(bad, 30)


def test_age_boundaries_allowed():
    assert Person("A", 0).age == 0
    assert Person("A", 150).age == 150


def test_age_out_of_range_rejected():
    for bad in (-1, 151):
        with pytest.raises(ValueError):
            Person("A", bad)


def test_age_wrong_type_rejected():
    for bad in (18.5, "18", None, True):
        with pytest.raises(ValueError):
            Person("A", bad)


def test_setters_validate_and_keep_old_value():
    p = Person("Іван", 30)
    with pytest.raises(ValueError):
        p.name = " "
    with pytest.raises(ValueError):
        p.age = 200
    assert (p.name, p.age) == ("Іван", 30)
    p.name = "  Петро "
    p.age = 40
    assert (p.name, p.age) == ("Петро", 40)


def test_is_adult_boundary():
    assert Person("A", 17).is_adult is False
    assert Person("A", 18).is_adult is True


def test_is_adult_read_only_and_follows_age():
    p = Person("A", 10)
    with pytest.raises(AttributeError):
        p.is_adult = True
    p.age = 20
    assert p.is_adult is True
