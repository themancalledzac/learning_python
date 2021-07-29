# Calculator
from art import logo

# Add


def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    continue_calculator = True
    while continue_calculator:
        num2 = float(input("What's the Second number?: "))
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ") == "y":
            num1 = answer
        else:
            continue_calculator = False
            calculator()


calculator()
