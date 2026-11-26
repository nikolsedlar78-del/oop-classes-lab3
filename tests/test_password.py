import pytest

from oop_tasks import Password


def test_check_correct_password():
    assert Password("secret123").check("secret123") is True


def test_check_wrong_password():
    p = Password("secret123")
    assert p.check("Secret123") is False
    assert p.check("") is False


def test_minimum_length_boundary():
    assert Password("12345678").check("12345678") is True
    with pytest.raises(ValueError):
        Password("1234567")


def test_set_changes_password():
    p = Password("oldpassword")
    p.set("newpassword")
    assert p.check("newpassword") is True
    assert p.check("oldpassword") is False


def test_failed_set_keeps_old_password():
    p = Password("oldpassword")
    with pytest.raises(ValueError):
        p.set("short")
    assert p.check("oldpassword") is True


def test_set_wrong_type_rejected():
    p = Password("oldpassword")
    for bad in (None, 12345678, b"password"):
        with pytest.raises(ValueError):
            p.set(bad)


def test_plain_password_is_not_stored():
    p = Password("supersecret")
    assert "supersecret" not in repr(vars(p))
    assert "supersecret" not in repr(p)
    assert not hasattr(p, "password")


def test_same_password_gives_different_hashes():
    a, b = Password("samepassword"), Password("samepassword")
    assert a._hash_value != b._hash_value


def test_check_non_string_returns_false():
    p = Password("secret123")
    assert p.check(None) is False
    assert p.check(123456789) is False
