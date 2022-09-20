iterations = int(input())
sum_even = 0
sum_odd = 0

for i in range(iterations):
    current_number = int(input())
    if i % 2 == 0:
        sum_even += current_number
    else:
        sum_odd += current_number
if sum_even == sum_odd:
    print(f'Yes')
    print(f'Sum = {sum_even}')
else:
    print(f'No')
    print(f'Diff = {abs(sum_even - sum_odd)}')