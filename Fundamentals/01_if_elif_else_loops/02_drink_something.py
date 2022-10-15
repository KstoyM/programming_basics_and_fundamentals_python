person_age = int(input())
drink_type = ''

if person_age <= 14:
    drink_type = 'toddy'
elif person_age <= 18:
    drink_type = 'coke'
elif person_age <= 21:
    drink_type = 'beer'
else:
    drink_type = 'whisky'

print(f'drink {drink_type}')
