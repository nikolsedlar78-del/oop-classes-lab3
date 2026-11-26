import pytest

from oop_tasks import Thermostat


def test_defaults():
    t = Thermostat()
    assert (t.min_t, t.max_t, t.target) == (10, 30, 20)


def test_target_within_range():
    t = Thermostat(10, 30)
    t.target = 25
    assert t.target == 25


def test_target_clamped_to_max():
    t = Thermostat(10, 30)
    t.target = 100
    assert t.target == 30


def test_target_clamped_to_min():
    t = Thermostat(10, 30)
    t.target = -50
    assert t.target == 10


def test_target_boundaries_kept():
    t = Thermostat(10, 30)
    t.target = 10
    assert t.target == 10
    t.target = 30
    assert t.target == 30


def test_default_target_clamped_if_outside_range():
    assert Thermostat(22, 28).target == 22
    assert Thermostat(0, 15).target == 15


def test_heating_needed():
    t = Thermostat(10, 30, 22)
    assert t.heating_needed(18) is True
    assert t.heating_needed(22) is False
    assert t.heating_needed(25) is False


def test_invalid_range_rejected():
    with pytest.raises(ValueError):
        Thermostat(30, 10)
    with pytest.raises(ValueError):
        Thermostat(10, 10)


def test_invalid_values_rejected():
    t = Thermostat()
    with pytest.raises(ValueError):
        t.target = "hot"
    with pytest.raises(ValueError):
        t.heating_needed(None)
    with pytest.raises(ValueError):
        Thermostat("a", 30)


def test_range_is_read_only():
    t = Thermostat()
    with pytest.raises(AttributeError):
        t.min_t = 0
    with pytest.raises(AttributeError):
        t.max_t = 100
