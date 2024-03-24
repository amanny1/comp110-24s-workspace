"""Unit tests for dictionary.py functions."""

__author__ = '730668694'


import pytest
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance

def test_invert_normal():
    """Test normal case for invert."""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}

def test_invert_edge_case():
    """Test edge case for invert (e.g., empty dictionary)."""
    assert invert({}) == {}

def test_invert_key_error():
    """Test KeyError for invert."""
    with pytest.raises(KeyError):
        invert({"a": "1", "b": "1"})

# Tests for favorite_color function
def test_favorite_color_normal():
    """Test normal case for favorite_color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"

def test_favorite_color_tie():
    """Test a tie case for favorite_color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "yellow", "Kris": "blue"}) in ["yellow", "blue"]

# Tests for count function
def test_count_normal():
    """Test normal case for count."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}

def test_count_empty_list():
    """Test count with an empty list."""
    assert count([]) == {}

# Tests for alphabetizer function
def test_alphabetizer_normal():
    """Test normal case for alphabetizer."""
    assert alphabetizer(["apple", "banana", "apricot"]) == {"a": ["apple", "apricot"], "b": ["banana"]}

def test_alphabetizer_empty():
    """Test alphabetizer with an empty list."""
    assert alphabetizer([]) == {}

# Tests for update_attendance function
def test_update_attendance_new_day():
    """Test update_attendance with a new day."""
    log = {"Monday": ["Vrinda", "Kaleb"]}
    update_attendance(log, "Tuesday", "Alyssa")
    assert log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}

def test_update_attendance_existing_day():
    """Test update_attendance with an existing day."""
    log = {"Monday": ["Vrinda", "Kaleb"]}
    update_attendance(log, "Monday", "Alyssa")
    assert log == {"Monday": ["Vrinda", "Kaleb", "Alyssa"]}


