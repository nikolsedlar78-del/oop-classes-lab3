import pytest

from oop_tasks import Email


def test_valid_address():
    e = Email("ivan@example.com")
    assert e.address == "ivan@example.com"
    assert str(e) == "ivan@example.com"


def test_user_and_domain():
    e = Email("ivan.koval@mail.example.ua")
    assert e.user == "ivan.koval"
    assert e.domain == "mail.example.ua"


def test_surrounding_spaces_stripped():
    assert Email("  a@b.com ").address == "a@b.com"


def test_missing_or_multiple_at_rejected():
    for bad in ("ivan.example.com", "a@@b.com", "a@b@c.com"):
        with pytest.raises(ValueError):
            Email(bad)


def test_empty_parts_rejected():
    for bad in ("@example.com", "ivan@", "@", ""):
        with pytest.raises(ValueError):
            Email(bad)


def test_domain_without_dot_rejected():
    with pytest.raises(ValueError):
        Email("ivan@localhost")


def test_bad_dots_in_domain_rejected():
    for bad in ("a@.com", "a@example.", "a@exa..mple.com"):
        with pytest.raises(ValueError):
            Email(bad)


def test_spaces_inside_rejected():
    with pytest.raises(ValueError):
        Email("iv an@example.com")


def test_wrong_type_rejected():
    for bad in (None, 123, ["a@b.com"]):
        with pytest.raises(ValueError):
            Email(bad)


def test_setter_validates_and_keeps_old_value():
    e = Email("a@b.com")
    with pytest.raises(ValueError):
        e.address = "broken"
    assert e.address == "a@b.com"
    e.address = "new@site.org"
    assert (e.user, e.domain) == ("new", "site.org")


def test_user_and_domain_read_only():
    e = Email("a@b.com")
    with pytest.raises(AttributeError):
        e.user = "x"
    with pytest.raises(AttributeError):
        e.domain = "x.com"
