amount_of_km = int(input())
part_of_the_day = input()

taxi_day_price = 0.7 + 0.79 * amount_of_km
taxi_night_price = 0.7 + 0.9 * amount_of_km
bus_price = 0.09 * amount_of_km  # minimum 20km
train_price = 0.06 * amount_of_km  # minimum 100km

if amount_of_km >= 100:
    print(f'{train_price:.2f}')
elif amount_of_km >= 20:
    print(f'{bus_price:.2f}')
elif amount_of_km < 20 and part_of_the_day == 'day':
    print(f'{taxi_day_price:.2f}')
elif amount_of_km < 20 and part_of_the_day == 'night':
    print(f'{taxi_night_price:.2f}')