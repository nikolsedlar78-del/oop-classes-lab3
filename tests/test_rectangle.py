import pytest

from oop_tasks import Rectangle


def test_area_and_perimeter():
    r = Rectangle(3, 4)
    assert r.area == 12
    assert r.perimeter == 14


def test_float_sides():
    r = Rectangle(2.5, 2)
    assert r.area == 5.0


def test_changing_side_updates_computed_values():
    r = Rectangle(3, 4)
    r.width = 10
    assert r.area == 40
    assert r.perimeter == 28


def test_zero_side_rejected():
    with pytest.raises(ValueError):
        Rectangle(0, 5)
    with pytest.raises(ValueError):
        Rectangle(5, 0)


def test_negative_side_rejected():
    r = Rectangle(1, 1)
    with pytest.raises(ValueError):
        r.width = -1
    with pytest.raises(ValueError):
        r.height = -0.1


def test_non_numbers_rejected():
    for bad in ("5", None, True, float("inf")):
        with pytest.raises(ValueError):
            Rectangle(bad, 1)


def test_failed_set_keeps_old_value():
    r = Rectangle(3, 4)
    with pytest.raises(ValueError):
        r.width = 0
    assert r.width == 3


def test_area_and_perimeter_read_only():
    r = Rectangle(3, 4)
    with pytest.raises(AttributeError):
        r.area = 100
    with pytest.raises(AttributeError):
        r.perimeter = 100


def test_very_small_positive_side_allowed():
    assert Rectangle(0.001, 1000).area == pytest.approx(1)
