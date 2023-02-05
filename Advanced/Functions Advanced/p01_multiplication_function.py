from functools import reduce


def multiply(*args):
    num = reduce(lambda a, b: a * b, args)
    return num


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
