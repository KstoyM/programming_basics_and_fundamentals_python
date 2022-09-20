iterations = int(input())
left_numbers_sum = 0
right_numbers_sum = 0

for i in range(2 * iterations):
    current_number = int(input())
    if i in range(0, iterations):
        left_numbers_sum += current_number
    else:
        right_numbers_sum += current_number
if left_numbers_sum == right_numbers_sum:
    print(f'Yes, sum = {left_numbers_sum}')
else:
    print(f'No, diff = {abs(right_numbers_sum - left_numbers_sum)}')
