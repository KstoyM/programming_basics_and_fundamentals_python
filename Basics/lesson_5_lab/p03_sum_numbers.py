number = int(input())
total_num2 = 0

while total_num2 <= number:
    number2 = int(input())
    total_num2 += number2
    if total_num2 >= number:
        print(total_num2)
        break