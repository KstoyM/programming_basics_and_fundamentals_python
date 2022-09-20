turns_of_game = int(input())

numbers_till_9 = 0
numbers_from_10_to_19 = 0
numbers_from_20_to_29 = 0
numbers_from_30_to_39 = 0
numbers_from_40_to_50 = 0
score = 0
invalid_numbers = 0

for turn in range(turns_of_game):
    current_score = int(input())
    if 0 > current_score or current_score > 50:
        invalid_numbers += 1
        score /= 2
    elif 0 <= current_score <= 9:
        numbers_till_9 += 1
        score += current_score * 0.2
    elif 10 <= current_score <= 19:
        numbers_from_10_to_19 += 1
        score += current_score * 0.3
    elif 20 <= current_score <= 29:
        numbers_from_20_to_29 += 1
        score += current_score * 0.4
    elif 30 <= current_score <= 39:
        numbers_from_30_to_39 += 1
        score += 50
    elif 40 <= current_score <= 50:
        numbers_from_40_to_50 += 1
        score += 100

print(f'{score:.2f}')
print(f'From 0 to 9: {numbers_till_9 / turns_of_game:.2%}')
print(f'From 10 to 19: {numbers_from_10_to_19 / turns_of_game:.2%}')
print(f"From 20 to 29: {numbers_from_20_to_29 / turns_of_game:.2%}")
print(f'From 30 to 39: {numbers_from_30_to_39 / turns_of_game:.2%}')
print(f'From 40 to 50: {numbers_from_40_to_50 / turns_of_game:.2%}')
print(f'Invalid numbers: {invalid_numbers / turns_of_game:.2%}')
