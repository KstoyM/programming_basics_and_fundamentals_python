def sum_number(num1, num2):
    return num1 + num2


def subtract(sum_num, num3):
    return sum_num - num3


def add_and_subtract(n1, n2, n3):
    sum_of_first_and_second = sum_number(n1, n2)
    subtracted_sum = subtract(sum_of_first_and_second, n3)
    return subtracted_sum


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
