budget = float(input())
season = input()
price_spent = 0
destination = ''
accommodation_type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price_spent = budget * 0.3
    elif season == 'winter':
        price_spent = budget * 0.7
if 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price_spent = budget * 0.4
    else:
        price_spent = budget * 0.8
if budget > 1000:
    destination = 'Europe'
    price_spent = budget * 0.9

if season == 'summer' and destination == 'Europe':
    accommodation_type = 'Hotel'
elif season == 'summer':
    accommodation_type = 'Camp'
else:
    accommodation_type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{accommodation_type} - {price_spent:.2f}')
