from functools import reduce


def operate(op, *args):
    operations = {
        '+': reduce(lambda x, y: x + y, args),
        '-': reduce(lambda x, y: x - y, args),
        '*': reduce(lambda x, y: x * y, args),
        '/': reduce(lambda x, y: x / y, args)
    }

    return operations[op]


print(operate("/", 4, 2))
