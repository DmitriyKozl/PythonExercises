from CalculatorProject import art

print(art.logo)
# output
# What is the first number? 7
# +
# -
# *
# /
# pick operation: +
# what's the next number?: 3
# 7 + 3 = 10
#
# type y to continue calculation with 10 or type n to start a new calculation: y


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
    continue_calculator = True
    input1 = int(input("What is the first number?\n"))
    for operator in operators:
        print(operator)
    while continue_calculator:
        operator_symbol = input("pick an operator from the list above\n")
        input2 = int(input("What is the second number?\n"))
        answer = operators[operator_symbol](input1, input2)
        print(f"{input1} {operator_symbol} {input2}= {answer}")
        if input("Type 'y' to continue 'c' to start a new calculation") == "y":
            input1 = answer
        else:
            continue_calculator = False
            calculator()


calculator()







