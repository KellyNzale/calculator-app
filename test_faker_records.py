import pytest
from calculator import add, subtract, multiply, divide

def test_generated_records(record):
    a, b, operation, expected = record
    if operation == 'add':
        assert add(a, b) == expected
    elif operation == 'subtract':
        assert subtract(a, b) == expected
    elif operation == 'multiply':
        assert multiply(a, b) == expected
    elif operation == 'divide':
        assert divide(a, b) == expected