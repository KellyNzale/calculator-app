import pytest
from faker import Faker
import random
from calculator import add, subtract, multiply, divide

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=0, type=int)

fake = Faker()

@pytest.fixture(params=[(fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), op)
                        for op in ['add', 'subtract', 'multiply', 'divide']])
def record(request):
    a, b, operation = request.param
    if operation == 'add':
        expected = add(a, b)
    elif operation == 'subtract':
        expected = subtract(a, b)
    elif operation == 'multiply':
        expected = multiply(a, b)
    elif operation == 'divide':
        expected = divide(a, b)
    return a, b, operation, expected