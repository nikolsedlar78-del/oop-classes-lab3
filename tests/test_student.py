import pytest

from oop_tasks import Student


def test_creation():
    s = Student(1, "Марія")
    assert (s.id, s.name, s.grades) == (1, "Марія", ())


def test_id_is_read_only():
    s = Student(1, "Марія")
    with pytest.raises(AttributeError):
        s.id = 2
    assert s.id == 1


def test_name_validation_and_strip():
    s = Student(1, "  Марія ")
    assert s.name == "Марія"
    with pytest.raises(ValueError):
        s.name = ""
    assert s.name == "Марія"


def test_grades_is_tuple():
    s = Student(1, "Марія")
    s.add_grade(90)
    assert isinstance(s.grades, tuple)
    assert s.grades == (90,)


def test_grades_cannot_be_modified_from_outside():
    s = Student(1, "Марія")
    s.add_grade(90)
    with pytest.raises(AttributeError):
        s.grades.append(100)
    with pytest.raises(AttributeError):
        s.grades = (100, 100)
    assert s.grades == (90,)


def test_grade_boundaries_allowed():
    s = Student(1, "Марія")
    s.add_grade(0)
    s.add_grade(100)
    assert s.grades == (0, 100)


def test_invalid_grades_rejected():
    s = Student(1, "Марія")
    for bad in (-1, 101, "90", None, True):
        with pytest.raises(ValueError):
            s.add_grade(bad)
    assert s.grades == ()


def test_average():
    s = Student(1, "Марія")
    assert s.average() is None
    s.add_grade(80)
    s.add_grade(100)
    assert s.average() == 90


def test_invalid_id_rejected():
    for bad in (0, -5, "1", 1.5, None):
        with pytest.raises(ValueError):
            Student(bad, "Марія")
