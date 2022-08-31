# Calculator 
from art import logo
# add
def add(n1, n2): 
    return n1 + n2

# subtract
def subtract(n1, n2): 
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for symbols in operators:
        print(symbols)

    should_continue = True

    while should_continue:
        operator_symbols = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number?: "))

        calculation_function = operators[operator_symbols]
        answer = calculation_function(num1, num2)  

        print(f"{num1} {operator_symbols} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
