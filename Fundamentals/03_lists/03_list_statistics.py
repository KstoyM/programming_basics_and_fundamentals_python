count_of_numbers = int(input())
positives_list = []
negatives_list = []

for number_index in range(count_of_numbers):
    current_number = int(input())
    if current_number >= 0:
        positives_list.append(current_number)
    else:
        negatives_list.append(current_number)

print(positives_list)
print(negatives_list)
print(f'Count of positives: {len(positives_list)}')
print(f'Sum of negatives: {sum(negatives_list)}')