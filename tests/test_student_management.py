import pytest

import student_management as sm


@pytest.fixture(autouse=True)
def reset_students():
    sm.students.clear()
    yield
    sm.students.clear()


def test_add_student(monkeypatch):
    inputs = iter(["101", "Alice", "85.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    sm.add_student()

    assert sm.students == [{"roll_no": "101", "name": "Alice", "marks": 85.5}]


def test_display_students_empty(capsys):
    sm.display_students()

    captured = capsys.readouterr()
    assert "No students available." in captured.out


def test_display_students_with_data(capsys):
    sm.students.append({"roll_no": "101", "name": "Alice", "marks": 85.5})

    sm.display_students()

    captured = capsys.readouterr()
    assert "Alice" in captured.out
    assert "101" in captured.out


def test_search_student_found(monkeypatch, capsys):
    sm.students.append({"roll_no": "101", "name": "Alice", "marks": 85.5})
    monkeypatch.setattr("builtins.input", lambda _: "101")

    sm.search_student()

    captured = capsys.readouterr()
    assert "Student Found" in captured.out
    assert "Alice" in captured.out


def test_search_student_not_found(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "999")

    sm.search_student()

    captured = capsys.readouterr()
    assert "Student not found." in captured.out


def test_calculate_average(capsys):
    sm.students.append({"roll_no": "101", "name": "Alice", "marks": 80.0})
    sm.students.append({"roll_no": "102", "name": "Bob", "marks": 90.0})

    sm.calculate_average()

    captured = capsys.readouterr()
    assert "Average Marks: 85.00" in captured.out


def test_calculate_average_no_students(capsys):
    sm.calculate_average()

    captured = capsys.readouterr()
    assert "No student records available." in captured.out
