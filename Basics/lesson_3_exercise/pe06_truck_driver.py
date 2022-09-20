season = input()
km_per_month = float(input())
price_per_km = 0

if season == 'Spring' or season == 'Autumn':
    if km_per_month <= 5000:
        price_per_km = 0.75
    elif km_per_month <= 10000:
        price_per_km = 0.95
    else:
        price_per_km = 1.45
elif season == 'Summer':
    if km_per_month <= 5000:
        price_per_km = 0.90
    elif km_per_month <= 10000:
        price_per_km = 1.1
    else:
        price_per_km = 1.45
elif season == 'Winter':
    if km_per_month <= 5000:
        price_per_km = 1.05
    elif km_per_month <= 10000:
        price_per_km = 1.25
    else:
        price_per_km = 1.45

salary = price_per_km * km_per_month * 4 - (price_per_km * km_per_month * 4 * 0.1)
print(f'{salary:.2f}')