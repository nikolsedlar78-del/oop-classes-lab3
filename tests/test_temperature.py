import pytest

from oop_tasks import Temperature


def test_default_and_custom_celsius():
    assert Temperature().celsius == 0
    assert Temperature(25).celsius == 25


def test_set_celsius():
    t = Temperature(10)
    t.celsius = 30
    assert t.celsius == 30


def test_celsius_below_absolute_zero_rejected():
    t = Temperature(10)
    with pytest.raises(ValueError):
        t.celsius = -273.16
    assert t.celsius == 10


def test_absolute_zero_boundary_allowed():
    t = Temperature(-273.15)
    assert t.celsius == -273.15


def test_fahrenheit_getter():
    assert Temperature(100).fahrenheit == pytest.approx(212)
    assert Temperature(-40).fahrenheit == pytest.approx(-40)


def test_fahrenheit_setter_updates_celsius():
    t = Temperature()
    t.fahrenheit = 212
    assert t.celsius == pytest.approx(100)


def test_fahrenheit_setter_validates():
    t = Temperature(20)
    with pytest.raises(ValueError):
        t.fahrenheit = -500
    assert t.celsius == 20
    t.fahrenheit = -459.67
    assert t.celsius == pytest.approx(-273.15)


def test_invalid_types_rejected():
    with pytest.raises(ValueError):
        Temperature("hot")
    t = Temperature()
    with pytest.raises(ValueError):
        t.celsius = None
    with pytest.raises(ValueError):
        t.fahrenheit = "100"
    with pytest.raises(ValueError):
        t.celsius = float("nan")


def test_internal_attribute_is_private_by_convention():
    t = Temperature(5)
    assert t._celsius == 5
    assert not hasattr(t, "celsius_value")
