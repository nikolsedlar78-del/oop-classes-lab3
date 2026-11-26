import pytest

from oop_tasks import Inventory


def test_empty_inventory():
    inv = Inventory()
    assert inv.items() == {}
    assert inv.quantity("яблука") == 0


def test_add_and_quantity():
    inv = Inventory()
    inv.add("яблука", 10)
    assert inv.quantity("яблука") == 10


def test_add_accumulates():
    inv = Inventory()
    inv.add("яблука", 10)
    inv.add("яблука", 5)
    assert inv.quantity("яблука") == 15


def test_remove():
    inv = Inventory()
    inv.add("яблука", 10)
    inv.remove("яблука", 4)
    assert inv.quantity("яблука") == 6


def test_remove_everything_deletes_item():
    inv = Inventory()
    inv.add("яблука", 3)
    inv.remove("яблука", 3)
    assert inv.quantity("яблука") == 0
    assert "яблука" not in inv.items()


def test_remove_more_than_available_rejected():
    inv = Inventory()
    inv.add("яблука", 3)
    with pytest.raises(ValueError):
        inv.remove("яблука", 4)
    assert inv.quantity("яблука") == 3


def test_remove_unknown_item_rejected():
    with pytest.raises(ValueError):
        Inventory().remove("груші", 1)


def test_items_returns_copy():
    inv = Inventory()
    inv.add("яблука", 3)
    copy = inv.items()
    copy["яблука"] = 999
    copy["хакер"] = 1
    assert inv.items() == {"яблука": 3}


def test_internal_dict_not_public():
    inv = Inventory()
    assert not hasattr(inv, "stock")
    assert not hasattr(inv, "items_dict")
    assert hasattr(inv, "_stock")


def test_invalid_quantities_and_names():
    inv = Inventory()
    for bad in (0, -1, 1.5, "3", None, True):
        with pytest.raises(ValueError):
            inv.add("яблука", bad)
    with pytest.raises(ValueError):
        inv.add("  ", 1)
    assert inv.items() == {}
