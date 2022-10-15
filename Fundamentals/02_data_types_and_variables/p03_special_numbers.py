number = int(input())

sum_of_digits = 0

for n1 in range(1, number + 1):
    sum_of_digits += n1 % 10
    sum_of_digits += n1 // 10
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 15:
        print(f'{n1} -> True')
    else:
        print(f'{n1} -> False')
    sum_of_digits = 0