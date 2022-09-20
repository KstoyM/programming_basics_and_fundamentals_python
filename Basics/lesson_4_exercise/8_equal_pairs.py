number_of_pairs = int(input())

current_pair = 0
previous_pair = 0
current_difference = 0
previous_difference = 0

for n in range(number_of_pairs * 2):
    current_number = int(input())
    current_pair += current_number

    if n % 2 != 0 and n >= 3:
        current_difference = max(current_difference, abs(current_pair - previous_pair))
        previous_pair = current_pair
        current_pair = 0

    elif n % 2 != 0 and n >= 1:
        previous_pair = current_pair
        current_pair = 0


if current_difference == 0:
    print(f'Yes, value={previous_pair}')
else:
    print(f'No, maxdiff={current_difference}')