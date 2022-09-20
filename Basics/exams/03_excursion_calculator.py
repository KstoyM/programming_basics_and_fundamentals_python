amt_of_people = int(input())
season = input()

total_sum = 0

if amt_of_people <= 5:
    if season == 'spring':
        total_sum += amt_of_people * 50
    elif season == 'summer':
        total_sum += amt_of_people * 48.5
        total_sum -= total_sum * 0.15
    elif season == 'autumn':
        total_sum += amt_of_people * 60
    else:
        total_sum += amt_of_people * 86
        total_sum += total_sum * 0.08

elif amt_of_people > 5:
    if season == 'spring':
        total_sum += amt_of_people * 48
    elif season == 'summer':
        total_sum += amt_of_people * 45
        total_sum -= total_sum * 0.15
    elif season == 'autumn':
        total_sum += amt_of_people * 49.5
    else:
        total_sum += amt_of_people * 85
        total_sum += total_sum * 0.08

print(f'{total_sum:.2f} leva.')