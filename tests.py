import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 2) == 8

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(20, 4) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)