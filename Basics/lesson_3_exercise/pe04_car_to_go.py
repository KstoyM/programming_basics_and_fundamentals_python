budget = float(input())
season = input()
car_type = ''
car_class = ''
price = 0

if budget <= 100:
    car_type = 'Economy class'
    if season == 'Summer':
        car_class = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car_class = 'Jeep'
        price = budget * 0.65
elif budget <= 500:
    car_type = 'Compact class'
    if season == 'Summer':
        car_class = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car_class = 'Jeep'
        price = budget * 0.8
else:
    car_type = 'Luxury class'
    car_class = 'Jeep'
    price = budget * 0.9

print(f'{car_type}')
print(f'{car_class} - {price:.2f}')