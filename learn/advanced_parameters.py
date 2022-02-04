
def sum_parameters(*args):
    """ variable number of arguments passed to sum function """
    # print(type(args))
    total = 0
    for value in args:
        total += value
    return total


print(sum_parameters(1, 4, 6, 9))


def calculate(n, **operations):
    """ calculate result of operation passed as variable length key-value pairs"""
    result = n
    result += operations.get("add")
    result *= operations.get("multiply")
    return result


print(calculate(5, add=10, multiply=15))
# TODO: Investigate how to ignore operation if get returns NONE
# TypeError: unsupported operand type(s) for *=: 'int' and 'NoneType'
# print(calculate(5, add=10))
# print(calculate(5, multiply=15))

# NOTE: Keys cannot be repeated in keyword arguments a.k.a **kwargs
# print(calculate(5, add=10, multiply=15, add=5))
# SyntaxError: keyword argument repeated: add
