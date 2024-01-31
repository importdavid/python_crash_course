"""Tests for the Employee class."""

import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee('David', 'Wilkins', 100000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise increments salary by $5000."""
    employee.give_raise()
    assert employee.salary == 105000

def test_give_custom_raise(employee):
    """Test that a custom raise increments thusly."""
    employee.give_raise(10000)
    assert employee.salary == 110000