import math

import pytest

from oop_tasks import Circle


def test_area_value():
    assert Circle(2).area == pytest.approx(math.pi * 4)


def test_no_computation_until_area_requested():
    assert Circle(2).compute_count == 0


def test_area_is_cached():
    c = Circle(2)
    c.area
    c.area
    c.area
    assert c.compute_count == 1


def test_radius_change_invalidates_cache():
    c = Circle(1)
    assert c.area == pytest.approx(math.pi)
    c.radius = 3
    assert c.area == pytest.approx(math.pi * 9)
    assert c.compute_count == 2


def test_same_radius_keeps_cache():
    c = Circle(2)
    c.area
    c.radius = 2
    c.area
    assert c.compute_count == 1


def test_radius_changed_but_area_not_requested_does_not_compute():
    c = Circle(1)
    c.area
    c.radius = 5
    c.radius = 6
    assert c.compute_count == 1


def test_non_positive_radius_rejected():
    for bad in (0, -1):
        with pytest.raises(ValueError):
            Circle(bad)


def test_invalid_radius_types_rejected():
    c = Circle(1)
    for bad in ("1", None, True, float("nan")):
        with pytest.raises(ValueError):
            c.radius = bad


def test_failed_set_keeps_state_and_cache():
    c = Circle(2)
    c.area
    with pytest.raises(ValueError):
        c.radius = -1
    assert c.radius == 2
    c.area
    assert c.compute_count == 1


def test_computed_properties_are_read_only():
    c = Circle(1)
    with pytest.raises(AttributeError):
        c.area = 5
    with pytest.raises(AttributeError):
        c.compute_count = 0
