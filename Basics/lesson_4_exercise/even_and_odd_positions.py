from sys import maxsize

iterations = int(input())

even_sum = 0
odd_sum = 0
even_max = -maxsize
even_min = maxsize
odd_max = -maxsize
odd_min = maxsize

for i in range(1, iterations + 1):
    curr_number = float(input())
    if i % 2 != 0:
        odd_sum += curr_number
        odd_max = max(odd_max, curr_number)
        odd_min = min(odd_min, curr_number)

    else:
        even_sum += curr_number
        even_max = max(even_max, curr_number)
        even_min = min(even_min, curr_number)


print(f'OddSum={odd_sum:.2f},')
if odd_min == maxsize or odd_max == -maxsize:
    print(f'OddMin=No,')
    print(f'OddMax=No,')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if even_min == maxsize or even_max == -maxsize:
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')