month = input()
number_of_nights_stay = int(input())
price_of_apartment_per_night = 0
price_of_studio_per_night = 0
discount_studio = 0
discount_apartment = 0

if month in ['May', 'October']:
    price_of_studio_per_night = 50
    price_of_apartment_per_night = 65
elif month in ['June','September']:
    price_of_studio_per_night = 75.2
    price_of_apartment_per_night = 68.7
elif month in ['July', 'August']:
    price_of_studio_per_night = 76
    price_of_apartment_per_night = 77

total_price_apartment = price_of_apartment_per_night * number_of_nights_stay
total_price_studio = price_of_studio_per_night * number_of_nights_stay

if 7 < number_of_nights_stay <= 14 and month in ['May', 'October']:
    discount_studio = total_price_studio * 0.05
elif number_of_nights_stay > 14 and month in ['May', 'October']:
    discount_studio = total_price_studio * 0.3
elif number_of_nights_stay > 14 and month in ['June', 'September']:
    discount_studio = total_price_studio * 0.2

if number_of_nights_stay > 14:
    discount_apartment = total_price_apartment * 0.1

total_price_studio -= discount_studio
total_price_apartment -= discount_apartment

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')