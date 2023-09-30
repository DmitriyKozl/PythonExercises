from CalculatorProject import art
import os


def subtract(a, b):
    return a - b


def add(a, b):
    return a+b


def dev(a, b):
    return a/b


def multiply(a, b):
    return a*b


operators = {
    "+": add,
    "-": subtract,
    "/": dev,
    "*": multiply
}


def calculator():
    print(art.logo)

    continue_calculator = True
    input1 = float(input("What is the first number?\n"))
    for operator in operators:
        print(operator)
    while continue_calculator:
        operator_symbol = input("pick an operator from the list above\n")
        input2 = float(input("What is the second number?\n"))
        answer = operators[operator_symbol](input1, input2)
        print(f"{input1} {operator_symbol} {input2}= {answer}")
        if input("Type 'y' to continue 'c' to start a new calculation") == "y":
            input1 = answer
        else:
            continue_calculator = False
            os.system('cls')
            calculator()


calculator()







