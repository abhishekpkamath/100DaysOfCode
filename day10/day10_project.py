from art import logo

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }

def calculate():
    print(logo)
    still_calculating = True
    num1 = float(input("What is the first number?: "))
    for operation in operations:
        print(operation)
    while still_calculating:
        op = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {answer}")
        user_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to to start a new calculation: ")
        if user_continue == "y":
            num1 = answer
        else:
            still_calculating = False
            calculate()

calculate()