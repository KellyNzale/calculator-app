import sys
from calculator import add, subtract, multiply, divide

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py a b operation")
        return

    a_str, b_str, operation = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
        return

    try:
        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        else:
            print(f"Unknown operation: {operation}")
            return

        print(f"The result of {a_str} {operation} {b_str} is equal to {int(result) if result.is_integer() else result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()