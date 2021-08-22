def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


number1 = int(input("Enter 1st number "))
number2 = int(input("Enter 2nd number "))
operation = input("Enter operation ")

print(operations[operation](number1, number2))

