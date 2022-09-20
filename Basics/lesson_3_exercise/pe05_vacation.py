budget = float(input())
season = input()

type_of_lodging = ''
place_of_vacation = ''
price = 0

if budget <= 1000:
    type_of_lodging = 'Camp'
    if season == 'Summer':
        place_of_vacation = 'Alaska'
        price = budget * 0.65
    else:
        place_of_vacation = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    type_of_lodging = 'Hut'
    if season == 'Summer':
        place_of_vacation = 'Alaska'
        price = budget * 0.8
    else:
        place_of_vacation = 'Morocco'
        price = budget * 0.6
else:
    type_of_lodging = 'Hotel'
    price = budget * 0.9
    if season == "Summer":
        place_of_vacation = 'Alaska'
    else:
        place_of_vacation = 'Morocco'

print(f'{place_of_vacation} - {type_of_lodging} - {price:.2f}')