import subprocess

def run_main(args):
    return subprocess.run(['python', 'main.py'] + args, capture_output=True, text=True).stdout.strip()

def test_main_add():
    assert run_main(['5', '3', 'add']) == "The result of 5 add 3 is equal to 8"

def test_main_divide_by_zero():
    assert run_main(['1', '0', 'divide']) == "An error occurred: Cannot divide by zero"

def test_main_unknown():
    assert run_main(['9', '3', 'unknown']) == "Unknown operation: unknown"

def test_main_invalid_a():
    assert run_main(['a', '3', 'add']) == "Invalid number input: a or 3 is not a valid number."

def test_main_invalid_b():
    assert run_main(['5', 'b', 'subtract']) == "Invalid number input: 5 or b is not a valid number."
