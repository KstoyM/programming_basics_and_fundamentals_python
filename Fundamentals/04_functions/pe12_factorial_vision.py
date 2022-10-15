def fact_division(num1, num2):
    num1_factorial = 1
    num2_factorial = 1
    for n1 in range(2, num1 + 1):
        num1_factorial *= n1
    for n2 in range(2, num2 + 1):
        num2_factorial *= n2
    return f'{num1_factorial / num2_factorial:.2f}'


input_num1, input_num2 = int(input()), int(input())
print(fact_division(input_num1, input_num2))
